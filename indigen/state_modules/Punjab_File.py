import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Punjab Male and Female First Names and Surnames
def generate_punjab_names(n, user_preference=None):
    
    suffix_to_prefixes_male = {"jeet": ["Gur", "Har", "Kul", "Aman", "Amar", "Kanwal", "Charan", "Sharan", "Man", "Sukh", 
        "Karam", "Prabhu", "Gagan", "Sur", "Indar", "Bal", "Simaran", "Sarab", "Ran", "Param", 
        "Dal", "Manindar", "Samar", "Swaran", "Sikandar", "Jag", "Man"],
                           "deep": ["Kul", "Aman", "Har", "Gur", "Raman", "Man", "Jag", "Gagan", "Harsh", "Daman", 
        "Sharan", "Jas", "Nav", "Jag"],
                           "Veer": [ "Bal", "Lakh", "Dal", "Jas", "Sukh", "Ran", "Raghu"],
        "Bir": ["Bal", "Lakh", "Dal", "Jas", "Sukh", "Ran", "Raghu"],
        "preet": ["Gur", "Har", "Man", "Sukh", "Amar", "Dal", "Jag"],
        "indar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
         "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "vindar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
        "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "jindar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
        "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "mindar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
        "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "shindar": ["Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "want": ["Kul", "Khush", "Kush", "Sat", "Jas", "Sukh", "Bal", "Bhag"],
        "meet": ["Gur", "Jag", "Man", "Har", "Sukh"],
        "pal": ["Gur", "Jas", "Har", "Tej", "Inder", "Maninder"],
        "jot": ["Prabh", "Nav", "Sukh", "Aman"],
                               "dev":["Har","Sukh", "Bal", "Kul"],
                               "mohan":["Man", "Jag"]}

    prefix_to_suffixes = {"Har": ["Keerat", "Dayal", "Bant", "Vant", "Bhajan", "Preet", "Jeet", "Deep", "nek", 
        "Jindar", "Mindar", "Vindar", "Indar", "Shindar", "Charan", "Govind", "Kishan", "Nam", 
        "Mesh", "Pal", "Mohindar", "Simran", "Harwant"],
        "Sukh": ["Mindar", "Jindar", "Windar", "Shindar"],
        "Man": ["Deep", "Jeet", "Inder"],
        "Kul": ["want", "Jindar", "Mindar", "Deep"],
        "Bal": ["Want", "Kar", "Beer", "Jeet", "Vindar", "Jindar"],
        "Jag": ["Jeet", "Tar", "Deep", "Meet", "Pal"]}

    suffix_to_prefixes_female = {"jeet": ["Gur", "Har", "Kul", "Aman", "Amar", "Kanwal", "Charan", "Sharan", "Man", "Sukh", 
        "Karam", "Prabhu", "Gagan", "Sur", "Indar", "Bal", "Simaran", "Sarab", "Ran", "Param", 
        "Dal", "Manindar", "Samar", "Swaran", "Sikandar", "Jag", "Man"],
                           "deep": ["Kul", "Aman", "Har", "Gur", "Raman", "Man", "Jag", "Gagan", "Harsh", "Daman", 
        "Sharan", "Jas", "Nav", "Jag"],
                           "veer": [ "Bal", "Lakh", "Dal", "Jas", "Sukh", "Ran", "Raghu"],
        "bir": ["Bal", "Lakh", "Dal", "Jas", "Sukh", "Ran", "Raghu"],
        "preet": ["Gur", "Har", "Man", "Sukh", "Amar", "Dal", "Jag"],
        "indar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
         "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "vindar": ["Gur", "Jag", "Sur", "Tej", "De","Bhup", "Har", "Sat", 
        "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "jindar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
        "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "mindar": ["Gur", "Jag", "Sur", "Tap", "Tej", "Dev", "Veer", "Moh", "Maha", "Bhup", "Har", "Sat", 
        "Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "shindar": ["Kul", "Raj", "Param", "Jas", "Man", "Bal"],
        "want": ["Kul", "Khush", "Kush", "Sat", "Jas", "Sukh", "Bal", "Bhag"],
        "meet": ["Gur", "Jag", "Man", "Har", "Sukh"],
        "pal": ["Gur", "Jas", "Har", "Tej", "Inder", "Maninder"],
        "jot": ["Prabhu", "Nav", "Sukh", "Aman"],
        "leen": [
        "Har", "Nav", "Sukh", "Gur", "Simran", "Jas", "Amrit", 
        "Parm", "Kiran","Bani", "Tej", "Shiv", "Aman", "Prit"],
    "noor": [
        "Simran", "Nav", "Sukh", "Gur", "Amrit","Tej", 
        "Kiran", "Rav", "Prit", "Jas", "Rup", "Nisha"]}

    
    punjabi_surnames = [
        "Ahuja", "Aulakh", "Bajwa", "Bains", "Bedi", "Bhalla", "Bhatia", "Bhullar", 
    "Bindra", "Brar", "Chadha", "Chahal", "Chaudhary", "Chima", "Dhaliwal", 
    "Dhillon", "Duggal", "Fateh", "Gill", "Grewal", "Hayer", "Kahlon", "Kang", 
    "Khalra", "Kohli", "Lamba", "Makkar", "Malhotra", "Mann", "Mangat", "Mehta", 
    "Nijjar", "Nanda", "Pannu", "Rai", "Rakhra", "Rana", "Sahota", "Sandhu", 
    "Sekhon", "Sidhu", "Sohal", "Sodhi", "Suri", "Toor"]
    
    punjabi_female_middlename = ['Kaur']
    punjabi_male_middlename = ['', 'Singh', 'Singh']


    # Punjabi Hindu names
    punjabi_hindu_male_names = [
    "Abeer", "Abhiman", "Adesh", "Ajit", "Ajmer", "Akal", "Akashdeep", "Akhand", "Amandeep",
    "Amarjeet", "Amarjit", "Amarnath", "Amarpal", "Amarpreet", "Amrik", "Anup", "Arjan", "Armaan",
    "Arvind", "Arvinder", "Ashok", "Avtar", "Balbir", "Baldev", "Baljit", "Balkrishan",
    "Balraj", "Balveer", "Balvinder", "Balwant", "Balwinder", "Bhagat", "Bhagwan", "Bhanu",
    "Bhimsen", "Bhola", "Bhupinder", "Bishan", "Chaman", "Chanchal", "Chandan", "Chander", "Chandrapal",
    "Charanjit", "Chattar", "Chiman", "Daler", "Darbara", "Darshan", "Darvesh", "Daya", "Dayal", "Dayaram",
    "Deepak", "Dev", "Devinder", "Devraj", "Dharam", "Dharamveer", "Dhirendra", "Dhruv", "Eshwar",
    "Gagan", "Ganesh", "Gian", "Girdhari", "Gopal", "Gopi", "Gurbaksh", "Gurdas", "Gurdev", "Gurdip",
    "Gurnam", "Gurpal", "Gurpreet", "Gyaneshwar", "Harbhajan", "Hardayal", "Hardeep", "Hardev",
    "Hargobind", "Hargun", "Hari", "Harinder", "Hariom", "Harish", "Harjeet", "Harmeet",
    "Harnaam", "Harnam", "Harpal", "Harvinder", "Himmat", "Inderjeet", "Inderjit", "Inderpal",
    "Ishar", "Ishwar", "Jagat", "Jagatpal", "Jagbir", "Jagdeep", "Jagdev", "Jagdish", "Jagir",
    "Jagjeet", "Janak", "Janakraj", "Jarnail", "Jasbir", "Jaspal", "Jaspinder", "Jaswant", "Jatin",
    "Jatinder", "Jeet", "Jeevan", "Jitender", "Joginder", "Jograj", "Kamaljeet", "Kanwar", "Karam",
    "Karamveer", "Karanveer", "Karminder", "Kartar", "Kartikey", "Kehar", "Kewal", "Kirpal", "Kirti",
    "Kripal", "Kulbhushan", "Kulbir", "Kuldeep", "Kuljeet", "Kulraj", "Kulvir", "Kundan", "Lajpat",
    "Lakhbir", "Lakhraj", "Lakhwinder", "Lakshman", "Madan", "Madhav", "Mahesh", "Mahinder", "Mandeep",
    "Mangal", "Maninder", "Manjeet", "Manmohan", "Manohar", "Manpreet", "Mohan", "Mohanbir", "Mohinder",
    "Mohinderpal", "Mukesh", "Mukund", "Munish", "Nahar", "Naib", "Nandlal", "Narayan", "Naresh", "Nareshpal",
    "Narinder", "Nasib", "Nathu", "Navdeep", "Nihal", "Niranjan", "Nirmal", "Omkar", "Omprakash", "Pankaj",
    "Paramjit", "Paramveer", "Pardeep", "Pargat", "Parkash", "Parvinder", "Phool", "Pirthi", "Prabhjot", "Pratap",
    "Prem", "Premchand", "Premjeet", "Pritam", "Pritpal", "Puran", "Raghubir", "Rajat", "Rajendra", "Rajeshwar",
    "Rajinder", "Rajkumar", "Rajveer", "Ram", "Ramesh", "Rameshwar", "Raminder", "Ramkishan", "Ramnik", "Rampal", "Randhir",
    "Ranjeet", "Ranjeev", "Rattan", "Ravinder", "Ravindra", "Roshan", "Rupinder", "Sahil", "Sanjay", "Sanjeev", "Sanwar",
    "Sardar", "Sardool", "Saroop", "Sarvan", "Sarwan", "Satbir", "Satinder", "Satnam", "Satpal", "Sawarn", "Sewak", "Sham",
    "Shankar", "Sher", "Shivraj", "Shyam", "Sohan", "Sohanlal", "Sukhbir", "Sukhdev", "Sukhpal", "Sumer", "Sundar", "Sunder", "Suraj",
    "Suresh", "Surinder", "Surjeet", "Tanveer", "Tara", "Tarsem", "Tarun", "Tejinder", "Tejpal", "Thakur", "Tilak", "Tirlok",
    "Trilok", "Uday", "Udham", "Ujagar", "Umang", "Umesh", "Upinder", "Upkar", "Vaidya", "Vanshik", "Varinder", "Vedant", "Vedprakash", "Veerpal", "Vijendra", "Vikram", "Vimal", "Vinod", "Viraj", "Virender", "Virendra", "Vishnu", "Vivanraj", "Yashpal", "Yashwant", "Yatharth", "Yudhvir", "Yugveer", "Yuvraj", "Zorawar", "Zorawarveer"
]
    punjabi_hindu_female_names = [
    "Aanchal", "Aarti", "Aashima", "Abha", "Abhilasha", "Achla", "Ajeeta", "Akriti", "Alaknanda", "Alka",
    "Amardeep", "Amarjot", "Amolak", "Amrapali", "Amrita", "Amritjeet", "Amritpal", "Anandi", "Anisha", "Anita",
    "Anjali", "Anjana", "Anoushka", "Anupama", "Anuradha", "Anushka", "Anvika", "Aradhna", "Archana", "Arpita",
    "Aruna", "Arundhati", "Asha", "Ashmita", "Avantika", "Avneet", "Ayesha", "Ayushmati", "Babita", "Bala",
    "Baldeep", "Baljeet", "Baljinder", "Balvinder", "Balwant", "Balwantjeet", "Balwinder", "Banita", "Basanti", "Bela",
    "Bhagwanti", "Bhagwati", "Bhagyashree", "Bhano", "Bhanupriya", "Bharati", "Bhavani", "Bhavna", "Bholi", "Binita",
    "Binni", "Champa", "Chanchal", "Chandini", "Chandrani", "Chandrapreet", "Charanjit", "Charumati", "Chhavi", "Chitralekha",
    "Damini", "Darshana", "Davinder", "Daya", "Dayawanti", "Dayawati", "Deepika", "Deepinder",
    "Deepmala", "Deepshikha", "Deepti", "Devangana", "Devika", "Devina", "Devinder", "Dhanwanti", "Diksha",
    "Diljeet", "Dipali", "Dolly", "Durga", "Ekta", "Esha", "Gagandeep", "Ganga", "Gauri", "Gayatri",
    "Geeta", "Geetanjali", "Girija", "Gulabo", "Guljeet", "Gulshan", "Gunjan", "Gunjinder", "Gurinder", "Gurleen",
    "Gurpinder", "Gursharan", "Gurvinder", "Hamsini", "Hansika", "Hardeep", "Harinder", "Harjit",
    "Harkiran", "Harleen",  "Harminder", "Harpreet", "Harshita", "Harvinder", "Hema", "Hemlata", "Himani",
    "Inderjeet", "Indira", "Indu", "Indumati", "Ira", "Ishani", "Ishika", "Ishita", "Ishmeet", "Ishwinder",
    "Jagjit", "Jagrati", "Jamuna", "Janaki", "Janhavi", "Janki", "Jasbir", "Jaskiran", "Jasleen", "Jasmeen",
    "Jasmeet", "Jaspreet", "Jaswinder", "Jaya", "Jeet", "Jeevan", "Jeevika", "Jhanvi", "Jharna", "Jyoti",
    "Jyotsana", "Jyotsna", "Kalpana", "Kamaljeet", "Kamini", "Kamla", "Kamlesh", "Kanak", "Kanwaljeet",
    "Karamjeet", "Karishma", "Karuna", "Kaveri", "Kavita", "Kavya", "Keerti", "Kiran", "Kirandeep", "Kiranjeet",
    "Kiranjit", "Kiranmayi", "Kiranpal", "Kirpal", "Komal", "Krishma", "Krishnaveni", "Kuldeep", "Kuljeet", "Kusum",
    "Kusumlata", "Lajwanti", "Lajwinder", "Lakshita", "Lalima", "Lalita", "Laljinder", "Lata", "Laxmi", "Leela",
    "Leelawati", "Maanvi", "Madhavi", "Madhu", "Madhubala", "Mahalakshmi", "Mahima", "Mahinderjeet", "Mala", "Malini",
    "Mamta", "Manisha", "Manjiri", "Manjit", "Manju", "Manjula", "Manjusha", "Manorama", "Manpreet", "Mayuri",
    "Meena", "Meenal", "Meera", "Megha", "Meher", "Minakshi", "Minal", "Mohinder", "Mohini", "Monika",
    "Mukta", "Munni", "Naina", "Namita", "Namrata", "Nanda", "Nandini", "Nandita", "Neelam", "Neelima",
    "Neha", "Nidhi", "Nilima", "Nimisha", "Nimmo", "Nimrit", "Niranjana", "Nirmal", "Nirmala", "Nirupama",
    "Nisha", "Nishita", "Nupur", "Padma", "Padmavati", "Pallavi", "Panchami", "Pankhuri", "Paramjeet", "Paramjit",
    "Parineeta", "Parminder", "Parvati", "Parveen", "Pavneet", "Pinky", "Pooja", "Poonam", "Prabhjot", "Prabhleen",
    "Pradnya", "Pragati", "Pramila", "Pratibha", "Pratima", "Preeti", "Preetinder", "Prem", "Premila", "Premlata",
    "Prerna", "Prithpal", "Priya", "Priyamvada", "Pushpa", "Pushpita", "Rachna", "Radha", "Ragini", "Rajashree",
    "Rajini", "Rajkumari", "Rajni", "Rajshree", "Rajveer", "Rama", "Ramandeep", "Raminder",
    "Ramita", "Ramneek", "Rani", "Ranjana", "Ranjita", "Rati", "Reena", "Rekha", "Renu", "Renuka",
    "Reshma", "Rewa", "Richa", "Rina", "Rinku", "Rishika", "Ritu", "Roopa", "Roopinder", "Rooprekha",
    "Roshni", "Rubina", "Ruchika", "Rukmani", "Rupinder", "Rupinderjeet", "Saadhna", "Saavitri", "Sabita", "Sadhna",
    "Samina", "Sandhya", "Sanghita", "Sangita", "Sanjana", "Sapna", "Sarbdeep", "Sarbjeet", "Sarita", "Saroj",
    "Sarojini", "Sarvani", "Satyawati", "Savita", "Savitri", "Seema", "Shaila", "Shailee", "Shalini", "Shanta", "Sharada", "Sharandeep", "Sharanjit", "Sharmila", "Sharvani",
    "Sheela", "Sheetal", "Shefali", "Shikha", "Shital", "Shivani", "Shivpriya", "Shobha", "Shraddha", "Shruti",
    "Simran", "Simranjeet", "Simranjit", "Simrat", "Sindhu", "Smita", "Sneh", "Snehlata", "Sonal", "Sonia",
    "Sonika", "Sonu", "Sravani", "Subhashini", "Sudha", "Sugandha", "Sujata", "Sulochana", "Suman", "Sumana",
    "Sumanjeet", "Sunita", "Surinder", "Sushila", "Sushma", "Suvarna", "Swarnalata", "Swarnjeet", "Swati", "Tanisha",
    "Tanvika", "Tara", "Tarandeep", "Tarawati", "Tarini", "Tejinder", "Tripta", "Triveni", "Ujjwala", "Ujwaldeep",
    "Uma", "Umang", "Upasana", "Upma", "Urmila", "Usha", "Vandana", "Varinder", "Veena", "Vidya",
    "Vimal", "Vimala", "Vimla", "Vinita", "Vinodini", "Vishakha", "Yashika", "Yashoda", "Yashpreet", "Yogini",
    "Yogita"]

    punjabi_hindu_surnames= ["Atri", "Bahl", "Bajwa", "Bakshi", "Bansal", "Batra", "Bedi", "Bhasin", "Bhatia", "Bhatt", "Bindra",
      "Chadha", "Chauhan", "Chawla", "Chhabra", "Chitkara", "Chopra", "Chugh", "Dawar", "Dhawan", "Dhir", "Garg",
      "Ghai", "Goel", "Gosaeen", "Grover", "Gulati", "Gupta", "Jaitley", "Joshi", "Kalra", "Kapila", "Kapoor",
      "Kapur", "Katyal", "Khanna", "Kharbanda", "Khattar", "Khosla", "Khurana", "Khurrana", "Kochar", "Kochhar",
      "Kohli", "Madan", "Mahajan", "Malhotra", "Mannan", "Mehta", "Nagrath", "Narula", "Oberoi", "Pasrichia",
      "Passi", "Prabhakar", "Puri", "Rai", "Rampal", "Sachdeva", "Saggar", "Sahi", "Salaria", "Saluja", "Sarin",
      "Sehgal", "Sehjpal", "Seth", "Sethi", "Sharma", "Singla", "Soni", "Sood", "Suri", "Tuli", "Valecha", "Verma",
      "Dhingra", "Chaddha", "Dhamija", "Bedi", "Arora", "Bhagat", "Duggal", "Goel", "Jindal", "Mittal", "Puri", "Tandon", "Talwar", "Randhwa"]
    
    
     # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names

        
        # Male Name Generation
        if random.choice(["Hindu", "Sikh"]) == "Sikh":
            name_type = random.choice(["suffix", "prefix"])
            if name_type == "suffix":      
                suffix_male = random.choice(list(suffix_to_prefixes_male.keys()))
                prefix_male = random.choice(suffix_to_prefixes_male[suffix_male])
                male_first = prefix_male + suffix_male.lower()
                male_middle = random.choice(punjabi_male_middlename)
                last_name_male = random.choice(punjabi_surnames)
                
            elif name_type == "prefix":
                prefix_male = random.choice(list(prefix_to_suffixes.keys()))
                suffix_male = random.choice(prefix_to_suffixes[prefix_male])
                male_first = prefix_male + suffix_male.lower()
                male_middle = random.choice(punjabi_male_middlename)
                last_name_male = random.choice(punjabi_surnames)
           
        else:
            male_first = random.choice(punjabi_hindu_male_names)
            male_middle = None
            last_name_male = random.choice(punjabi_hindu_surnames)

        if preferences.get('name_type') == 'first':
            name_male = male_first  # Only first name
        else:
            # Construct full name, only adding the middle name if it's not None
            if male_middle:
                name_male = male_first + " " + male_middle + " " + last_name_male
            else:
                name_male = male_first + " " + last_name_male

        # Female Name Generation
        if random.choice(["Hindu", "Sikh"]) == "Sikh":
            name_type = random.choice(["suffix", "prefix"])

            if name_type == "suffix":      
                suffix_female = random.choice(list(suffix_to_prefixes_female.keys()))
                prefix_female = random.choice(suffix_to_prefixes_female[suffix_female])
                female_first = prefix_female + suffix_female.lower()
                female_middle = random.choice(punjabi_female_middlename)
                last_name_female = random.choice(punjabi_surnames)
                
            elif name_type == "prefix":
                prefix_female = random.choice(list(prefix_to_suffixes.keys()))
                suffix_female = random.choice(prefix_to_suffixes[prefix_female])
                female_first = prefix_female + suffix_female.lower()
                female_middle = random.choice(punjabi_female_middlename)
                last_name_female = random.choice(punjabi_surnames)
    
        else:
            female_first = random.choice(punjabi_hindu_female_names)
            female_middle = None
            last_name_female = random.choice(punjabi_hindu_surnames)

        if preferences.get('name_type') == 'first':
            name_female = female_first  # Only first name
        else:
            if female_middle:
                name_female = female_first + " " + female_middle +" "+ last_name_female  # Full name
            else:
                name_female = female_first + " " + last_name_female

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_punjab_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df

