import pandas as pd

# Helper function to save names to a CSV file
def save_names_to_csv(names, filename='generated_names.csv'):
    """Save generated names to a CSV file."""
    df = pd.DataFrame(names, columns=["Name", "Gender"])
    df.to_csv(filename, index=False)
    print(f"Names have been saved to {filename}")

# Helper function to create a state function-friendly format
def format_name_data(names, gender_data):
    """Format name data in a way that is easy to pass to the state generation functions."""
    formatted_data = [(name, gender) for name, gender in zip(names, gender_data)]
    return formatted_data
