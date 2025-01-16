import random
import pandas as pd
import os


# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_jk_names(n, user_preference=None, seed=None):

    # Kashmiri Pandit Male First Names
    kashmiri_pandit_male_firstname= [
        "Aaditya", "Abhinav", "Ajay", "Akhil", "Alok", "Amit", "Anand", "Anil", "Ankit", "Anupam",
        "Arjun", "Ashok", "Avinash", "Balraj", "Bharat", "Bhaskar", "Chetan", "Chander", "Dinesh", "Deepak",
        "Dev", "Devendra", "Dhananjay", "Dhruv", "Dinesh", "Gautam", "Gopal", "Govind", "Hari", "Harish",
        "Hemant", "Ishaan", "Jagat", "Jai", "Jatin", "Jitendra", "Kailash", "Kamal", "Karan", "Kartik",
        "Krishna", "Kuldeep", "Lalit", "Lokesh", "Madan", "Mahesh", "Manish", "Mohan", "Mukesh", "Naveen",
        "Neeraj", "Nikhil", "Nitin", "Omkar", "Pankaj", "Parmesh", "Piyush", "Pradeep", "Prakash", "Prashant",
        "Raghav", "Rajesh", "Rajiv", "Rakesh", "Raman", "Ramesh", "Ravi", "Rohit", "Sachin", "Sandeep",
        "Sanjay", "Sarat", "Sarvesh", "Satish", "Shailendra", "Shankar", "Shantanu", "Sharad", "Shashi", "Shekhar",
        "Shiv", "Shridhar", "Siddharth", "Somesh", "Subhash", "Sujit", "Suman", "Suresh", "Surya", "Tej",
        "Trilok", "Uday", "Upendra", "Vaibhav", "Vikas", "Vikram", "Vinay", "Vineet", "Vishal", "Yash"]


    # Kashmiri Pandit Surnames
    kashmiri_pandit_surname= [
        "Bhat", "Pandit", "Razdan", "Kaul", "Kachru", "Handoo", "Wali", "Zutshi", "Raina", "Tickoo",
        "Munshi", "Koul", "Khar", "Bhan", "Sopori", "Kaw", "Wanchoo", "Hak", "Mattoo", "Ganju",
        "Dhar", "Bamzai", "Chakoo", "Jalali", "Tikoo", "Saraf", "Nehr", "Chrungoo", "Sapru", "Katju",
        "Malla", "Hangloo", "Taploo", "Bhatt", "Mushran", "Safaya", "Teng", "Peshin", "Gurtu", "Zadoo",
        "Haksar", "Reu", "Bhagati", "Talashi", "Wakhaloo", "Sharga", "Trakroo", "Yachh", "Dulloo", "Sharga",
        "Zalpuri", "Sharma", "Patloo", "Kher", "Mushran", "Chrungoo", "Thussu", "Saproo", "Ramanuj", "Bambroo",
        "Dar", "Madan", "Sondhi", "Mastoo", "Taimini", "Karihaloo", "Pandita", "Rangroo", "Zadoo", "Gurtu",
        "Razdan", "Ravinder", "Bhagati", "Bharany", "Misri", "Kaushik", "Gadroo", "Hingoo", "Wazir", "Kalra",
        "Nehru", "Dadoo", "Magotra", "Rainu", "Handoo", "Malla", "Kaak", "Jalali", "Chaku", "Nadru",
        "Ashai", "Parimoo", "Chrungoo", "Katru", "Gadroo", "Fotedar", "Trisal", "Jaitley", "Bamzai", "Takoo"]


    # Kashmiri Pandit Female First Names
    kashmiri_pandit_female_firstname = [
        "Aarti", "Aditi", "Anjali", "Anita", "Archana", "Aruna", "Ashima", "Aslesha", "Bhavani", "Chandrika",
        "Damini", "Deepali", "Devika", "Diksha", "Ekta", "Gayatri", "Geeta", "Hansa", "Indira", "Ishani",
        "Jaya", "Jyoti", "Kajal", "Kalpana", "Kamla", "Kiran", "Kumud", "Lalita", "Leela", "Lata",
        "Madhuri", "Manisha", "Meenakshi", "Mira", "Mona", "Nalini", "Namrata", "Nandita", "Neelam", "Nidhi",
        "Padma", "Pallavi", "Parvati", "Pragya", "Priya", "Purnima", "Radha", "Rajni", "Reena", "Rita",
        "Sakshi", "Sangeeta", "Sarita", "Seema", "Shalini", "Shanta", "Sharda", "Sheetal", "Shikha", "Shilpa",
        "Smita", "Sneha", "Sonal", "Suman", "Sunanda", "Sunita", "Sushma", "Swapna", "Tanvi", "Trishna",
        "Urmila", "Vaishali", "Vandana", "Varsha", "Vasudha", "Vijaya", "Vinita", "Yamini", "Yashoda", "Yogita",
        "Aasha", "Aishwarya", "Amrita", "Ankita", "Anupama", "Bhawna", "Chhavi", "Deeksha", "Gauri", "Ira",
        "Karishma", "Lakshmi", "Megha", "Neetu", "Nirmala", "Pooja", "Priti", "Rakhi", "Rashmi", "Veena"]

    #  Male Ladakhi First Names
    ladakh_male_firstname= [
    "Lobsang", "Lama", "Sangpo", "Kalsang", "Rigzin", "Palden", "Chakmo", "Sangay", 
    "Tenzin", "Nawang", "Namgyal", "Yeshe", "Rinchen", "Tsering", "Kundun", "Rinpoche", 
    "Dorje", "Tsewang", "Phuntsok", "Karma", "Sherab", "Tshering", "Kunzang", "Phurpa", 
    "Zangpo"]

    # Ladakhi Surnames
    ladakh_surname= ['Zangmo', 'Ngawang', 'Sangpo', 'Sungmo', 'Namdrol', 'Mendrel', 'Dama', 'Phurba', 'Kundun',
    'Zalpo', 'Palden', 'Choden', 'Wangchuk', 'Chudak', 'Jigdral', 'Chhakpa', 'Dorje', 'Sherpa', 'Tenzing', 'Phunzo',
    'Chakyi', 'Rinpoche', 'Kelden', 'Momo', 'Yunda', 'Lobsang', 'Palmo', 'Phuntsok', 'Tashi', 'Nangpo', 'Tsewang',
    'Dorji', 'Tashong', 'Gonpo', 'Samdup', 'Palchen', 'Tshering', 'Gyalpo', 'Kalsang', 'Sangmo', 'Lhagyari',
    'Kunzang', 'Angmo', 'Zawa', 'Tharchin', 'Shambu', 'Tsomo', 'Tsultrim', 'Dornay', 'Gendun', 'Lama', 'Zigpo',
    'Gyalmo', 'Gye', 'Sherab', 'Lhabuk', 'Sonam', 'Phurpa', 'Tashichoden', 'Sangay', 'Chawang', 'Karma', 'Jampa',
    'Yangchen', 'Gyaltsen', 'Namgyal', 'Jigme', 'Lunpo', 'Nima', 'Drolma', 'Tsering', 'Tensung', 'Choskyi', 'Tenzin',
    'Zawang', 'Dawa', 'Zangpo', 'Lhawang','Norbu', 'Wangpo', 'Sharma', 'Tendhar', 'Tsenpo', 'Rinchen', 'Chukyi',
    'Chakmo', 'Gyatso', 'Pema', 'Yangzom', 'Thundup', 'Gyelpo']  
        
    #  Female Ladakhi First Names
    ladakh_female_firstname= [
    "Aditi", "Chakmo", "Choden", "Chhime", "Choskyi", "Dolma", "Drolma", "Gyalmo",
    "Lhamo", "Lhagyari", "Maya", "Momo", "Palmo", "Pema", "Sangmo", "Sonam", "Tashi",
    "Tshomo", "Yangchen", "Yunmo", "Zangmo", "Zawmo", "Zathmo", "Yeshe"
]

    # Muslim Male First Names
    muslim_male_firstname= [
        "Aarif", "Adil", "Aftab", "Ahsan", "Aijaz", "Akbar", "Aman", "Amin", "Anwar", "Asif",
        "Aslam", "Azhar", "Bilal", "Farhan", "Faiz", "Faisal", "Feroz", "Gulzar", "Hamid", "Hasan",
        "Hassan", "Husain", "Imran", "Irshad", "Irfan", "Ismail", "Jamil", "Junaid", "Kamal",
        "Kashif", "Khalid", "Luqman", "Majid", "Manzoor", "Maqbool", "Mohammad", "Mujtaba", "Muneer",
        "Nadeem", "Nashit", "Nasir", "Nazir", "Noman", "Omar", "Pervaiz", "Rafiq", "Rashid", "Rauf",
        "Rehman", "Reza", "Rizwan", "Sabir", "Said", "Salim", "Sami", "Shakeel", "Shahid", "Shakir",
        "Shaukat", "Shiraz", "Sikandar", "Sultan", "Tariq", "Tariq", "Umar", "Wasiq", "Yasir", "Zahid",
        "Zain", "Zaki", "Zarar", "Zubair", "Abdul", "Adeel", "Aftab", "Ahsan", "Akram", "Ameen",
        "Anas", "Arif", "Azam", "Bilal", "Fahad", "Farooq", "Fazil", "Ghulam", "Haroon", "Hassan",
        "Imran", "Ismail", "Jabir", "Junaid", "Kamran", "Khalil", "Muneer", "Nadeem", "Nashit",
        "Nasir", "Noman", "Omar", "Parvez", "Rafiq", "Rashid", "Rehman", "Rizwan", "Saad", "Saim",
        "Sami", "Shan", "Shahid", "Shakeel", "Shams", "Shaukat", "Shiraz", "Sikandar", "Sultan", "Tariq",
        "Ubaid", "Usman", "Yaseen", "Yusuf", "Zahoor", "Zain", "Zaki", "Zarif", "Zubair", "Abid",
        "Akhlaq", "Amit", "Azaan", "Azhar", "Bashir", "Basharat", "Danish", "Dawood", "Farhan", "Farooq",
        "Fahad", "Faisal", "Feroz", "Ghulam", "Habib", "Hakim", "Hassan", "Husain", "Imad", "Imran",
        "Irfan", "Kamil", "Kashif", "Khalid", "Luqman", "Mansoor", "Maqbool", "Mehdi", "Mirza", "Mohammad",
        "Mujtaba", "Muneer", "Nashit", "Nasir", "Noor", "Omar", "Pervaiz", "Qasim", "Rafiq", "Rashid",
        "Rehman", "Reza", "Rizwan", "Sabir", "Saeed", "Salman", "Sami", "Shakeel", "Shamsher", "Shan",
        "Shaukat", "Shiraz", "Sikandar", "Suleman", "Sultan", "Tariq", "Usman", "Wasiq", "Yasir", "Zahid",
        "Zubair", "Ziya", "Aamir", "Aftab", "Ahsan", "Arif", "Azim", "Bilal", "Fahad", "Farhan",
        "Faisal", "Feroz", "Gulzar", "Hamid", "Hassan", "Imran", "Irshad", "Irfan", "Junaid", "Kamran",
        "Kashif", "Khalid", "Muneer", "Nashit", "Nasir", "Noman", "Rafiq", "Rashid", "Rizwan", "Said",
        "Salim", "Sami", "Shahid", "Shan", "Shakeel", "Shamsher", "Shaukat", "Shiraz", "Sikandar", "Sultan",
        "Tariq", "Umar", "Yasir", "Zahid", "Zain", "Zubair", "Abdul", "Adeel", "Azhar", "Bilal",
        "Faisal", "Fahad", "Rizwan", "Hamid", "Hasan", "Irfan", "Shan", "Shakir", "Zubair", "Amin",
        "Imran", "Junaid", "Rauf", "Nasir", "Maqbool", "Shahid", "Yasir", "Khalid", "Sami", "Zaki"]


    # Muslim female First Names
    muslim_female_firstname= [
        "Aaliya", "Amina", "Asma", "Aysha", "Bushra", "Farah", "Fatima", "Hina", "Iqra", "Jameela",
        "Jamila", "Khadija", "Laila", "Mahira", "Mariam", "Muneeza", "Nadira", "Nazia", "Rashida", "Sadia",
        "Samira", "Shazia", "Sana", "Sobia", "Sultana", "Tabassum", "Yasmin", "Zahra", "Zainab", "Zoya",
        "Aisha", "Amira", "Anisa", "Fariha", "Imrana", "Kalsoom", "Lubna", "Maimuna", "Mehmooda", "Nargis",
        "Nasreen", "Ruksana", "Shahnaz", "Sumbul", "Sana", "Razia", "Riffat", "Sana", "Tahira",
        "Ayesha", "Naureen", "Farhana", "Rubina", "Zainab", "Asima", "Madiha", "Zehra", "Nazia", "Neelam",
        "Samina", "Nazia", "Safia", "Sahar", "Nilofer", "Muneera", "Shabana", "Shabnam", "Sabeen", "Rizwana",
        "Sumbul", "Meher", "Sumaiya", "Shaista", "Nazia", "Sana", "Hafsa", "Saima", "Zehra", "Alina",
        "Ahsina", "Hafsa", "Shabana", "Seema", "Kausar", "Zeenat", "Sadia", "Zakia", "Lubna", "Samina",
        "Sadia", "Sara", "Nabila", "Kiran", "Shameema", "Tabassum", "Asma", "Farida", "Sabeen", "Shabnam",
        "Mahnoor", "Rabab", "Nasreen", "Areeba", "Rubina", "Fariha", "Amina", "Zainab", "Aasia", "Nargis",
        "Saima", "Sadaf", "Shahnaz", "Mariam", "Saira", "Fozia", "Bisma", "Kiran", "Zaira", "Seher",
        "Sonia", "Tasneem", "Lubna", "Nighat", "Mehreen", "Nadia", "Asiya", "Sara", "Zara",
        "Mishal", "Tehmina", "Faryal", "Zainab", "Kausar", "Sana", "Aminah", "Nadira", "Khalida", "Iqra",
        "Rida", "Ameena", "Sumayya", "Sana", "Shiza", "Zehra", "Mubashira", "Aaliya", "Sumbul", "Tuba",
        "Rubina", "Sakina", "Meher", "Nadira", "Sana", "Amina", "Mariya", "Shakila", "Sumbul", "Rukhsana",
        "Faiza", "Madiha", "Samina", "Imrana", "Sumaiya", "Mehmooda", "Saira", "Shahla", "Sana",
        "Neelum", "Hina", "Muneera", "Ayesha", "Zahra", "Mishal", "Nabila", "Lubna", "Shabana", "Sara",
        "Tazeen", "Farzana", "Sania", "Naureen", "Shahnaz", "Shaista", "Sana", "Saniya", "Fatima", "Riffat",
        "Areeba", "Mehreen", "Samira", "Nabila", "Sanya", "Shazia", "Amina", "Saba", "Ayesha", "Mariam",
        "Tasneem", "Shireen", "Zahra", "Rubina", "Samira", "Ameenah", "Kashifa", "Sumaiya", "Faiza", "Noor",
        "Shahida", "Asma", "Sara", "Nargis", "Nida", "Noor", "Asma", "Kainat", "Mona", "Meher", "Alia",
        "Shazia", "Mariam", "Sumaira", "Muneeza", "Raheel", "Suman", "Tuba", "Afshan", "Hina", "Rana",
        "Mariam", "Mira", "Lubna", "Kausar", "Zainab", "Rizwana", "Fariha", "Farida", "Jameela", "Nashita",
        "Rafat", "Tabassum", "Sabeen", "Amena", "Alina", "Sahar", "Ahsina", "Saira", "Bisma", "Shahnaz",
        "Samia", "Meher", "Sadiqa", "Shazia", "Jamilah", "Zoya", "Saima", "Sana", "Fatima", "Azra", "Zainab",
        "Mubashira", "Shahrzad", "Shiza", "Samina", "Hina", "Ruba", "Sumaiya", "Sadiya", "Rehana", 
        "Tehmina", "Asma", "Zara", "Sushma", "Sana", "Safa", "Raheel", "Rukhsana", "Zara"]


    # Muslim Surnames
    muslim_surname= [
        "Bhat", "Mir", "Shah", "Wani", "Khan", "Dar", "Sah", "Lone", "Reshi",
        "Hassan", "Parray", "Malik", "Nabi", "Chowdhury", "Raja", "Ahmad", "Zargar", "Kawa",
        "Rather", "Dar", "Khan", "Mohiuddin", "Maqbool", "Yatoo", "Ganie", "Kundro", "Rafiq", "Jahangir",
        "Mujtaba", "Najar", "Halwai", "Fayaz", "Bukhari", "Teli", "Wahid", "Hussain", "Lodhi", "Ilyas",
        "Parray", "Rashid", "Yusuf", "Shabir", "Gulzar", "Tantray", "Akhtar", "Hamid", "Fayaz", "Khan",
        "Hassan", "Sabir", "Ganie", "Wani", "Tufail", "Khalid", "Jabeen", "Khurshid", "Rafiq", "Shafi",
        "Nazir", "Amin", "Umar", "Ashraf", "Bashir", "Syed", "Khursheed", "Sayeed", "Shah", "Haider",
        "Qureshi", "Rana", "Abdullah", "Shamim", "Ahmad", "Maqsood", "Shahbaz", "Akhtar", "Raza", "Mudasir",
        "Bashir", "Waza", "Tariq", "Qazi", "Kamil", "Wani", "Dawood", "Saleem", "Noor", "Mehraj",
        "Abdullah", "Hassan", "Ahmad", "Zahid", "Imran", "Khaliq", "Nasir", "Qamar", "Nashit", "Rizwan",
        "Tanveer", "Sajid", "Khatana", "Mohammad", "Abbas", "Tariq", "Sattar", "Saeed", "Syed", "Hamza"]
    
# Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Helper function to generate names
    def generate_religious_names(count, firstnames, surnames, gender):
        for _ in range(count):
            first_name = random.choice(firstnames)
            surname = random.choice(surnames)
            if preferences.get('name_type') == 'first':
                names.append((first_name, gender))
            else:
                names.append((f"{first_name} {surname}", gender))

    # Divide counts equally for all religions and genders
    religion_count = n // 6
    remaining = n % 6

    # Generate male names
    generate_religious_names(religion_count, kashmiri_pandit_male_firstname, kashmiri_pandit_surname, "Male")
    generate_religious_names(religion_count, ladakh_male_firstname, ladakh_surname, "Male")
    generate_religious_names(religion_count + remaining, muslim_male_firstname, muslim_surname, "Male")

    # Generate female names
    generate_religious_names(religion_count, kashmiri_pandit_female_firstname, kashmiri_pandit_surname, "Female")
    generate_religious_names(religion_count, ladakh_female_firstname, ladakh_surname, "Female")
    generate_religious_names(religion_count, muslim_female_firstname, muslim_surname, "Female")

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_jk_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df
