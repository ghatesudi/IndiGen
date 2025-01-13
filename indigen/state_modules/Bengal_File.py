import pandas as pd
import os
import random

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_bengal_names(n, user_preference=None):

    # Westbengal Male First Names
    bengali_male_firstname= [
        "Abhijit", "Amit", "Arindam", "Anirban", "Arnab", "Ashok", "Avik", "Babul", "Bappa", "Biswajit",
        "Bikram", "Bikas", "Bhabani", "Chandan", "Chandran", "Chirodeep", "Chirantan", "Debabrata", "Debasis", "Dinesh",
        "Dipankar", "Durjoy", "Debojyoti", "Dhiman", "Gautam", "Gourav", "Goutam", "Gokul", "Haran", "Hiran",
        "Hemanta", "Hemendra", "Joydeep", "Jitendra", "Jishu", "Kalyan", "Kamal", "Kartik", "Kunal", "Kishore",
        "Krishnendu", "Laltu", "Lakshman", "Madhusree", "Manoj", "Mahesh", "Mayukh", "Manish", "Mantu",
        "Monojit", "Monirul", "Mukul", "Murari", "Nabin", "Narayan", "Nirmal", "Nitesh", "Nikhil", "Niloy",
        "Partha", "Pranab", "Pritam", "Prosenjit", "Pradip", "Parthasarthi", "Probal", "Rajat", "Rakesh", "Ranjan",
        "Ratan", "Rajib", "Rajesh", "Rajiv", "Ramesh", "Riddhiman", "Rishabh", "Robi", "Rudra", "Rupal",
        "Sabyasachi", "Sandeep", "Sankar", "Sanjib", "Santanu", "Shakti", "Subir", "Subhasis", "Suman", "Sudipta",
        "Sumit", "Sunil", "Sujoy", "Sushant", "Sourav", "Shubho", "Somnath", "Subhendu", "Shovan", "Sudhakar",
        "Tarak", "Tapas", "Tapan", "Tanmay", "Tridib", "Tarun", "Utpal", "Ujjal", "Umesh", "Utpal",
        "Uttam", "Vikram", "Vikas", "Vishal", "Vivek", "Yuvraj", "Arun", "Ashutosh", "Basudeb", "Baidyanath",
        "Bijoy", "Bidhan", "Biswajeet", "Bodhisattva", "Banshidhar", "Chandrakant", "Chakrapani", "Dhritiman", "Dharmendra", "Deepak",
        "Dwijendra", "Devendra", "Dilip", "Dilip", "Debarshi", "Ganesh", "Gautam", 
        "Hari", "Himadri", "Hemant", "Hitesh", "Indranil", "Ishaan", "Jitendra ", "Jiban", "Jayanta", "Jishu Sengupta",
        "Kanchan", "Koushik", "Kamalakar", "Lajpat", "Lalan", "Mandar", "Manindra", "Mayank", "Monoj", "Nabarun",
        "Nandan", "Narendranath", "Neel", "Nikhil ", "Pankaj", "Param", "Parth", "Pranay", "Prabhat", "Pritish",
        "Pradeep", "Probir", "Rajib ", "Rajarshi", "Rameswar", "Rajendranath", "Raj", "Rishan", "Rohit", "Ratanlal",
        "Rahul", "Sandip", "Subir", "Suvam", "Subhankar", "Santosh", "Sudhir", "Samir", "Samarjit", "Suprakash",
        "Shuvra", "Shyamal", "Sushil", "Sanjoy", "Shankar", "Somendra", "Shubham", "Subrata", "Suraj", "Tridipta",
        "Tapash", "Tanmay ", "Tirthankar", "Trinanjan", "Tapan ", "Uttam ", "Utpal ", "Venkatesh", "Vibhor", "Vishwanath",
        "Vignesh", "Vijay", "Yash", "Animesh", "Asit", "Biswajit ", "Biplab", "Chandan ", "Charan", "Dhruba",
        "Dinesh ", "Dipanjan", "Dipto", "Diptesh", "Devansh", "Gaurav ", "Gaurang", "Hiranmay", "Hemraj", "Iqbal",
        "Jaydev", "Joyesh", "Kalyan ", "Kamaluddin", "Kashi", "Koushik Das", "Krishan", "Krishnendra", "Mahindra", "Maitreya",
        "Manindra ", "Manoj ", "Mayur", "Mohan", "Moloy", "Nayan", "Nirmal ", "Nitai", "Pritesh", "Pratik",
        "Prithviraj", "Radhakrishnan", "Rajat ", "Rajit", "Rajiv ", "Rajendra ", "Rahul ", "Rishav", "Ranjit ", "Samiran",
        "Shaktibrata", "Sharmistha", "Sanyog", "Sankalp", "Sanjoy ", "Shashi", "Shivendra", "Subhankar ", "Soumik", "Sourav ",
        "Sudipta ", "Subir ", "Somnath ", "Sudhir ", "Suman", "Sushant", "Sumantra", "Subhojit", "Subrata ", "Swapan",
        "Sujit", "Swarnendu", "Tanmoy", "Tarun ", "Tanmay", "Trinath", "Utpal ", "Vivekananda", "Vinoj", "Vishwanath ",
        "Vimal", "Vipin", "Yashpal", "Zeeshan", "Zahir", "Amarendra", "Ashish", "Aniruddha", "Amitabh", "Arijit"]
    # Westbengal Female First Names
    bengali_female_firstname = [
        'Hemlata', 'Pratyusha', 'Anjali', 'Tanika', 'Sayantani', 'Rachita', 'Dipta', 'Trishti', 'Kavita', 'Priyadarshini', 'Sweta', 
        'Sharanya', 'Tanya', 'Geetanjali', 'Radhika', 'Sahana', 'Madhumita', 'Laxmi', 'Lalita', 'Bijoya', 'Nikita', 'Ranjana', 'Sree', 
        'Sandhya', 'Santoshi', 'Sanjana', 'Dipa', 'Kanak', 'Suparna', 'Barsha', 'Aditi', 'Sucharita', 'Nisha', 'Ratna', 'Ankita', 'Nandini', 
        'Arpita', 'Kalpana', 'Sreeja', 'Shyamali', 'Sreyashi', 'Chandita', 'Tanu', 'Sneha', 'Pritha', 'Varsha', 'Kanchan', 'Charu', 'Deepa', 
        'Soumi', 'Maitri', 'Priyanka', 'Rajul', 'Sukanya', 'Tasmia', 'Sharmila', 'Shubhi', 'Manju', 'Amrita', 'Kamalini', 'Kumudini', 'Rishika', 
        'Sreya', 'Tina', 'Purnima', 'Madhavi', 'Pooja', 'Sarayu', 'Mandira', 'Ananya', 'Vandana', 'Tanuja', 'Bhaswati', 'Satarupa', 'Tanushree', 
        'Bipasa', 'Srishti', 'Anushka', 'Koyel', 'Chaitali', 'Rupa', 'Swagata', 'Madhusree', 'Kamalika', 'Nabanita', 'Ushashi', 'Sharika', 
        'Suchismita', 'Subhasree', 'Rima', 'Amita', 'Chandrika', 'Jyoti', 'Dhanashree', 'Kamini', 'Kiran', 'Shikha', 'Kunjalata', 'Sumathi', 
        'Pratibha', 'Nivriti', 'Sudipta', 'Koushani', 'Rupali', 'Tanusree', 'Manasi', 'Sabrina', 'Sanjukta', 'Amiti', 'Sachi', 'Rekha', 
        'Supriya', 'Ritika', 'Avni', 'Kalyani', 'Moumita', 'Nishita', 'Smita', 'Subhika', 'Pallavi', 'Vishaka', 'Trina', 'Rimpa', 'Bipasha', 
        'Mitali', 'Gargee', 'Tithi', 'Neelima', 'Nutan', 'Sibani', 'Urmila', 'Sangita', 'Isha', 'Aparna', 'Bikashita', 'Esha', 'Kanchana', 
        'Sounakshi', 'Anwesha', 'Madhubala', 'Meher', 'Rina', 'Rupal', 'Madhulika', 'Upama', 'Samarita', 'Subrina', 'Sridhi', 'Sampa', 
        'Sakshi', 'Nandita', 'Snehalata', 'Subhita', 'Shobha', 'Durga', 'Suman', 'Rupkatha', 'Sushmita', 'Charulata', 'Madhuri', 'Mira', 
        'Nivedita', 'Karishma', 'Chitra', 'Pinky', 'Yamini', 'Sujata', 'Chandini', 'Sunita', 'Indira', 'Anjushree', 'Sathi', 'Anju', 
        'Rukmini', 'Sharani', 'Lopa', 'Tuhina', 'Tumpa', 'Rini', 'Sadhana', 'Madhabi', 'Debarati', 'Pragati', 'Mousumi', 'Medha', 'Arohi', 
        'Rupsha', 'Sharmistha', 'Sarika', 'Vidya', 'Bani', 'Shreya', 'Baisakhi', 'Meera', 'Debika', 'Bhawna', 'Shubhra', 'Ujjani', 'Namita', 
        'Upasana', 'Gitanjali', 'Gargi', 'Sampurna', 'Bidisha', 'Jaya', 'Sanjita', 'Swarna', 'Shoma', 'Anjoli', 'Suma', 'Sonali', 'Chandra', 
        'Sumita', 'Mina', 'Soma', 'Srabani', 'Kanta', 'Monika', 'Vasundhara', 'Maya', 'Priya', 'Indrani', 'Chandana', 'Ujjwala', 'Debjani', 
        'Teesta', 'Anamika', 'Manisha', 'Suchita', 'Sarita', 'Archana', 'Dipti', 'Suravi', 'Shivani', 'Tanvi', 'Bithika', 'Ranjita', 'Madhura', 
        'Riya', 'Sampad']
    bengali_surname = [ 
        "Chakraborty", "Banerjee", "Das", "Sengupta", "Ghosh", "Dutta", "Chatterjee", "Mukherjee", "Roy", "Bhattacharya",
        "Mitra", "Paul", "Saha", "Bhattacharjee", "Nandy", "Ganguly", "Majumdar", "Kundu", "Basu", "Chowdhury",
        "Kar", "Bhaduri", "Dey", "Mitra", "Ray", "Karmakar", "Bhowmik", "Banik", "Madhusree", "Sanyal",
        "Rath", "Mandal", "Pal", "Ghoshal", "Adhikary", "Banik", "Sengupta", "Chakrabarti", "Rai", "Singh",
        "Bhuiyan", "Halder", "Bose", "Sinha", "Pramanik", "Dasgupta", "Hossain", "Majumdar", "Naskar", "Chatterji",
        "Mazumder", "Sanyal", "Ganguly", "Haldar", "Tiwari", "Bhuiyan", "Bhaduri", "Dasgupta", "Sen", "Patra",
        "Pramanik", "Barman", "Mukherji", "Nath", "Sharma", "Kumar", "Karmakar", "Raychaudhuri", "Dey", "Goswami",
        "Dhar", "Roychowdhury", "Poddar", "Chakrabarty", "Sanyal", "Baidya", "Basu", "Mondal", "Dasgupta", "Bandyopadhyay",
        "Kundu", "Haldar", "Das", "Nayak", "Mahato", "Naskar", "Chowdhuri", "Banerjee", "Khatun", "Mallick",
        "Mondal", "Chatterjee", "Singha", "Shaha", "Ray", "Sinha", "Choudhury", "Bhowmick", "Poddar", "Ghosal",
        "Agarwal", "Tiwari", "Roy", "Ganguly", "Pattnaik", "Saha", "Kundu", "Mukherjee", "Bhattacharya", "Mukherjee",
        "Shome", "Saha", "Bose", "Ganguly", "Bandyopadhyay", "Kar", "Routh", "Mitra", "Ghosal", "Bose",
        "Mahalder", "Agarwal", "Sharma", "Sen", "Jana", "Chowdhury", "Ghosh", "Borah", "Patra", "Bhuyan",
        "Karmakar", "Jha", "Pal", "Ghoshal", "Hussain", "Mundal", "Banerji", "Das", "Sarkar", "Haldar",
        "Mishra", "Borgohain", "Pramanik", "Bardhan", "Bhattacharya", "Saha", "Kishore", "Banerjee", "Saha",
        "Mitra", "Nayak", "Chowdhuri", "Das", "Sharma", "Maitra", "Kumar", "Bhattacharyya", "Dutta", "Sen",
        "Chatterjee", "Adhikary", "Mukhopadhyay", "Bose", "Shaha", "Patel", "Sen", "Sengupta", "Bhaumik",
        "Kundu", "Poddar", "Patra", "Ghosh", "Bandyopadhyay", "Naskar", "Das", "Barman", "Sanyal", "Majumder",
        "Pramanik", "Goswami", "Ganguly", "Bhuiyan", "Mukherjee", "Chatterjee", "Mondal", "Dutta", "Chakrabarty",
        "Sanyal", "Ray", "Sen", "Chakraborty", "Saha", "Sarkar", "Ghosal", "Banerjee", "Patel", "Bhuiyan",
        "Kumar", "Das", "Sarkar", "Sharma", "Singh", "Mitra", "Chowdhury", "Madhusree", "Rath", "Bose"]
    # Initialize user preferences
    preferences = init(user_preference)
    # Create a list to store names and their genders
    names = []
    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(bengali_male_firstname)
        last_name_male = random.choice(bengali_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(bengali_female_firstname)
        last_name_female = random.choice(bengali_surname)

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
    file_path = 'generated_bengal_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df