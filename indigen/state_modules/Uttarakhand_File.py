import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_uttarakhand_names(n, user_preference=None):

    # uttarakhand Male First name
    uttarakhand_male_firstname = [
        "Ajay", "Alok", "Amar", "Ambar", "Amrendra", "Anand", "Anandilal", "Anil", "Anirudh", "Anoop", "Archit", "Arjun",
        "Arvind", "Ashok", "Atmaram", "Atul", "Avinash", "Badri", "Baldev", "Balwan", "Banke", "Bhagat", "Bhairav",
        "Bharat", "Bhaskar", "Bheem", "Bhola", "Bhuwan", "Bihari", "Bijendra", "Brajesh", "Chaman", "Champak", "Chandra",
        "Chandramohan", "Charan", "Chaturbhuj", "Dalbir", "Damodar", "Daya", "Deendayal", "Deepak", "Dev",
        "Devanand", "Devendra", "Devesh", "Dharam", "Dharamvir", "Dharmesh", "Dhruv", "Dilip", "Dinesh", "Divakar",
        "Durgesh", "Dwarika", "Gagan", "Gajendra", "Ganesh", "Gaurav", "Ghanshyam", "Girendra", "Girish", "Gopichand",
        "Govind", "Govinda", "Gulab", "Guna", "Gyan", "Hansraj", "Harak", "Harendra", "Hari", "Haridutt", "Harilal",
        "Harimohan", "Harish", "Harivansh", "Hemant", "Hemraj", "Himanshu", "Indrajeet", "Ishwar", "Jagdish", "Jai",
        "Jaidev", "Jaipal", "Janak", "Jaspal", "Jaswant", "Jatin", "Jeevan", "Jitendra", "Jogendra", "Kailash", "Kalyan",
        "Kamal", "Kanak", "Kanhaiya", "Kanwal", "Karan", "Keshav", "Kewal", "Kishan", "Kishore", "Kripal", "Krishan",
        "Krishnakant", "Kuldeep", "Lajpat", "Lakhan", "Lakshya", "Laxman", "Madan", "Madhav", "Mahavir",
        "Mahendra", "Mahesh", "Mangal", "Manohar", "Manoharlal", "Manoj", "Mansingh", "Meghraj", "Mohan", "Moolchand",
        "Mukesh", "Mulkraj", "Murari", "Narayan", "Narendra", "Naresh", "Nareshpal", "Narsingh", "Navin", "Neeraj",
        "Nilesh", "Nirmal", "Nitin", "Omprakash", "Omveer", "Padam", "Pankaj", "Param", "Paramjeet", "Parashar",
        "Parmanand", "Pawan", "Phoolchand", "Pitambar", "Pradeep", "Prakash", "Pramod", "Pratap", "Prem", "Prithvi",
        "Punit", "Puran", "Purushottam", "Pushkar", "Raghav", "Raghu", "Raghunath", "Raghuraj", "Raghuvir", "Rajan",
        "Rajendra", "Rajesh", "Rajpal", "Rajveer", "Ramesh", "Randhir", "Ranjeet", "Ranveer", "Ratan", "Ravi",
        "Ravikant", "Ravindra", "Rishabh", "Rishikesh", "Ritesh", "Roopchand", "Rudra", "Sadanand", "Sahadev", "Sahil",
        "Sandeep", "Sanjay", "Santosh", "Satish", "Satyam", "Shailesh", "Shakti", "Shankar", "Sharad", "Sharvan",
        "Shashank", "Shekhar", "Shishupal", "Shobhit", "Shridhar", "Shyam", "Shyamveer", "Sidharth", "Sitaram", "Sohan",
        "Somesh", "Srikant", "Subodh", "Sudhir", "Sukumar", "Sumer", "Sunder", "Suraj", "Surender", "Suresh", "Surinder",
        "Surya", "Swaminath", "Swaroop", "Tejpal", "Trilochan", "Trilok", "Trivendra", "Uday", "Uddhav", "Udit", "Umesh",
        "Uttam", "Uttamchand", "Vachaspati", "Veer", "Vijay", "Vinay", "Vineet", "Virendra", "Vishal", "Vishnu",
        "Vishwanath", "Vyas", "Yogendra", "Yogesh", "Yudhisthir", "Zorawar"]


    # uttarakhand Male Surname
    uttarakhand_male_surname = [
        "Agrawal", "Ahuja", "Arya", "Bagat", "Baghel", "Bajpai", "Bali", "Balodi", "Bansal", "Barman", "Bedi",
        "Bhagat", "Bhandari", "Bharadwaj", "Bhardwaj", "Bhatt", "Bhattacharya", "Bhimwal", "Bhullar", "Chahal",
        "Chandra", "Chaturvedi", "Chaubey", "Chauhan", "Chaurasia", "Dagar", "Darbari", "Dhanraj", "Dhiman", "Dhingra",
        "Dhyani", "Dinesh", "Dobriyal", "Dubey", "Dvivedi", "Dwivedi", "Garg", "Gaur", "Gautam", "Goel", "Gosain", "Kumar",
        "Goswami", "Goyal", "Gupta", "Harit", "Jaswal", "Joshi", "Kamboj", "Kapoor", "Kashyap", "Kaul",
        "Kesarwani", "Khandelwal", "Khanna", "Khare", "Khatri", "Khurana", "Kothari", "Kotiyal", "Kulshreshtha",
        "Kunjwal", "Lal", "Lalit", "Lohia", "Malhotra", "Malviya", "Manral", "Mathur", "Matwal", "Mehra", "Mishra",
        "Mohan", "Nainwal", "Naithani", "Nath", "Nautiyal", "Negi", "Ojha", "Pande", "Pandey", "Pandit", "Pathak",
        "Patni", "Prasad", "Puri", "Purohit", "Purvi", "Raghunath", "Rajput", "Rastogi", "Rathi", "Raturi", "Rawat",
        "Sah", "Sahni", "Sahrawat", "Saini", "Saraswat", "Saxena", "Sehgal", "Sengar", "Shakti", "Shandilya", "Sharma",
        "Shekhar", "Shukla", "Singh", "Sisodia", "Soni", "Soniya", "Sood", "Talwar", "Tanwar", "Tiwari", "Tomar",
        "Tyagi", "Upadhyay", "Varma", "Verma", "Vishal", "Vishwakarma", "Vyas", "Yadav"]

    # uttarakhand Female First name
    uttarakhand_female_firstname = [
        "Aarti", "Abha", "Aditi", "Alka", "Amba", "Amrita", "Anamika", "Anjali", "Anju", "Annapurna", "Aparna",
        "Aradhana", "Arpita", "Asha", "Ashalata", "Ashwini", "Babita", "Bhagwati", "Bharti", "Bhavna", "Bhawna",
        "Bimla", "Bina", "Binita", "Champa", "Champavati", "Chanchal", "Chandani", "Chandralekha", "Charulata", "Chitra",
        "Damini", "Dayawati", "Deepa", "Deepali", "Devaki", "Devika", "Dhanalakshmi", "Dharma", "Dimple", "Dipshikha",
        "Dipti", "Durga", "Eesha", "Ganga", "Garima", "Gauri", "Gayatri", "Geeta", "Gitanjali", "Gulab", "Hansa",
        "Hemavati", "Hemlata", "Himalata", "Indira", "Indu", "Isha", "Ishwari", "Jaya", "Jayanti", "Jyoti", "Kalawati",
        "Kamala", "Kamini", "Kamlesh", "Kanaka", "Kanchan", "Kanika", "Kanti", "Karishma", "Karuna", "Kaushalya", "Kiran",
        "Kumari", "Kumkum", "Kusum", "Kusumlata", "Lakshmi", "Lalita", "Lata", "Leela", "Leelavati", "Leelawati", "Madhu",
        "Madhubala", "Madhulika", "Madhuri", "Maitreyi", "Malati", "Malika", "Mallika", "Malvika", "Mamta", "Mandakini",
        "Manju", "Manjula", "Manorama", "Meena", "Meera", "Mina", "Minakshi", "Mohini", "Mridula", "Mukeshwari", "Mukta",
        "Naina", "Namita", "Namrata", "Nanda", "Nandini", "Nandita", "Narayani", "Navina", "Niranjana", "Nirmala", "Nisha",
        "Nutan", "Padma", "Pallavi", "Pallavini", "Parul", "Parvati", "Pashupati", "Patralekha", "Phoolwati", "Poonam",
        "Prabha", "Prakashvati", "Pratibha", "Preeti", "Premalata", "Prerna", "Priti", "Priya", "Pushpa", "Pushpalata",
        "Radha", "Radhika", "Rajeshwari", "Rajini", "Rajni", "Rakhi", "Rama", "Ramola", "Reetika", "Rekha", "Rekhalata",
        "Renu", "Renuka", "Richa", "Rishika", "Ritu", "Rohini", "Roma", "Roshani", "Rudrani", "Rukmani", "Rupa",
        "Sadhna", "Sandhya", "Sangeeta", "Sanjana", "Santosh", "Sarita", "Saroja", "Sarojini", "Sati", "Savita",
        "Savitri", "Seema", "Shakuntala", "Shalini", "Shanti", "Sharmila", "Sheela", "Sheetal", "Shilpa", "Shivani",
        "Shobha", "Shobhana", "Shraddha", "Shradha", "Shubhra", "Shweta", "Simran", "Smita", "Sneha", "Snehlata",
        "Sohni", "Sona", "Sonal", "Subhadra", "Suhasini", "Suman", "Sumati", "Sunanda", "Sunita", "Supriya", "Surekha",
        "Surya", "Sushila", "Sushmita", "Suvarna", "Swarnalata", "Swati", "Tara", "Tejaswini", "Tilakvati", "Tilottama",
        "Tripti", "Tripurasundari", "Triveni", "Trupti", "Tulika", "Tulsi", "Urja", "Urmila", "Usha", "Uttara",
        "Vaidehi", "Vanamala", "Vandana", "Varsha", "Vasundhara", "Vibha", "Vibhuti", "Vidhya", "Vidya", "Vidyawati",
        "Vijaya", "Vimaladevi", "Vimla", "Vimukta", "Vimuktavati", "Vina", "Vinita", "Vishakha", "Vishnupriya",
        "Yashasvini", "Yashoda", "Yogini", "Yogita", "Zeenat"]


    # uttarakhand Female Surname
    uttarakhand_female_surname = [
        "Agrawal", "Ahuja", "Arya", "Bagat", "Baghel", "Bajpai", "Bali", "Balodi", "Bansal", "Barman", "Bedi",
        "Bhagat", "Bhandari", "Bharadwaj", "Bhardwaj", "Bhatt", "Bhattacharya", "Bhimwal", "Bhullar", "Chahal",
        "Chandra", "Chaturvedi", "Chaubey", "Chauhan", "Chaurasia", "Dagar", "Darbari", "Dhanraj", "Dhiman", "Dhingra",
        "Dhyani", "Dinesh", "Dobriyal", "Dubey", "Dvivedi", "Dwivedi", "Garg", "Gaur", "Gautam", "Goel", "Gosain",
        "Goswami", "Goyal", "Gupta", "Harit", "Jaswal", "Joshi", "Kamboj", "Kapoor", "Kashyap", "Kaul", "Kaur", "Kumari"
        "Kesarwani", "Khandelwal", "Khanna", "Khare", "Khatri", "Khurana", "Kothari", "Kotiyal", "Kulshreshtha",
        "Kunjwal", "Lal", "Lalit", "Lohia", "Malhotra", "Malviya", "Manral", "Mathur", "Matwal", "Mehra", "Mishra",
        "Mohan", "Nainwal", "Naithani", "Nath", "Nautiyal", "Negi", "Ojha", "Pande", "Pandey", "Pandit", "Pathak",
        "Patni", "Prasad", "Puri", "Purohit", "Purvi", "Raghunath", "Rajput", "Rastogi", "Rathi", "Raturi", "Rawat",
        "Sah", "Sahni", "Sahrawat", "Saini", "Saraswat", "Saxena", "Sehgal", "Sengar", "Shakti", "Shandilya", "Sharma",
        "Shekhar", "Shukla", "Devi", "Sisodia", "Soni", "Soniya", "Sood", "Talwar", "Tanwar", "Tiwari", "Tomar",
        "Tyagi", "Upadhyay", "Varma", "Verma", "Vishal", "Vishwakarma", "Vyas", "Yadav"]
     # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(uttarakhand_male_firstname)
        last_name_male = random.choice(uttarakhand_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(uttarakhand_female_firstname)
        last_name_female = random.choice(uttarakhand_female_surname)

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
    file_path = 'generated_uttarakhand_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df