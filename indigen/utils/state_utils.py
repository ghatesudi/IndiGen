import os

def get_state_modules():
    """Get the list of state module filenames in the 'state_modules' directory."""
    current_dir = os.path.dirname(__file__)  # Get the current directory
    package_root = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Going two levels up to indigen
    state_dir = os.path.join(package_root, 'indigen', 'state_modules')  # Corrected path

    # Debugging: print the path to the state_modules folder
    #print(f"Looking for state modules in: {state_dir}")

    # Check if the directory exists
    if not os.path.exists(state_dir):
        print(f"Error: {state_dir} does not exist!")
        return []

    # Get all Python files in the state_modules folder (without .py extension)
    state_modules = [
        f[:-3]  # Remove the '.py' extension
        for f in os.listdir(state_dir)
        if f.endswith('.py') and f != '__init__.py'  # Exclude '__init__.py'
    ]

    return state_modules
