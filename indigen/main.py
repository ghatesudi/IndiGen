import os
import importlib
from .utils.state_utils import get_state_modules  # Assuming you have this utility function
import pandas as pd
from .utils.common import save_names_to_csv, format_name_data
import sys

def dynamic_import_state_functions():
    """Dynamically import all state modules and return a dictionary of functions."""
    state_modules = get_state_modules()  # Get state module names from the directory
    state_functions = {}

    #print(f"Available state modules: {state_modules}")  # Debug print

    # Ensure the state_modules path is in the system path for dynamic imports
    current_dir = os.path.dirname(__file__)
    state_modules_path = os.path.join(current_dir, '..', 'indigen', 'state_modules')  # Adjust if necessary
    if state_modules_path not in sys.path:
        sys.path.append(state_modules_path)

    for state_module in state_modules:
        try:
            # Dynamically import the module (e.g., Assam_File -> Assam)
            module_name = f"indigen.state_modules.{state_module}"  # Full path to module
            module = importlib.import_module(module_name)

            # Dynamically get the function name (e.g., generate_assam_names from Assam_File)
            function_name = f"generate_{state_module.split('_')[0].lower()}_names"
            state_functions[state_module] = getattr(module, function_name)

            #print(f"Successfully imported: {state_module}")  # Debug print

        except ImportError as e:
            print(f"Error importing module {state_module}: {e}")
        except AttributeError as e:
            print(f"Error getting function from {state_module}: {e}")

    #print(f"State functions available: {state_functions}")  # Debugging the function dictionary
    return state_functions


def display_menu():
    """Display the user menu."""
    print("\nWelcome to the State Name Generator!")
    print("Options:")
    print("1. Generate names for a specific state")
    print("2. Generate names from all states (default)")

def get_state_choice():
    """Prompt the user to select a state or choose all states."""
    state_functions = dynamic_import_state_functions()  # Get state functions dynamically

    # Show the available states
    print("Available states:")
    all_states = list(state_functions.keys())  # List of available states
    #print(f"Available states: {all_states}")  # Debug print

    if not all_states:
        print("No states available. Exiting.")
        return None, None, None
    
    for idx, state in enumerate(all_states, 1):
        print(f"{idx}. {state}")

    state_choice = input("Enter the state number, name, or 'all' for all states: ").strip()
    if state_choice.lower() == 'all' or state_choice == '':
        print(f"You entered: 'ALL STATES'")
    else:
        print(f"You entered: '{state_choice}'")  # Debug print

    if state_choice.lower() == 'all' or state_choice == '':  # If the user selects 'all' or leaves it blank
        return 'all', all_states, state_functions  # Return 'all' to indicate all states should be processed

    if state_choice.isdigit():  # If the user enters a number
        state_index = int(state_choice) - 1
        if state_index < 0 or state_index >= len(all_states):
            print("Invalid state selection. Exiting.")
            return None, None, None
        selected_state = all_states[state_index]
        return selected_state, all_states, state_functions

    elif state_choice in all_states:  # If the user enters a valid state name
        selected_state = state_choice
        return selected_state, all_states, state_functions

    else:
        print("Invalid state selection. Exiting.")
        return None, None, None


def get_number_of_names():
    """Prompt the user to enter the number of names they want to generate."""
    try:
        num_names = int(input("Enter the number of names to generate: ").strip())
        return num_names
    except ValueError:
        print("Invalid input. Exiting.")
        return None

def get_name_type():
    """Ask the user if they want to generate first names or full names."""
    name_type = input("Generate first names only? (yes/no, default is no): ").strip().lower()
    if name_type == "yes":
        return {'name_type': 'first'}
    else:
        return {'name_type': 'full'}

def main():
    """Main function to drive the name generation process."""
    
    # Display the menu
    display_menu()

    # Get the user's choice of state(s)
    state_choice, all_states, state_functions = get_state_choice()

    # Validate user input for state choice
    if state_choice is None:
        return

    # Get the number of names to generate
    num_names = get_number_of_names()
    if num_names is None:
        return
    
    # Get the name type (first or full)
    user_preference = get_name_type()

    # Generate the names for the selected state(s)
    print("\nGenerated Names:")
    try:
        if state_choice == 'all':
            # Generate names for all states
            for state in all_states:
                generate_function = state_functions.get(state)
                if callable(generate_function):
                    print(f"\nGenerating names for {state}...")
                    names = generate_function(num_names, user_preference)
                    if isinstance(names, pd.DataFrame):
                        print(names.to_string(index=False))
                    else:
                        print(f"Error: The function did not return a DataFrame. It returned {type(names)}")
                else:
                    print(f"Error: {generate_function} is not a valid function.")
        else:
            # Generate names for the selected state
            generate_function = state_functions.get(state_choice)
            if callable(generate_function):
                names = generate_function(num_names, user_preference)
                if isinstance(names, pd.DataFrame):
                    print(names.to_string(index=False))
                else:
                    print(f"Error: The function did not return a DataFrame. It returned {type(names)}")
            else:
                print(f"Error: {generate_function} is not a valid function.")
    except Exception as e:
        print(f"Error generating names: {e}")

def init():
    """Initialize the package and call the main function."""
    #print("Initializing the name generator package...")
    main()


if __name__ == "__main__":
    main()
