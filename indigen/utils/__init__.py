# utils/__init__.py
import os  # Add this import

def get_state_modules():
    """Discover all state modules in the state_modules folder."""
    current_dir = os.path.dirname(__file__)  # Now 'os' is available
    files = os.listdir(current_dir)
    state_modules = [os.path.splitext(f)[0] for f in files if f.endswith(".py") and f not in ("__init__.py", "main.py")]
    return state_modules
