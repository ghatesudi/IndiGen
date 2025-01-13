import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# maharashtra Male and Female First Names and Surnames
def generate_maharashtra_names(n, user_preference=None):
    # maharashtra Male First Names
    maharashtra_male_firstname= [
        'Baban', 'Aniruddha', 'Ramesh', 'Nandlal', 'Prajwal', 'Vinayak', 'Bhausaheb', 'Vikram', 'Kamran', 'Anup', 'Nand', 
        'Siddharth', 'Jagadish', 'Digambar', 'Baiju', 'Mitesh', 'Hemendra', 'Kunal', 'Shubham', 'Rajesh', 'Girish', 'Deven', 
        'Gopal', 'Gaurish', 'Jagdish', 'Hemraj', 'Manoj', 'Govind', 'Eknath', 'Brijesh', 'Yash', 'Ganesh', 'Aadesh', 'Pradeep', 
        'Kishore', 'Rajiv', 'Sitaram', 'Bharat', 'Chandramohan', 'Jitendra', 'Rupesh', 'Mukul', 'Gajanan', 'Nayan', 'Shamrao', 
        'Shantanu', 'Vikrant', 'Avinash', 'Prakash', 'Ganeshwar', 'Ujjwal', 'Mangesh', 'Yogesh', 'Digvijay', 'Sushil', 'Parag', 
        'Niranjan', 'Rohit', 'Harish', 'Chandresh', 'Satyendra', 'Santosh', 'Chirag', 'Krishnakant', 'Piyush', 'Bhaskar', 'Shivram', 
        'Vibhav', 'Vatsal', 'Jagannath', 'Omkar', 'Lokesh', 'Vishwajeet', 'Vikash', 'Subhash', 'Sandeep', 'Kailash', 'Siddhesh', 
        'Dattaram', 'Shankar', 'Ganpat', 'Raghav', 'Devendra', 'Gaurav', 'Mahesh', 'Vasudev', 'Nirav', 'Prashant', 'Vishwanath', 
        'Atmaram', 'Chetan', 'Bhushan', 'Pritam', 'Manish', 'Vishwas', 'Ranjan', 'Krishna', 'Rajendra', 'Laxman', 'Deepak', 'Jeevan', 
        'Dattatray', 'Harinarayan', 'Suraj', 'Arvind', 'Gajendra', 'Pravin', 'Umesh', 'Raghunath', 'Ketan', 'Chandrakant', 'Nandkishore', 
        'Mithun', 'Naveen', 'Yashwanth', 'Harishchandra', 'Pranav', 'Dinesh', 'Vivek', 'Hemant', 'Vishal', 'Lalit', 'Madhusudhan', 'Kamlesh', 
        'Jayant', 'Madhusudan', 'Javed', 'Mahadev', 'Ashok', 'Aditya', 'Suresh', 'Ravindra', 'Sushant', 'Ajay', 'Narayan', 'Shyam', 'Pankaj', 
        'Vasant', 'Tanay', 'Abhijeet', 'Rameshwar', 'Harsh', 'Uday', 'Ajit', 'Makarand', 'Ashwin', 'Mohan', 'Shivendra', 'Karan', 'Madhav', 
        'Bhavesh', 'Dattaguru', 'Kailas', 'Nikhil', 'Ishwar', 'Alok', 'Prabhakar', 'Anil', 'Priti', 'Amit', 'Rajeev', 'Raghvendra', 'Kalpesh', 
        'Shivaji', 'Keshav', 'Chinmay', 'Vinod', 'Nilesh', 'Anand', 'Tejas', 'Niraj', 'Tanmay', 'Ranjit', 'Nitin', 'Sagar', 'Tushar',
        "Narahari", "Vitthal", "Pandurang", "Pandharinath", "Eknath", "Shreepad", "Tukaram","Tanaji", "Madhukar", "Martand", "Datta",
        "Dattatrey", "Bhausaheb", "Tätoji", "Tatya","Shivaji", "Dattu", "Bajirao", "Malharao", "Vaman", "Chhagan", "Baghoji", "Bhujang",
    "Gyaneshwar", "Mangesh", "Moropant", "Triyambak", "Namdeo", "Moreshwar", "Gyandeo","Bhikhu", "Dataji", "Balasaheb", "Kondiba",
        "Jiwaji", "Dattopant", "Sadashiva", "Vinayak", "Gajanan", "Gadadhar", "Bal Gangadhar"]
    
        # maharashtra Male Suffix
    maharashtra_male_suffix= [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "bhau", 'saheb']

    suffix_to_prefix_male = {
    "ji": ["Shiva", "Shambha", "Ragho", "Vagho", "Chama", "ba", "Bhikha", "Jago", "Tana",
        "Nana", "aba", "Baya", "Tato", "Kano", "Bala", "Rano", "Janako", "Rambha", "Vitho",
        "Samba", "Jiva"],
    "rao": ["Balavant", "Yashvant", "Vasant", "Martand", "Chimman", "Babu", "Shesh", "Bhim", 
        "Baji", "Vinayak", "Venkata", "Vaman", "Khande", "Shivaji", "Baban", "Appă", "Vilas"
    ],
    "bhau": ["Hari", "Kusha", "Bala", "Raja"],
    "bhai": ["Keshu", "Vitthal", "Ballabh", "Dheerü"],
    "ba": ["Tatya", "Dhondi", "Kondo", "Betho", "Balo", "Dado", "Nago", "Vithoba", "Baghoba"],
    "saheb": ["Bala", "Nana", "Apa", "Anna", "Kaka", "Bhau", "Datta"],
    "bapu": ["Sakharam", "Banya"],
    "nath": ["Shri", "Kashi", "Ek", "Pandhari"]}
    
    # maharashtra Female First Names
    
    maharashtra_female_firstname = [
        'Vishakha', 'Meenal', 'Deepali', 'Sarika', 'Meena', 'Kalpana', 'Yashoda', 'Sushmita', 'Aparna', 'Bhavana', 
        'Jeevitha', 'Rashmi', 'Shashwati', 'Aruna', 'Anjali', 'Lalita', 'Kamala', 'Snehal', 'Gauri', 'Sanya', 'Swarali', 
        'Swara', 'Rupa', 'Ishwari', 'Hema', 'Swati', 'Vishaka', 'Esha', 'Priya', 'Disha', 'Gulzar', 'Smita', 'Radhika', 
        'Lajwanti', 'Jeevan', 'Ravi', 'Gaurika', 'Tanuja', 'Anuja', 'Vaidehi', 'Tanvi', 'Kshama', 'Sushita', 'Anita', 
        'Bhumika', 'Bhoomi', 'Vandana', 'Amruta', 'Deepa', 'Priti', 'Ragini', 'Manjiri', 'Garima', 'Nidhi', 'Rajani', 
        'Yamuna', 'Shubhra', 'Vibhuti', 'Aishwarya', 'Kavita', 'Madhuri', 'Tejaswini', 'Tejal', 'Karuna', 'Aakansha', 
        'Shubhangi', 'Rima', 'Yamita', 'Yashasvi', 'Minal', 'Vimala', 'Suman', 'Chandrika', 'Krupa', 'Devika', 'Hemanti', 
        'Brahmi', 'Pooja', 'Chitra', 'Geeta', 'Kumud', 'Anvita', 'Indira', 'Kanchan', 'Ira', 'Nalini', 'Tripti', 'Kiran', 
        'Chhavi', 'Dattika', 'Pradnya', 'Yamini', 'Shital', 'Sharmila', 'Niranjana', 'Kishori', 'Divya', 'Krishna', 
        'Sadhana', 'Shanaya', 'Nayan', 'Nutan', 'Pragati', 'Rohini', 'Ashwini', 'Latika', 'Madhushree', 'Leela', 'Charulata', 
        'Vanshika', 'Chandini', 'Sonal', 'Yashika', 'Archita', 'Kumudini', 'Niharika', 'Vibha', 'Jagriti', 'Vasundhara', 
        'Ishika', 'Shruti', 'Bhakti', 'Nisha', 'Alka', 'Dina', 'Vidya', 'Bharti', 'Laxmi', 'Sharanya', 'Sangeeta', 'Manisha', 
        'Chhaya', 'Yogita', 'Siddhi', 'Nandita', 'Sumati', 'Tanu', 'Jivika', 'Akhila', 'Gargee', 'Vaishali', 'Usha', 'Durga', 
        'Soni', 'Ekta', 'Sushila', 'Diksha', 'Avni', 'Damayanti', 'Ananya', 'Kriti', 'Vrinda', 'Neelima', 'Rajini', 'Nandini', 
        'Jayashree', 'Anvi', 'Ishita', 'Sushma', 'Urmila', 'Tanya', 'Aarti', 'Jyoti', 'Shaila', 'Neelam', 'Chandana', 'Jaya', 
        'Isha', 'Madhavi', 'Kavitha', 'Kavya', 'Bhargavi', 'Chaitali', 'Savitri', 'Pallavi', 'Gulsher', 'Sakshi', 'Kamini', 
        'Nikita', 'Ranjana', 'Gargi', 'Shalini', 'Shubha', 'Gulab', 'Sujata', 'Poonam', 'Ganga', 'Gulika', 'Trupti', 'Damini', 
        'Chandani', 'Manju', 'Akanksha', 'Archana', 'Anushka',"Shalini", "Vaishali", "Subhalaxmi", "Bhagyashree", "Sugandha", 
        "Sumitra", "Surekha", "Sumedha", "Juthika", "Priyanka", "Asha", "Usha", "Nisha","Pooja", "Divya", "Vanamala", "Sonalī",
        "Saroja", "Pupul", "Prabha", "Sarojini","Shubhangi", "Mriņalini", "Padmja", "Sunanda", "Indira", "Ujjwala", "Medha",
        "Ruchira", "Suhasini", "Rohini", "Madhavi", "Chitra", "Shilpa", "Jyotsna", "Latika","Mridula", "Godavari", "Bhagirathi",
        "Mukta", "Savithry", "Savitha", "Saraswathy","Laxmi", "Shri", "Uma", "Parvathy", "Sharada", "Durga", "Mandakini"]
    
    maharashtra_female_suffix = [ " ", " ", " ", " ", " ", " ", " ", "bai", "tai" ]

    suffix_to_prefix_female = {
    "bai": ["Ashlya", "Laxmi", "Tija", "Khasu", "Tandu", "Sona", "Gangü", "Vithabai"],
    "tai": ["Usha", "Meena"],"ai": ["Vitt", "Rakham"],
    "devi": ["Padma", "Rama", "Vijaya"],
    "rani": ["Mitha", "Devika"],"akka": ["Kam", "Lia"],
    "raje": ["Padma", "Vasundhara", "Vijaya", "Anuradha", "Usha", "Yashodhara"]}
    
    maharashtra_surname = [
        "Adkar", "Agarkar", "Ambedkar", "Anand", "Apte", "Babar", "Bansode", "Bapat", "Bhave", "Bhagat",
        "Bhavsar", "Bhardwaj", "Bodke", "Chandekar", "Chandran", "Chavan", "Chitre", "Dandekar", "Deshmukh", 
        "Deshpande", "Dhumal", "Dixit", "Dnyandev", "Gadgil", "Gajanan", "Gaitonde", "Gandhi", "Garge",
        "Gawali", "Gholap", "Gokhale", "Gondhalekar", "Haware", "Holkar", "Jadhav", "Jadhavrao", "Jadhaw",
        "Jain", "Jadhav", "Joshi", "Kadam", "Kale", "Kambli", "Khandekar", "Kharche", "Khot", "Kumbhar", 
        "Kulkarni", "Lad", "Lohar", "Madhav", "Mahadik", "Mahajan", "Mankar", "Mhatre", "Mhaske", "Mokashi", 
        "Nadkarni", "Nandedkar", "Nargund", "Nath", "Nene", "Pakhale", "Pande", "Patil", "Phadke", "Pimple",
        "Pote", "Rane", "Ravindra", "Rathod", "Sawant", "Shah", "Shinde", "Shirke", "Shukla", "Sonawane",
        "Tambe", "Tayade", "Tiwari", "Tulpule", "Vaidya", "Valvi", "Vangale", "Vasudev", "Wagh", "Wankhede", 
        "Wani", "Yadav", "Zade", "Zambare", "Vichare", "Dhamangaonkar", "Desai", "Bhanushali", "Borkar", 
        "Bajpai", "Bhagat", "Chandran", "Chore", "Chudamani", "Dabhade", "Dhole", "Gokul", "Gondhale", "Jadhav",
        "Jadhavrao", "Jangid", "Joshi", "Kanak", "Kattale", "Khan", "Kolhe", "Kharche", "Khanvilkar", "Khatri", 
        "Khandekar", "Kulkarni", "Lad", "Lohar", "Mahadeo", "Manerkar", "Mane", "Marathe", "Mehta", "Modi", 
        "Nandekar", "Naik", "Narvekar", "Patankar", "Pingle", "Pooja", "Rane", "Rathod", "Sawant", "Suryavanshi",
        "Shrikant", "Shinde", "Shinde", "Suryawanshi", "Soman", "Sohoni", "Sonawane", "Tambay", "Tambe", "Tiwari",
        "Tulpule", "Vaidya", "Vijay", "Vishwakarma", "Vishwanath", "Vishwajeet", "Wani", "Wagh", "Zanje", 
        "Zende", "Zalki", "Zarde", "Sarkar", "Sutar", "Patil", "Jadhav", "Jadhaw", "Sawant", "Vaz", "More", 
        "Gajra", "Gadgil", "Kulkarni", "Rao", "Ranade", "Shikare", "Kulkarni", "Kale", "Kumbhar", "Wadkar"]
        # Initialize user preferences
    preferences = init(user_preference)
    # Create a list to store names and their genders
    names = []
    # Generate names
    for i in range(n // 2):  # Generate half male and half female names

        male_name_type = random.choice(["simple", "combination"])

        if male_name_type == "simple":
            # Male Name Generation
            first_name_male = random.choice(maharashtra_male_firstname)
            suffix_male = random.choice(maharashtra_male_suffix)
            last_name_male = random.choice(maharashtra_surname)
            name_male_first = first_name_male + suffix_male + " " + last_name_male
            name_male_first2 = None
        elif male_name_type == "combination":
            suffix_male2 = random.choice(list(suffix_to_prefix_male.keys()))
            prefix_male2 = random.choice(suffix_to_prefix_male[suffix_male2])
            first_name_male2 = prefix_male2
            last_name_male = random.choice(maharashtra_surname)
            name_male_first2 = first_name_male2 + suffix_male2.lower() + " " + last_name_male
            name_male_first = None
            
        if preferences.get('name_type') == 'first':
            name_male = first_name_male + suffix_male  # Only first name + suffix
        else:
            # Use whichever name is not None
            if name_male_first is not None:
                name_male = name_male_first
            else:
                name_male = name_male_first2
            

        # Female Name Generation
        female_name_type = random.choice(["simple", "combination"])

        if female_name_type == "simple":
            first_name_female = random.choice(maharashtra_female_firstname)
            suffix_female = random.choice(maharashtra_female_suffix)
            last_name_female = random.choice(maharashtra_surname)
            name_female_first = first_name_female + suffix_female + " " + last_name_female
            name_female_first2 = None
        elif female_name_type == "combination":
            suffix_female2 = random.choice(list(suffix_to_prefix_female.keys()))
            prefix_female2 = random.choice(suffix_to_prefix_female[suffix_female2])
            first_name_female2 = prefix_female2
            last_name_female = random.choice(maharashtra_surname)
            name_female_first2 = first_name_female2 + suffix_female2.lower() + " " + last_name_female
            name_female_first = None
            
        if preferences.get('name_type') == 'first':
            name_female = first_name_female + suffix_female  # Only first name + suffix
        else:
            # Use whichever name is not None
            if name_female_first is not None:
                name_female = name_female_first
            else:
                name_female = name_female_first2

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_maharashtra_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df

