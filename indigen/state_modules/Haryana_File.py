import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# haryana Male and Female First Names and Surnames
def generate_haryana_names(n, user_preference=None):
    haryana_male_firstnames = [
        "Amit", "Rakesh", "Suresh", "Sunil", "Rajesh", "Mahesh", "Ravinder", "Joginder", "Satish", "Ramesh",
        "Sandeep", "Pardeep", "Virender", "Karan", "Vikram", "Deepak", "Anil", "Narender", "Rohit", "Kuldeep",
        "Arvind", "Vijay", "Baljeet", "Jaideep", "Rajbir", "Manoj", "Devender", "Yashpal", "Krishan", "Naresh",
        "Bhupender", "Dinesh", "Harinder", "Surender", "Parveen", "Akhil", "Subhash", "Mukesh", "Ashok", "Ramphal",
        "Gaurav", "Kunal", "Ajit", "Balwant", "Chander", "Dalbir", "Devendra", "Gajendra", "Harbhajan", "Inderjit", 
        "Jitendra", "Karamveer", "Laxman", "Mahender", "Narendra", "Omprakash", "Pardeep", "Rajender", 
        "Satyendra", "Tejpal", "Umed", "Virender","Aditya", "Bhanu", "Chinmay", "Dhananjay", "Eshwar", "Gopal", "Hari", "Indra", "Keshav", 
        "Lakshman", "Madhav", "Narayan", "Omkar", "Pranav", "Raghav", "Sanket", "Sudhir", "Vishal", 
        "Yash", "Yogendra","Amit", "Arun", "Brijesh", "Chetan", "Devansh", "Gautam", "Hemant", "Ishan", "Kartik", 
        "Manish", "Neeraj", "Nikhil", "Piyush", "Rajat", "Rakesh", "Saurabh", "Suresh", "Uday", 
        "Vaibhav", "Vivek","Arjun", "Bhupendra", "Chirag", "Dushyant", "Girish", "Hemendra", "Jaidev", "Kuber", "Lokesh", 
        "Mahavir", "Niranjan", "Prithvi", "Ranbir", "Ranjeet", "Ratan", "Shivendra", "Suryaprakash", 
        "Tejas", "Ujjwal", "Vikram", "Arvind", "Bhagirath", "Chandrapal", "Dinesh", "Govind", "Harish", "Ishwar", "Karan", "Mahendra", 
        "Mukesh", "Naresh", "Prakash", "Rajesh", "Ramesh", "Sanjay", "Sharad", "Sunil", "Tulsiram", 
        "Vikas", "Vijay","Amar", "Bhupender", "Chandra", "Dharmendra", "Ganesh", "Hardeep", "Inderpal", "Jagdish", 
        "Kailash", "Lalit", "Mohan", "Naveen", "Nishant", "Rajiv", "Ravindra", "Satendra", "Shankar", 
        "Somesh", "Tarun", "Yatindra","Ashok", "Bharat", "Chetan", "Deenbandhu", "Eklavya", "Gajanan", "Hariprasad", "Jagannath", 
        "Kamal", "Loknath", "Madhukar", "Niraj", "Om", "Prabhakar", "Ravishankar", "Satish", "Shivam", 
        "Sukhdev", "Upendra", "Yashwant","Akhil", "Bhavesh", "Charan", "Dev", "Gopal", "Harendra", "Jaideep", "Kartikeya", "Madhav", 
        "Navin", "Nitin", "Rohit", "Shivraj", "Surendra", "Tejinder", "Umesh", "Vardhan", "Vimal", 
        "Yuvraj", "Zorawar","Amritpal", "Balraj", "Charanjit", "Daljit", "Gurdeep", "Harjinder", "Inderjeet", "Joginder", 
        "Karamjit", "Manjeet", "Nirmal", "Parminder", "Rajveer", "Ranvir", "Sarbjit", "Surjit", 
        "Tejinder", "Upkar", "Varinder", "Yadvinder","Arshdeep", "Bhupinder", "Dilpreet", "Gurjot", "Harpreet", "Inderjit", "Jaspreet", "Kamaljeet", 
        "Manpreet", "Nirbhay", "Prabhjot", "Ravinder", "Sandeep", "Simranjit", "Taranjit", "Udaybir", 
        "Vikramjit", "Yashpreet", "Zorawar", "Himmat","Amardeep", "Bhupinder", "Charanjit", "Darshan", "Gurdas", "Harmeet", "Indrajit", "Jagdish", 
        "Kuldeep", "Maninder", "Nirmaljit", "Parminder", "Rajbir", "Ravinder", "Sarbjit", "Tejinder", 
        "Upender", "Vijender", "Yadwinder", "Zorawar"
    ]
    haryana_male_surnames = [
        'Singh', "Yadav", "Malik", "Dahiya", "Hooda", "Sangwan", "Chauhan", "Sheoran", "Dalal", "Rathi", "Punia",
        "Deswal", "Dhankar", "Ahlawat", "Rana", "Beniwal", "Sihag", "Sehrawat","Phogat","Khatri", "Gulia", "Kundu", "Jakhar",
        "Sindhu", "Tanwar","Lamba", "Balyan", "Pundir", "Goyat", "Mor","Kashyap", "Sharma", "Kaushik", "Tewatia", "Nehra",
        "Chaudhary", "Rathi", "Pundir", "Kadian", "Sihag", "Dahiya", "Ahlawat",
        "Chhillar", "Bainsla", "Jangra", "Sangwan", "Dalal", "Rana", "Nangia", "Lather", "Tanwar", 
        "Sheoran", "Kadian","Sharma", "Pandey", "Tiwari", "Chaturvedi", "Dubey", "Bhatt", "Vyas", "Joshi", "Saraswat", 
        "Pathak", "Awasthi", "Bhatnagar", "Upadhyay", "Misra", "Rastogi", "Pratap", "Purohit", 
        "Vishwakarma", "Tripathi","Agarwal", "Oswal", "Khandelwal", "Seth", "Goel", "Mittal", "Garg", "Bansal", "Chawla", 
        "Khanna", "Gupta", "Jain", "Soni", "Poddar", "Maheshwari", "Bhatia", "Taneja", "Jindal", 
        "Agarwalia","Rathore", "Chauhan", "Solanki", "Chandrawat", "Sisodia", "Pundir", "Kachhawaha", "Rajawat", 
        "Shekhawat", "Sengar", "Yadav", "Jadon", "Tanwar", "Chandela", "Baghel", "Singh", "Bhomia", 
        "Swarup", "Thakur", "Kumar","Yadav", "Ahir", "Gaharwar", "Chaudhary", "Shukla", "Nishad", "Dewal", "Kumar", "Sahu", 
        "Maurya", "Bais", "Tanwar", "Gupta", "Kachhap", "Mishra", "Rathi", "Kewat", "Mandal", 
        "Sharma","Gurjar", "Bishnoi", "Kadian", "Tanwar", "Choudhary", "Dahiya", "Lather", "Ranawat", 
        "Bhardwaj", "Rana", "Sheoran", "Shekhawat", "Jangid", "Sangwan", "Kadian", "Chalawat", 
        "Chandrawat", "Raghav", "Jat","Chamaar", "Valmiki", "Mala", "Ravidas", "Dhanuk", "Chamar", "Madhesi", "Bhangi", "Mushar", 
        "Ram", "Mehta", "Lodh", "Hirpara", "Mewara", "Dholia", "Sadh", "Paswan", "Mahato", "Teli", 
        "Gorkha", "Saini", "Khajuria", "Rana", "Rathore", "Madhia", "Bansa", "Mishra", 
        "Bhushan", "Sani", "Poonia", "Chandawat", "Vyas", "Gusain", "Chand", "Parmar", "Raghav", 
        "Kachori", "Bisht","Sohal", "Sidhu", "Grewal", "Dhillon", "Gill", "Khalra", "Saini", "Sandhu", "Pall", 
        "Singh", "Chahal", "Bains", "Jassa", "Chandok", "Hayer", "Rai", "Bhullar", "Kooner", "Dhindsa", 
        "Bedi","Ramgarhia", "Gill", "Sohi", "Khosa", "Khangura", "Chana", "Chawla", "Mann", "Sangha", 
        "Sekhon", "Jaswal", "Pannun", "Brar", "Guraya", "Mann", "Khumaran", "Bal", "Dhot", "Khalid", 
        "Rattan","Khatri", "Chopra", "Malhotra", "Kapoor", "Mehra", "Bedi", "Sachdeva", "Khurana", "Singh", 
        "Gupta", "Chawla", "Mahajan", "Gulati", "Aggarwal", "Taneja", "Arora", "Bansal", "Kalra", 
        "Tiwari", "Khera"
    ]


    haryana_female_firstnames = [
        'Juhi', 'Sakshi', 'Manisha', 'Babita', 'Komal','Renuka', 'Manu', 'Anita', 'Suman', 'Sunita', 
        'Poonam', 'Seema', 'Rekha', 'Kamlesh', 'Meena', 'Manju', 'Sarita', 'Geeta', 'Sushma', 
        'Anjali', 'Ritu', 'Kavita', 'Nisha','Veena', 'Mamta', 'Neelam', 'Shobha',
        'Jyoti', 'Rakhi', 'Mona', 'Shalini','Deepika', 'Pushpa', 'Kiran', 'Radha',
        'Rajni', 'Asha', 'Bimla', 'Laxmi', 'Indira', 'Priyanka','Savita','Nirmala'    # Jat Names
        "Aarti", "Baljeet", "Chandni", "Daljeet", "Devika", "Harpreet", "Indu", "Jaspreet", "Karamjeet", 
        "Komal", "Lajwanti", "Manju", "Nirmal", "Pooja", "Rajni", "Suman", "Tejinder", "Urmila", "Vandana", 
        "Yamuna","Aishwarya", "Bhavya", "Chandana", "Disha", "Esha", "Gauri", "Indira", "Kavita", "Lakshmi", 
        "Manju", "Nandini", "Priya", "Radhika", "Saraswati", "Shashi", "Swati", "Vandita", "Yashoda", 
        "Vishakha", "Yogita","Agarwali", "Alka", "Anju", "Chandni", "Gita", "Kiran", "Lalita", "Meera", "Nisha", 
        "Pooja", "Rani", "Sushma", "Vandana", "Vasundhara", "Aarti", "Asha", "Bindiya", "Devika", 
        "Kajal", "Ranjana","Annapurna", "Bhavna", "Chandrakanta", "Devi", "Gajra", "Indira", "Kanchan", "Madhuri", 
        "Rajeshwari", "Rani", "Saraswati", "Shakuntala", "Vimla", "Vidya", "Vishakha", "Yashoda", 
        "Ravina", "Meenakshi", "Shubhangi", "Kumari","Aarti", "Chandrika", "Geeta", "Harita", "Kavita", "Leela", "Madhuri", "Nalini", "Nandita", 
        "Prabha", "Ravina", "Rina", "Shanti", "Simran", "Sujata", "Suman", "Sushma", "Tanuja", 
        "Vasundhara", "Yamini","Aditi", "Bhavna", "Chandana", "Deepti", "Gauri", "Harika", "Indu", "Jaya", "Kajal", 
        "Laxmi", "Madhavi", "Nisha", "Radhika", "Saraswati", "Shakuntala", "Shanti", "Simran", 
        "Suman", "Tanvi", "Vandana","Alka", "Babli", "Chandini", "Disha", "Gurpreet", "Jaspreet", "Kiran", "Lajwanti", "Meenakshi", 
        "Nidhi", "Poonam", "Rakhi", "Sharmila", "Suman", "Sushila", "Urmila", "Vandana", "Vasudha", 
        "Vidya", "Shakuntala", "Aaradhya", "Aarti", "Deepika", "Harita", "Jaswinder", "Komal", "Kriti", "Madhavi", "Meera", 
        "Nandini", "Neelam", "Pooja", "Rani", "Simran", "Suman", "Tanuja", "Yashika", "Asha", "Sunita", 
        "Sushma", "Amritpal", "Charanjit", "Daljeet", "Harpreet", "Jasleen", "Karamjit", "Mandeep", "Navdeep", 
        "Parminder", "Ravinder", "Simranjeet", "Sukhpreet", "Tejinder", "Upkar", "Varinder", "Yoginder", 
        "Zorawar", "Harman", "Bikramjit", "Inderjeet","Amarjit", "Charanjit", "Daljeet", "Harjit", "Jatinder", "Karamjit", "Mandeep", "Navneet", 
        "Prabhjot", "Rajpreet", "Simran", "Surinder", "Tejinder", "Varinder", "Zorawar", "Harman", 
        "Vikramjit", "Yuvraj", "Jaspreet", "Parminder","Amrit", "Charanjit", "Daljit", "Harjeet", "Inderjit", "Jasvinder", "Kuldeep", "Mandeep", 
        "Parminder", "Ravinder", "Simranjeet", "Surjit", "Tejinder", "Upkar", "Vikram", "Yadwinder", 
        "Aman", "Jagdeep", "Narinder", "Satinder"]


    haryana_female_surnames = [
        'Kaur', 'Devi', 'Rani', 'Kumari', 'Chawla', 'Choudhary','Sharma',
        "Yadav", "Malik", "Dahiya", "Hooda", "Sangwan", "Chauhan", "Sheoran", "Dalal", "Rathi", "Punia",
        "Deswal", "Dhankar", "Ahlawat", "Rana", "Beniwal", "Sihag", "Sehrawat", "Bura",
        "Phogat", "Tanwar",  "Chhillar", "Bainsla", "Jangra", "Sangwan", "Dalal", "Rana", "Nangia", "Lather", "Tanwar", 
        "Sheoran", "Kadian","Sharma", "Pandey", "Tiwari", "Chaturvedi", "Dubey", "Bhatt", "Vyas", "Joshi", "Saraswat", 
        "Pathak", "Awasthi", "Bhatnagar", "Upadhyay", "Misra", "Rastogi", "Pratap", "Purohit", 
        "Vishwakarma", "Tripathi","Agarwal", "Oswal", "Khandelwal", "Seth", "Goel", "Mittal", "Garg", "Bansal", "Chawla", 
        "Khanna", "Gupta", "Jain", "Soni", "Poddar", "Maheshwari", "Bhatia", "Taneja", "Jindal", 
        "Agarwalia","Rathore", "Chauhan", "Solanki", "Chandrawat", "Sisodia", "Pundir", "Kachhawaha", "Rajawat", 
        "Shekhawat", "Sengar", "Yadav", "Jadon", "Tanwar", "Chandela", "Baghel","Bhomia", 
        "Swarup", "Thakur", "Kumar","Yadav", "Ahir", "Gaharwar", "Chaudhary", "Shukla", "Nishad", "Dewal", "Kumar", "Sahu", 
        "Maurya", "Bais", "Tanwar", "Gupta", "Kachhap", "Mishra", "Rathi", "Kewat", "Singh", "Mandal", 
        "Sharma","Gurjar", "Bishnoi", "Kadian", "Tanwar", "Choudhary", "Dahiya", "Lather", "Ranawat", 
        "Bhardwaj", "Rana", "Singh", "Sheoran", "Shekhawat", "Jangid", "Sangwan", "Kadian", "Chalawat", 
        "Chandrawat", "Raghav", "Jat","Chamaar", "Valmiki", "Mala", "Ravidas", "Dhanuk", "Chamar", "Madhesi", "Bhangi", "Mushar", 
        "Ram", "Mehta", "Lodh", "Hirpara", "Mewara", "Dholia", "Sadh", "Paswan", "Mahato", "Teli", 
        "Gorkha", "Saini", "Khajuria", "Rana", "Rathore", "Madhia", "Bansa", "Mishra", 
        "Bhushan", "Sani", "Poonia", "Chandawat", "Vyas", "Gusain", "Chand", "Parmar", "Raghav", 
        "Kachori", "Bisht","Sohal", "Sidhu", "Grewal", "Dhillon", "Gill", "Khalra", "Saini", "Sandhu", "Pall", 
        "Chahal", "Bains", "Jassa", "Chandok", "Hayer", "Rai", "Bhullar", "Kooner", "Dhindsa", 
        "Bedi","Ramgarhia", "Gill", "Sohi", "Khosa", "Khangura", "Chana", "Chawla", "Mann", "Sangha", 
        "Sekhon", "Jaswal", "Pannun", "Brar", "Guraya", "Mann", "Khumaran", "Bal", "Dhot", "Khalid", 
        "Rattan","Khatri", "Chopra", "Malhotra", "Kapoor", "Mehra", "Bedi", "Sachdeva", "Khurana", 
        "Gupta", "Chawla", "Mahajan", "Gulati", "Aggarwal", "Taneja", "Arora", "Bansal", "Kalra", 
        "Tiwari", "Khera"
    ]

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(haryana_male_firstnames)
        last_name_male = random.choice(haryana_male_surnames)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(haryana_female_firstnames)
        last_name_female = random.choice(haryana_female_surnames)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female  # Full name

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_haryana_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df