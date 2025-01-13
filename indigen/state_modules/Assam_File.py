import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
# The init function that sets user preferences
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

def generate_assam_names(n, user_preference=None):
    # Male and Female First Names
    male_assam_firstname = ["Abhijeet", "Akashdeep", "Anirban", "Arup", "Biswajit", "Barun", "Bhaskar", "Banikanta", "Bhabesh", 
                            "Bidyut", "Bhupen", "Bhargav", "Bodhi", "Bhanuprasad", "Chandan", "Chitragupt", "Charan", "Chinmoy", 
                            "Dinesh", "Devendra", "Debojit", "Dipankar", "Dipesh", "Debasish", "Dhrubajyoti", "Dhiraj", "Durgesh", 
                            "Gouranga", "Gunadhar", "Gopal", "Gokul", "Gautam", "Hemanta", "Harihar", "Hiren", "Hemendra", "Harish"]
    
    female_assam_firstname = ["Ananya", "Aaratrika", "Aishani", "Aloka", "Alpana", "Anamika", "Anindita", "Aparajita", 
                              "Arpita", "Arundhati", "Asmita", "Avantika", "Bandita", "Barnali", "Barsha", "Bijoya", "Bipasha", 
                              "Bithika", "Chandana", "Charulata", "Chhanda", "Chhaya", "Debjani", "Debika", "Deepanjali", "Deepa", 
                              "Devika", "Diya", "Dolon", "Dwipti", "Ela", "Eshita", "Gauri", "Haimanti", "Ila", "Indrani", "Ishani"]
    
    # Surnames common in Assam
    assam_surname = ['Kalita', 'Thakuria', 'Bhuyan', 'Borah', 'Sarmah', 'Laskar', 'Pathak', 'Maheshwari', 'Gayan', 'Boro', 'Pujari', 'Bharali', 
                     'Sikdar', 'Talukdar', 'Pradhani', 'Baroowa', 'Barpatra', 'Chaliha', 'Deka', 'Barman', 'Bora', 'Parashar', 'Sinha', 
                     'Morang', 'Mahanta', 'Doley', 'Chakravarty', 'Bhattacharya', 'Phukan', 'Bishwas', 'Saikia', 'Baruah', 'Borthakur']

    # Initialize user preferences (default to 'full' name type if not passed)
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(male_assam_firstname)
        last_name_male = random.choice(assam_surname)
        
        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

                
        # Female Name Generation
        first_name_female = random.choice(female_assam_firstname)
        last_name_female = random.choice(assam_surname)
        
        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female  # Full name

        # Append female name with gender information
        # Append male name with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Ensure file writing happens
    file_path = 'generated_assam_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')
    
    print(f"Names have been written to '{file_path}' successfully.")
    return df
