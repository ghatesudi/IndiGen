import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_tripura_names(n, user_preference=None):

    # tripura Male First Names
    tripura_male_firstname = [
        "Abhijit", "Anirban", "Arup", "Biplab", "Biswajit", "Birendra", "Chandan", "Chandrakanta", "Dinesh", "Debojit", "Deepak",
        "Dilip", "Ganesh", "Gopal", "Gobinda", "Harish", "Himanshu", "Hira", "Indrajit", "Indra", "Kamal", "Kalyan", "Kanchan",
        "Kailash", "Laxman", "Loknath", "Manik", "Manish", "Madhusree", "Mohan", "Mantu", "Mangal", "Mithun", "Nirmal", "Nayan",
        "Narendra", "Nitai", "Pritam", "Purna", "Pranab", "Rajkumar", "Rajib", "Rajendra", "Ranjit", "Ratan", "Rupesh", "Rakesh",
        "Roshan", "Ramakant", "Shyam", "Somnath", "Suraj", "Santosh", "Sunil", "Suresh", "Shankar", "Shubham", "Subhendu", "Siddharth",
        "Subhash", "Surendra", "Tarun", "Tanmoy", "Uday", "Ujjal", "Utpal", "Vikash", "Vishal", "Vipul", "Vikas", "Ajay", "Arjun",
        "Binoy", "Bishal", "Bimal", "Dipankar", "Goutam", "Jagat", "Jitendra", "Jagdish", "Jibon", "Keshab", "Krishan", "Lokenath",
        "Mahendra", "Mohit", "Manoranjan", "Munindra", "Narayan", "Pankaj", "Prasanta", "Pradeep", "Purnendu", "Raghunath", "Samarendra",
        "Subrata", "Suryakant", "Tushar", "Ujjwal", "Aabir", "Aakash", "Abhinav", "Adhir", "Advit", "Ajoy", "Akash", "Alok", "Animesh",
        "Anindya", "Arindam", "Arvind", "Asit", "Ashoke", "Atin", "Avinash", "Banesh", "Bandhan", "Barun", "Bikash", "Bipin", "Brij",
        "Chaitanya", "Chandranath", "Charan", "Chintan", "Dipak", "Diptanshu", "Dhruba", "Dipendra", "Durgesh", "Gaurav", "Gokul",
        "Gour", "Harendra", "Hemant", "Himadri", "Indranil", "Iqbal", "Ishwar", "Jadav", "Jagadish", "Jagannath", "Jayanth", "Jayanta",
        "Kamini", "Kanishk", "Kedar", "Kiran", "Krishnan", "Kumar", "Lokesh", "Manindra", "Mukesh", "Mitesh", "Nandini", "Nilay",
        "Niraj", "Nirupam", "Partha", "Rajat", "Rajeev", "Raghav", "Rakhal", "Ranjan", "Ranveer", "Revanth", "Ritesh", "Rituparno",
        "Raghavendra", "Ramesh", "Ramanuj", "Rajan", "Rahul", "Rishabh", "Satyendra", "Shibnath", "Shib", "Shyamal", "Shouvik", "Shubho",
        "Subhasish", "Sudhir", "Sumit", "Sushil", "Swarup", "Tanay", "Tapan", "Tapas", "Tirtha", "Tridib", "Vishnu", "Vidyut", "Vinay",
        "Vivek", "Vishwanath", "Bishnu", "Babu", "Banshi", "Barindra", "Brijesh", "Bipul", "Bidyut", "Bansidhar", "Budhiman",
        "Chandrakant", "Chakrapani", "Chiranjeev", "Dhiman", "Darshan", "Dushyant", "Dineshwar", "Dwarakanath", "Gajendra", "Gopendra",
        "Gorakh", "Gouri", "Haldhar", "Haran", "Harvinder", "Hirak", "Hiran", "Indranath", "Indrajeet", "Jagannatha", "Jayanand", "Jash",
        "Jivendra", "Jeet", "Kalicharan", "Kamalkant", "Kanak", "Kashi", "Kiritesh", "Kirit", "Kishor", "Kripesh", "Krishnachandra",
        "Krishnendu", "Lakshminarayan", "Mahabir", "Manab", "Manmohan", "Mahesh", "Mukul", "Monojit", "Narinder", "Nimai", "Neel",
        "Pramod", "Purnachandra", "Piyush", "Praful", "Pratik", "Prashant", "Rajanikanth", "Rameshwar", "Ranadeep", "Rohit", "Sandeep",
        "Saroj", "Shourya", "Sharad", "Suman", "Sumant", "Subhayan", "Shibendra", "Sankar", "Samir", "Tamal", "Tathagata", "Tarak",
        "Tanmay", "Ujjawal", "Uttam", "Vasant", "Vijay", "Yashoda"]

    # tripura surnames
    tripura_surname = [
        "Tripura", "Chakma", "Noatia", "Jamatia", "Rakhine", "Mog", "Thakur", "Debbarma", "Manik", "Reang", "Kar", "Saha",
        "Roy", "Barma", "Majumdar", "Dey", "Talukdar", "Bhattacharya", "Tripathi", "Banik", "Das", "Manna", "Pramanik", "Shil",
        "Debnath", "Paul", "Majumder", "Bhowmick", "Sutradhar", "Dutta", "Mollah", "Choudhury", "Barman", "Chakraborty", "Sen",
        "Basak", "Saha", "Barai", "Bhattacharya", "Thakur", "Roychoudhury", "Karle", "Nag", "Rani", "Singha", "Dasgupta",
        "Chowdhury", "Soren", "Bhattacharjee", "Mahato"]



    # tripura Female First Names
    tripura_female_firstname =  [ 
        "Aditi", "Anjali", "Biswajit", "Chanu", "Chameli", "Dipa", "Hira", "Kumari", "Khyati", "Jhuma", "Joya", "Jhumka", "Jibonika", "Laxmi", "Maloti", "Mitali", "Mandira",
        "Monika", "Nayana", "Rina", "Rajbari", "Ranjana", "Rima", "Rupa", "Shanti", "Subhasree", "Purnima", "Sandhya", "Sanjukta", "Sitara", "Soma", "Swapna", "Tumpa", "Tripti",
        "Utpalini", "Rekha", "Nirmala", "Bindu", "Anita", "Bina", "Pritam", "Sonali", "Kamala", "Nandini", "Kirti", "Asha", "Manju", "Titi", "Saraswati", "Aabha", "Antara",
        "Aparna", "Arpita", "Basanti", "Bithika", "Bishnupriya", "Bijoya", "Chaitali", "Charulata", "Chhaya", "Chhobi", "Chandana", "Chandrika", "Debjani", "Damini", "Dipti",
        "Durga", "Elina", "Indira", "Indrani", "Jaya", "Janaki", "Jhumur", "Jyotika", "Kamini", "Kalyani", "Kalpana", "Karuna", "Kiran", "Kuntala", "Lopamudra", "Manasi",
        "Manjari", "Malini", "Maitreyee", "Medha", "Monalisa", "Mrinalini", "Moushumi", "Nirupa", "Padma", "Padmini", "Parul", "Pritha", "Pranjal", "Radhika", "Rajeshwari",
        "Ratna", "Ruchi", "Sarojini", "Sharmila", "Shashi", "Shobha", "Sushmita", "Sudha", "Sumana", "Sujata", "Suman", "Swati", "Tanima", "Tanuja", "Tithi", "Trina", "Upasana",
        "Urmila", "Usha", "Uttara", "Vidhatri", "Vina", "Vidya", "Yashoda", "Amita", "Ananya", "Bidisha", "Bhavana", "Charusheela", "Chandrima", "Chintana", "Dayita", "Deepika",
        "Girija", "Gitali", "Haimanti", "Hridaya", "Jahnavi", "Kumudini", "Kunjalata", "Laili", "Lata", "Madhuri", "Malabika", "Mita", "Mithila", "Mohini", "Monisha", "Parvati",
        "Pritilata", "Rajlakshmi", "Rukmini", "Rati", "Renuka", "Shibani", "Sharika", "Sharmistha", "Sharini", "Shukla", "Sushma", "Sita", "Sumita", "Swarnalata", "Subhra",
        "Sarika", "Susmita", "Tamalika", "Trishala", "Urmi", "Ujjwala", "Vibha", "Aishwarya", "Alaka", "Alpana", "Arati", "Abhaya", "Aparajita", "Bandana", "Bharati", "Bhavani",
        "Bhaswati", "Bibha", "Chandra", "Chandini", "Dipali", "Kusum", "Madhubala", "Nivedita", "Prabha", "Pratima", "Rajani", "Rakhi", "Ritu", "Ruma", "Sadhana", "Sukanya",
        "Sumanita", "Shubhra", "Shabari", "Shilpi", "Tanvi", "Trishna","Ushashi", "Varsha", "Vijaya", "Anima", "Amrita", "Asmita", "Barsha", "Barnali", "Brishti", "Charushila",
        "Diti", "Gargee", "Goutami", "Kanti", "Lajja", "Manisha" ]  
    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(tripura_male_firstname)
        last_name_male = random.choice(tripura_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(tripura_female_firstname)
        last_name_female = random.choice(tripura_surname)

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
    file_path = 'generated_tripura_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df