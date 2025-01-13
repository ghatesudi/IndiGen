import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Orissa Male and Female First Names and Surnames
def generate_orissa_names(n, user_preference=None):

    # Orissa Male First Names
    odia_male_firstnames= [
        'Nagesh', 'Anirudh', 'Jagabandhu', 'Rameswar', 'Tejas', 'Abinash', 'Bhagirath', 'Balaram', 'Vikash', 'Rakesh', 'Saroj', 'Rohit', 
        'Madhusudan', 'Haran', 'Upendra', 'Kishore', 'Satyendra', 'Debasish', 'Puru', 'Alok', 'Sohit', 'Suresh', 'Amar', 'Shankar', 'Devendra', 
        'Sourabh', 'Laxmidhar', 'Uday', 'Pankaj', 'Gaurav', 'Raghupati', 'Prithvi', 'Yogesh', 'Rajat', 'Satyajit', 'Akhilesh', 'Sambit', 
        'Bikramjit', 'Shyam', 'Arvind', 'Subash', 'Suren', 'Sanjib', 'Kandarp', 'Bikash', 'Rajiv', 'Sarat', 'Rathindra', 'Chandresh', 'Banamali', 
        'Ananta', 'Debashish', 'Pranav', 'Vishwanath', 'Suman', 'Ranjan', 'Govind', 'Aaditya', 'Mukul','Tapan', 'Vikrant', 'Bijay', 'Vishal', 
        'Ratan', 'Subhendra', 'Niranjan', 'Nitin', 'Sudhir', 'Jaswant', 'Chiranjeeb', 'Prabhat', 'Bishnu', 'Siddhartha', 'Vineet', 'Dwarakanath', 
        'Pranab', 'Keshav', 'Prasanna', 'Chaitanya', 'Indrajit', 'Satyapratap', 'Harishankar', 'Abhishek', 'Ujjwal', 'Shubham', 'Debaraj', 
        'Saikat', 'Harish', 'Chandan', 'Durga', 'Jnanendra', 'Narayan', 'Sandeep', 'Sanjay', 'Ravi', 'Vishnu', 'Chittaranjan', 'Subhendu', 
        'Lalit', 'Sujit', 'Pratap', 'Giridhar', 'Jitendra', 'Deepak', 'Milan', 'Suraj', 'Kalyan', 'Prakash', 'Siddharth', 'Pradeep', 'Dinesh', 
        'Hari', 'Rajendra', 'Gopal', 'Sushanta', 'Tanmay', 'Vishnuprasad', 'Madhukar', 'Bikram', 'Ajit', 'Brahmananda', 'Dharma', 'Haribandhu', 
        'Vijay', 'Swarup', 'Anil', 'Dibakar', 'Prasanta', 'Jagadish', 'Ramesh', 'Chinmay', 'Hariprasad', 'Nirmal', 'Maitreya', 'Kamal', 
        'Jagannath', 'Ishwar', 'Tapas', 'Sourav', 'Pravin', 'Arup', 'Kanhu', 'Ashok', 'Bhanu', 'Narayana', 'Umesh', 'Subhajit', 'Raghunandan', 
        'Raghunath', 'Kedar', 'Ravindra', 'Krishna', 'Kiran', 'Subrata', 'Naveen', 'Achyut', 'Tushar', 'Bansidhar', 'Manoj', 'Manindra', 
        'Saswat', 'Laxman', 'Samir', 'Pabitra', 'Bipin', 'Sushil', 'Abhay', 'Sudarshan', 'Chandrakant', 'Gokul', 'Sudhanshu', 'Saurabh', 
        'Satyabrata', 'Debendra', 'Kailash', 'Utpal', 'Binod', 'Madhukanta', 'Arun', 'Amresh', 'Girish', 'Vidyadhar', 'Sahadev', 'Sabyasachi', 
        'Kamalakar', 'Narendra', 'Debabrata', 'Bhabani', 'Tapesh', 'Jasbir', 'Manish', 'Sushant', 'Chiranjeevi', 'Karan', 'Nirakar', 'Ranjit', 
        'Madhav', 'Kushal']
    odia_male_suffix = [
        '', '', '', '', '', '', '', '', '', '',"prasad", "nath", "ranjan", "chandra", "kumar", "deep", "mohan", "bhushan",
        "mani", "dutta", "babu", "das", "charan", "priya", "jeet", "sundar",
        "raj", "dev", "ashok", "chaitanya",'', '', '', '', '']
    # Orissa Male Surnames
    odia_male_surname= [
        "Patnaik", "Behera", "Pattnaik", "Sahoo", 'Sahu', "Rath", "Das", "Mohanty", "Tripathy", "Jena",
        "Nayak", "Samal", "Mishra", "Parida", "Pradhan", "Barik", "Hota", "Kumar", "Dasarathi",
        "Rana", "Dasgupta", "Choudhury", "Nanda", "Padhy", "Panigrahi", "Mohapatra", "Sethi",
        "Chakraborty", "Khalat", "Kohli", "Mishra", "Samantray", "Acharya", "Swain", "Dhal", 'Mallick ',
        "Bhoi", "Sahu", "Satpathy", "Tiwari", "Kant", "Jagtap", "Prusty", "Ghosh", "Patel", "Pati",
        "Sarnayat", "Madhusmita", "Rathore", "Mohant", "Dasarath", "Rai", "Baral"]
    # Orissa Female First Names
    odia_female_firstname = [
        'Satyasri', 'Shanta', 'Neelam', 'Chandana', 'Sonal', 'Aditi', 'Bharati', 'Diksha', 'Chhaya', 'Puja', 'Oindrila', 'Nisha', 
        'Swarnalata', 'Neelima', 'Saraswati', 'Binodini', 'Jaiwanti', 'Yamini', 'Durga', 'Yamuna', 'Tanvi', 'Debanshi', 'Girija', 
        'Dipti', 'Sanjana', 'Dipika', 'Kanchan', 'Kumari', 'Madhusmitha', 'Sangeeta', 'Ritu', 'Pallabi', 'Padmini', 'Sunita', 'Jaya', 
        'Namita', 'Garima', 'Yashoda', 'Vasudha', 'Shakuntala', 'Vishaka', 'Ujjwala', 'Swati', 'Aradhya', 'Kalyani', 'Tulika', 'Baisakhi', 
        'Shakti', 'Bishakha', 'Ganga', 'Kanak', 'Sampurna', 'Shubha', 'Nivriti', 'Durgati', 'Rajani', 'Satarupa', 'Nandini', 'Trupti', 'Swarna', 
        'Sita', 'Bhamini', 'Damini', 'Nitika', 'Shubhra', 'Ankita', 'Bishnupriya', 'Leena', 'Maya', 'Ruchi', 'Vibhuti', 'Esha', 'Prabhati', 
        'Hemanti', 'Manisha', 'Vishali', 'Komala', 'Kanika', 'Vidhatri', 'Oja', 'Aastha', 'Pallavi', 'Pranjali', 'Bimala', 'Rupa', 'Mansi', 
        'Kumud', 'Preeti', 'Sharmila', 'Shashi', 'Ratna', 'Sushma', 'Eka', 'Indrani', 'Tara', 'Himani', 'Rupali', 'Parama', 'Chandrika', 
        'Poonam', 'Lalita', 'Amita', 'Sakshi', 'Pratima', 'Sashwati', 'Debasmita', 'Sharanya', 'Chandini', 'Vijaya', 'Rashmi', 'Vandana', 
        'Jyoti', 'Ishita', 'Sakina', 'Maitri', 'Madhurima', 'Sashi', 'Priyanka', 'Kiranmayee', 'Brahmi', 'Sona', 'Kavita', 'Nandita', 'Sampada', 
        'Bina', 'Urmila', 'Krishna', 'Subhashini', 'Kasturi', 'Nayana', 'Tulasi', 'Bithika', 'Sarojini', 'Duryati', 'Palak', 'Sohini', 'Abanti', 
        'Parbati', 'Mrunalini', 'Kanti', 'Nabaja', 'Ranjana', 'Chhavi', 'Kalpana', 'Binapani', 'Gargee', 'Chaitali', 'Sweta', 'Chitrani', 
        'Vithika', 'Savitri', 'Shanti', 'Madhavi', 'Alpana', 'Komal', 'Kumudini', 'Vasanti', 'Suman', 'Sushmita', 'Rachana', 'Charulata', 
        'Manasi', 'Madhura', 'Jivika', 'Basantika', 'Nalini', 'Laxmi', 'Pragati', 'Usha', 'Shubhada', 'Niharika', 'Tarini', 'Tanuja', 
        'Nabaprabha', 'Sadhana', 'Malini', 'Mitali', 'Gunjan', 'Rina', 'Neha', 'Rama', 'Divya', 'Hema', 'Gita', 'Arpita', 'Trishna', 
        'Jaswanti', 'Subhalakshmi', 'Tanu', 'Parwati', 'Kavya', 'Sujata', 'Ananya', 'Sonali', 'Kamala', 'Manjari', 'Alaka', 'Madhusree', 
        'Ishani', 'Prerna', 'Rajashree', 'Seema', 'Shalini', 'Lipi', 'Gungun', 'Nirmala', 'Barsha', 'Vidya', 'Ritika', 'Madhuri', 'Padma', 
        'Bindiya', 'Sitarani', 'Pooja', 'Radhika', 'Sakhi', 'Subhra', 'Bipasha', 'Trisha', 'Sushila', 'Anjali', 'Indira']
    odia_female_surname =  [
        "Patnaik", "Behera", "Pattnaik", 'Sahu', "Sahoo",
        "Rath", "Das", "Mohanty", "Tripathy", "Jena", "Nayak",
        "Samal", "Mishra", "Parida", "Pradhan", "Barik", "Hota",
        "Kumar", "Dasarathi", "Rana", "Dasgupta", "Choudhury",
        "Nanda", "Padhy", "Panigrahi", "Mohapatra", "Sethi",
        "Chakraborty", "Khalat", "Kohli", "Mishra", "Samantray",
        "Acharya", "Swain", "Dhal", "Bhoi", "Sahu", "Satpathy",
        "Routray", "Tiwari", "Kant", "Jagtap", "Prusty", "Ghosh",
        "Patel", "Pati", "Sarnayat", "Madhusmita", "Rathore", "Mohant",
        "Dasarath", "Rai", "Baral"]
    odia_female_suffix= ['', '', '', '', '',"sundari", "priya", "lina", "shree", "devi", "rani", "bharti", "prabha",'', '', '', '', '']

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(odia_male_firstnames)
        suffix_male = random.choice(odia_male_suffix)
        last_name_male = random.choice(odia_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            if suffix_male:  # Adding suffix if exists
                name_male = first_name_male + " " + suffix_male + " " + last_name_male  # Full name with suffix
            else:
                name_male = first_name_male + " " + last_name_male  # Full name without suffix

        # Female Name Generation
        first_name_female = random.choice(odia_female_firstname)
        suffix_female = random.choice(odia_female_suffix)
        last_name_female = random.choice(odia_female_surname)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            if suffix_female:  # Adding suffix if exists
                name_female = first_name_female + " " + suffix_female + " " + last_name_female  # Full name with suffix
            else:
                name_female = first_name_female + " " + last_name_female  # Full name without suffix

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_orissa_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df