import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_rajasthan_names(n, user_preference=None):
    # Rajasthan Male First Names
    rajasthani_male_firstname_hindu = [
        'Ajit', 'Veerendra', 'Ashwin', 'Aaditya', 'Rajesh', 'Kailashnath', 'Rudra', 'Raghuraj', 'Lakshman', 'Shatrughna', 'Kundan', 'Ramakant', 'Narendra',
        'Ganesh', 'Rajbir', 'Mohan', 'Deependra', 'Prithviraj', 'Rajendra', 'Pratap Bahadur', 'Sanjay', 'Deendayal', 'Ravindra Pratap', 'Ranveer', 'Ranbhir',
        'Deepak', 'Vasant', 'Vikesh', 'Sumit', 'Raghunath Ram', 'Vishnu', 'Kavindra', 'Raghvendra', 'Chandramohan', 'Ishwar Raj', 'Sohan', 'Kalu', 'Ravindra',
        'Kamlesh', 'Jai', 'Gopal', 'Parth', 'Shivaji', 'Poonam', 'Raj', 'Raghav', 'Maharaj', 'Nalin', 'Jaswant', 'Devansh', 'Devaram', 'Soma', 'Sudhir', 'Tejpal',
        'Kunwar', 'Tushar', 'Anuj', 'Kesar Singh', 'Hitesh', 'Gurvinder', 'Rajan', 'Rishabh Raj', 'Raghunandan', 'Chandan', 'Parveen', 'Jasvinder', 'Manohar',
        'Rohit', 'Ishaan', 'Sidharth', 'Kishan', 'Shubrajit', 'Manik', 'Bharat', 'Shubham', 'Harish', 'Arjun', 'Neeraj', 'Yogendra', 'Vishwesh', 'Virendra',
        'Sunder', 'Jivendra', 'Praveen', 'Laxman', 'Gagan', 'Siddharth', 'Babulal', 'Raghunath', 'Hiral', 'Govind', 'Krishan', 'Sudhakar', 'Mithun', 'Arvind',
        'Vimal', 'Mukesh', 'Samar', 'Sarvesh', 'Pritam', 'Yogesh', 'Karan', 'Vivek', 'Bakul', 'Yashwant', 'Mihir', 'Brijendra', 'Suresh', 'Himanshu', 'Sushil',
        'Shankar Lal', 'Sajjan', 'Surajit', 'Shivendra', 'Rishit', 'Amrit', 'Arun', 'Kishan Singh', 'Pranjal', 'Parmeshwar', 'Bhanwar', 'Bhanu', 'Raghveer',
        'Nilesh', 'Tarun', 'Dineshwar', 'Satyendra', 'Ajeet', 'Hiralal', 'Balveer', 'Amar', 'Devender', 'Kundanlal', 'Devendra', 'Nawal', 'Dinesh', 'Suhail',
        'Balwant', 'Anand', 'Naresh', 'Bhubaram', 'Sandeep', 'Mahendra', 'Ganpat', 'Chintan', 'Mohanlal', 'Anmol', 'Vishal', 'Sanjay Kumar', 'Veer', 'Gurdeep', 
        'Harvinder', 'Bhavesh', 'Bhanupratap', 'Bhagat', 'Kushal', 'Jagdish', 'Balaram', 'Shyam', 'Udayveer', 'Ramesh', 'Vijendra', 'Laxminarayan', 'Rajveer', 
        'Rajvinder', 'Chandra', 'Vikrant', 'Shivraj', 'Ishwar', 'Vinayak', 'Balkishan', 'Jitendra', 'Kailas', 'Narendra', 'Rameshwar', 'Mahesh', 'Kailash', 'Chandrapal', 
        'Rajendra Pratap', 'Jeevan', 'Tej', 'Ashish', 'Nirmal', 'Ashok', 'Arjun Singh', 'Premendra', 'Manvendra', 'Rajkumar', 'Sarvagya', 'Arjit', 'Manoj', 'Lokesh', 'Saurabh', 
        'Amit', 'Abhishek', 'Naveen', 'Shashank', 'Ajay', 'Pintu', 'Kishore', 'Subhash', 'Karanveer', 'Rishabh', 'Rajvendra', 'Shakti', 'Vir', 'Suryanarayan', 'Yashvardhan', 'Vishwajeet', 
        'Sunil', 'Surendra', 'Vishvesh', 'Prabhu', 'Ashesh', 'Chandreshwar', 'Swarup', 'Jagdeep', 'Krishna', 'Nitesh', 'Bhupender', 'Sahdev', 'Pramod', 'Shamsher', 'Pawan', 'Rajiv', 
        'Harsh', 'Omprakash', 'Dilip', 'Rajender', 'Jagat', 'Hari', 'Ansh', 'Anil', 'Chandresh', 'Madhusudan', 'Raghavendra', 'Uday', 'Jodh', 'Mukul', 
        'Nikhil', 'Brij', 'Bheem', 'Rana', 'Hemraj', 'Gaurav', 'Ambarish', 'Raju', 'Ratan', 'Dhanraj', 'Raghunath Singh', 'Vikram', 'Kamal', 'Lalit', 
        'Pankaj', 'Radheshyam', 'Tejendra', 'Girdhar', 'Chandrasen', 'Ladu', 'Gajendra', 'Satish', 'Kanak', 'Harishankar', 'Nitin', 'Vikramjit', 
        'Satyam', 'Sonu', 'Kishor', 'Suraj', 'Ravindra Singh', 'Chandrashekhar', 'Kesar', 'Prakash', 'Tejpal Singh', 'Balkrishna', 'Prathmesh', 
        'Bhanuprasad', 'Madan', 'Shankar', 'Ashok Kumar', 'Yash', 'Shailendra', 'Manish', 'Maan', 'Bhavar', 'Abhay', 'Ranjit', 'Suman', 'Chirag', 
        'Rajnish', 'Pravin', 'Shatrunjay', 'Chandran', 'Dharmendra', 'Karamveer', 'Vijay', 'Prem', 'Prabhakar', 'Shravan', 'Anwar', 'Udai', 
        'Surender', 'Rajkumar Singh', 'Ranvijay', 'Pradeep', 'Aniruddh', 'Rajat', 'Mahipal', 'Amardeep', 'Pratap', 'Tulsiram', 'Bhupendra', 
        'Gulab', 'Tejveer', 'Bhim', 'Harishchandra', 'Rakesh', 'Aarav', 'Krish', 'Girish', 'Chhagan', 'Narayan', 'Vikramaditya', 'Manmohan', 
        'Ramkishan', 'Balvir', 'Vinod', 'Rajaram', 'Raghbir', 'Chetan', 'Tanmay', 'Bhavani', 'Chiranjeev', 'Vikas', 'Vinay']
    # Rajasthan Male Surnames
    rajasthani_male_surname_hindu = [
        'Ram', 'Kumar', "Singh", "Rathore", "Chauhan", "Rajput", "Sengar", "Tomar", "Shekhawat", "Bishnoi", "Meena", "Jat", "Yadav", "Solanki",
        "Parmar", "Chandrawat", "Kachwaha", "Bagri", "Soni", "Raghav", "Bhawani", "Chand", "Kaswan", "Sakseria", "Sharma", "Lal",
        "Vyas", "Desai", "Patel", "Paliwal", "Beniwal", "Dadhich", "Choudhary", "Hada", "Agarwal", "Kothari", "Narang", "Khandelwal",
        "Gupta", "Chhipa", "Malviya", "Suryavanshi", "Kothari", "Tiwari", "Kumawat", "Jangid", "Tarkhan", "Dhakar", "Dewasi", "Kumar",
        "Kharwa", "Rathi", "Kumbhat", "Sakarwar", "Bhati", "Yograj", "Sardar", "Bansal", "Bhatia", "Sangwan", "Shah", "Jaiswal", "Dhoja",
        "Chahal", "Mishra", "Khatri", "Lodha", "Sanghi", "Kishore", "Prajapati", "Bhanwar", "Purohit", "Jangid", "Gadiya", "Surana",
        'Kumawat','Goyal','Mali','Gupta','Prajapat','Aggarwal','Chand','Bairwa','Meghwal','Poswal','Verma','Bansal','Pal','Gurjar','Puri',
        'Chandra','Gehlot','Sing','Prasad','Prakash','Garg','Jangid','Jha','Ghanchi','Sargara']
    # Rajasthan Female First Names
    rajasthani_female_firstname_hindu = [
        "Gayatri", "Padmini", "Durgavati", "Laxmibai", "Sita", "Vishala", "Sahiba", "Kesarbai", "Ratnavati", "Baiji Rao", "Kesar", "Anju", "Kumud", 
        "Rajwanti", "Chundawat", "Padmavati", "Bhati", "Anupama", "Gajri", "Shanta", "Vimalbai", "Tripti", "Minal", "Charushila", "Kamalwati", 
        "Sunanda", "Kalyani", "Arundhati", "Jodhbai", "Ganga", "Manorama", "Roopmati",
        "Gharibavati", "Gunjabai", "Champa", "Chanchal", "Krishna", "Devbai", "Kesar", "Yashoda", "Shree", "Shubhlata", "Aishwarya", "Anandi", 
        "Aruna", "Bhairavi", "Chandra", "Charulata", "Chhavi", "Devika", "Disha", "Gauri", "Gayatri", "Geetika", "Hemlata", "Indira", "Ishwari", 
        "Kamla", "Kesar", "Kirti", "Kumud", "Lajwanti", "Lalita", "Laxmi", "Manju", "Mohini", "Neelam", "Nandini", "Padma", "Padmini",
        "Rajkumari", "Rajwati", "Rameshwari", "Rani", "Rukmini", "Saanvi", "Saroj", "Shaila", "Shakti", "Shalini", "Sheetal", "Shivani", "Shreya", 
        "Snehal", "Suman", "Sunita", "Sumati", "Sushila", "Swati", "Tripti", "Usha", "Vandana", "Vibha", "Vishakha", "Yashoda", "Aarti", "Amrita", 
        "Asmita", "Bindiya", "Chitralekha", "Dalpati", "Dhanwati",  "Gokila", "Hansa", "Haripriya", "Heera", "Kamini", "Kashish", "Kirpal", "Kusum", 
        "Lajwati", "Manjuwanti", "Mayuri", "Mohana", "Nisha", "Poonam", "Rajrani", "Rajvi", "Rupal", "Rameshwari", "Rukshani", "Shalini", "Shubhra", 
        "Shilpa", "Sheetal",  "Yashika", "Alokika", "Amrapali", "Anjuli", "Anupama", "Aparna", "Arpita", "Basanti", "Bhavika", "Bhavana", "Bimla", 
        "Chandraja", "Chandrika", "Charushila", "Chhavi", "Darshana",
        "Deepika", "Dhara", "Divyanka", "Dulari", "Gajra", "Garima", "Geetanjali", "Hiral", "Jagriti", "Jayanti", "Jivika", "Kamalini", "Kanti", 
        "Karuna", "Kashmira", "Kiran", "Kshama", "Kusumwati", "Lalima", "Lajvanti", "Malini", "Manjuwanti", "Meenal", "Mohanika", "Nandita", "Narmada", "Neela", "Neelima", "Nirupa", "Padmavati", "Parnika", "Prabhati", "Poonam", "Rajeshwari", "Rajwanti", "Ranjana", "Rekha", "Riddhi", "Rima", "Ritu", "Sadhana", "Sakshi", "Sanchita", "Sandhya", "Seema", "Shakti", "Shanta", "Sharika", "Sheela", "Shilpi", "Shubhangi", "Shubhra", "Smita", "Snehalata", "Sudarshini", "Sumanthi", "Sunita", "Surabhi", "Surya", "Tanuja", "Tarini", "Trishala", "Ujjwala", "Uma", "Urmila", "Usha", "Vaidehi", "Vandita", "Varsha", "Vasundhara", "Vidhatri", "Vidhya", "Vijaya", "Vinita", "Vishwajeet", "Yamini", "Yashika", "Yojana",  "Ashmita", "Ashika", "Aadhya", "Aakriti", "Abhilasha", "Akansha", "Alka", "Amisha", "Anupama", "Anvika", "Archana", "Arpita", "Asita", "Avantika", "Bhakti", "Bhanupriya", "Bhavika", "Bhavya", "Chandani", "Chitralekha", "Darshini", "Deepika", "Deshna", "Devanshi", "Dhanvi", "Dimple",  "Geet", "Gitali", "Gurnam", "Harshika", "Heena", "Himani", "Indumati", "Iravati", "Ishita", "Jaya", "Jyoti", "Kamakshi", "Kanak", "Kanisha", "Kashvi", "Kaveri", "Kirti", "Kusum", "Lajwanti", "Latika", "Madhavi", "Mahika", "Malini", "Manju", "Meenal", "Minakshi", "Mohini", "Namrata", "Nandini", "Nandita",
        "Naina", "Neelam", "Neha", "Nikita", "Nisha", "Nivedita", "Pallavi", "Poonam", "Pranjali", "Preeti", "Prerana", "Rajani", "Rajlaxmi", 
        "Rajwanti", "Ranjita", "Rati", "Richa", "Rina", "Ritu", "Rupal", "Sadhana", "Sakshi", "Samriddhi", "Sandhya", "Sanya", "Shalini", "Shashi", 
        "Sheetal", "Shilpa", "Shivali", "Shraddha", "Shubha", "Shubhecha", "Smita", "Snehal", "Suman", "Sunita", "Surabhi", "Tanisha", "Tapasya", 
        "Trisha", "Vaidehi", "Vanita", "Vatsala", "Vimala", "Chhavi", "Ahalya", "Charul", "Gajala", "Gouri", "Asha", "Bharti", "Charvi", "Divya", 
        "Kamla", "Meenakshi",
        "Dhirajwati", "Sushmita", "Janaki", "Shubhanjali", "Jivika", "Chandrakala",  "Aishwarya", "Alka", "Anju", "Archana", "Chandni", "Charulata", 
        "Devika", "Durga", "Geetanjali", "Gauri", "Ganga", "Hema", "Jaya", "Kamini", "Kiran", "Manju", "Meera", "Minal", "Nandini", "Pooja", 
        "Rajkumari", "Rani", "Rekha", "Rupal", "Shakti", "Shalini", "Shubhi", "Sonal", "Sumitra", "Tanvi", "Triveni", "Urmila", "Vidhya", "Vina", 
        "Vasundhara", "Yashoda", "Suman", "Chhavi", "Swati", "Simran", "Kanak", "Kesar", "Maya", "Kusum", "Neelam", "Komal", "Manju", "Shubhi", 
        "Suman", "Shalini", "Jeevika", "Tanuja", "Naina", "Ritika", "Rashmi", "Meenal", "Pooja", "Kajal", "Sakshi", "Nidhi", "Vandana", "Sonali", 
        "Sushmita", "Rupal", "Kanak", "Neha", "Manju", "Snehal", "Priti", "Pranjal", "Bhavna", "Shreya", "Tanisha", "Aarti", "Pallavi", "Rajwanti", 
        "Anjali", "Bhawna", "Rekha", "Suman", "Komal", "Bhavya", "Sita", "Renu", "Anushka", "Bhavika", "Simran", "Radhika", "Nikita", "Reema", 
        "Nirali", "Priyanka", "Chanchal", "Shubham", "Purnima", "Pramila", "Nikita", "Manisha", "Rupal", "Vandana", "Rupali", "Sushila", "Vishaka", 
        "Kavita", "Shashi", "Chandrika", "Gargi", "Aruna", "Swati", "Ravina", "Rakhi", "Kavita"  ]
    rajasthani_female_surname_hindu = [
        "Rathore", "Choudhary", "Rajput", "Shekhawat", "Mehta", "Kothari", "Sharma", "Purohit", "Jain", "Bishnoi", 
        "Soni", "Gupta", "Mahawar", "Agarwal", "Bairwa", "Dadhich", "Sikarwar", "Mali", "Parihar", "Bhat", "Pathak", 
        "Yadav", "Chaudhury", "Tanwar", "Vyas", "Bhargava", "Suthar", "Gujjar", "Rawat", "Bhandari", "Goyal", "Raval", 
        "Khatri", "Vishnoi", "Panchal", "Gadhvi", "Solanki", "Kadiwala", "Lodhi", "Chokshi", "Khandelwal", "Nathwani", 
        "Mishra", "Bora", "Bhimani", "Kachhwaha", "Khachra", "Jatav", "Gajjar", "Devi", "Kumari", "Bai", "Ben", "Meena", 
        "Prajapat", "Bansal", "Aggarwal", "Ghanchi", "Verma", "Badala", "Garg", "Lohar", "Rawal", "Gehlot", "Kushwaha", 
        "Meghwal", "Bhil", "Khandelwal", "Kumawat", "Rani", "Madhiwal", "Parashar", "Raj", "Ram", "Rebari", "Sahu", 
        "Sargara", "Sen", "Hada", "Kachawa", "Singhvi", "Jhala", "Charan", "Naagar", "Kalal", "Paliwal"
    ]
    #Muslim names
    rajasthani_male_firstname_muslim = [
        "Ahmed", "Ali", "Imran", "Ibrahim", "Rehman", "Rashid", "Salim", "Suleman", "Shahbaz",
        "Farhan", "Zahid", "Nasir", "Faiz", "Fahad", "Mustafa", "Rizwan", "Yusuf", "Shoaib",
        "Bilal", "Omar", "Hassan", "Zeeshan", "Sami", "Tariq", "Nashit", "Rafiq", "Jameel",
        "Raza", "Khaleel", "Kasim", "Murtaza", "Adnan", "Furqan", "Zubair", "Shakir",
        "Rehan", "Ayaan", "Arif", "Sajid", "Shabbir", "Bashir", "Arsalan", "Wasiq"
    ]
    rajasthani_male_surname_muslim = [
        "Khan", "Shaikh", "Ansari", "Pathan", "Syed","Qureshi", "Mirza", "Rizvi", "Siddiqui","Chaudhary","Farooqi","Jamal","Pasha",
        "Bukhari","Memon","Rashid","Jafari","Hussain","Bashir","Mir","Sarmadi","Qadir","Mujtaba","Ghulam","Hafeez","Latif","Amin","Bhat",
        "Ali","Nadvi","Javed","Lodhi","Azmi","Anwar","Haider","Firoz"]
    rajasthani_female_firstname_muslim = [
        "Ayesha", "Fatima", "Khadija", "Zainab", "Sana", "Mariyam", "Amna", "Rabia", "Tasneem", "Fariha", 
        "Amina", "Noor", "Sadaf", "Lubna", "Shazia", "Areeba", "Bushra", "Zara", "Kausar", "Mehwish", 
        "Asma", "Nazia", "Sadia", "Samina", "Huma", "Nazish", "Saira", "Shamim", "Nabila", "Razia",
        "Afreen", "Rukhsar", "Bushra", "Jameela", "Sana", "Fariha", "Nigar", "Shahnaz", "Nazrana",'Huma'
    ]
    rajasthani_female_surname_muslim = [
        'Bano',"Khan", "Shaikh", "Ansari", "Pathan", "Syed", "Qureshi", "Rizvi", "Siddiqui", "Chaudhary", "Mirza", 
        "Farooqi", "Bukhari", "Memon", "Khan", "Rashid", "Jafari", "Hussain", "Bashir", "Sarmadi", 
        "Qadir", "Mujtaba", "Ghulam", "Bhat", "Ali", "Azmi", "Anwar", "Haider", "Firoz", "Rashid", 
        "Latif", "Mughal", "Khan", "Javed", "Amin", "Lodhi", "Sajid", "Fatima", "Zahra", "Mir", 
        "Akhtar", "Sultana", "Kausar", "Parveen"
    ]
    # Religion Percentages
    religion_percentages = {
        'male': {'hindu': 70, 'muslim': 30},
        'female': {'hindu': 70, 'muslim': 30}
    }

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        if random.random() < religion_percentages['male']['hindu'] / 100:
            # Hindu Male Name
            first_name_male = random.choice(rajasthani_male_firstname_hindu)
            last_name_male = random.choice(rajasthani_male_surname_hindu)
        else:
            # Muslim Male Name
            first_name_male = random.choice(rajasthani_male_firstname_muslim)
            last_name_male = random.choice(rajasthani_male_surname_muslim)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        if random.random() < religion_percentages['female']['hindu'] / 100:
            # Hindu Female Name
            first_name_female = random.choice(rajasthani_female_firstname_hindu)
            last_name_female = random.choice(rajasthani_female_surname_hindu)
        else:
            # Muslim Female Name
            first_name_female = random.choice(rajasthani_female_firstname_muslim)
            last_name_female = random.choice(rajasthani_female_surname_muslim)

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
    file_path = 'generated_rajasthani_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df