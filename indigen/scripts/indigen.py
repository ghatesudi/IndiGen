from indigen.main import init
from indigen.utils.state_utils import get_state_modules

def main():
    """Main function for the name generator script."""
    print("Welcome to the State Name Generator!")

    # Test the `init` function
    print("\nInitializing the generator...")
    try:
        init()  # This could set up the environment or provide an introduction
    except Exception as e:
        print(f"Error during initialization: {e}")

    # Test the `get_state_modules` function
    print("\nRetrieving state modules...")
    try:
        state_modules = get_state_modules()
        print(f"Available state modules: {state_modules}")
    except Exception as e:
        print(f"Error while retrieving state modules: {e}")


if __name__ == "__main__":
    main()
