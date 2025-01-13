# name_package/__init__.py

# Import the main entry point function
from .main import init  # Ensure 'init' exists in main.py

# Import utility functions (if needed for external usage)
from .utils.state_utils import get_state_modules  # Correct import path

__version__ = "0.1"
__author__ = "Sudeep Ghate"
