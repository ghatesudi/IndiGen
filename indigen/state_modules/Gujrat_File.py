import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Gujarat Male and Female First Names and Surnames
def generate_gujrat_names(n, user_preference=None):
    # gurjat Male First Names
    gujrati_male_firstname = [
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
        'Balwant', 'Anand', 'Naresh', 'Bhubaram', 'Sandeep', 'Mahendra', 'Ganpat', 'Chintan', 'Mohanlal', 'Anmol', 'Vishal', 'Sanjay ', 'Veer', 'Gurdeep', 'Harvinder', 
        'Bhavesh', 'Bhanupratap', 'Bhagat', 'Kushal', 'Jagdish', 'Balaram', 'Shyam', 'Udayveer', 'Ramesh', 'Vijendra', 'Laxminarayan', 'Rajveer', 'Rajvinder', 'Chandra', 
        'Vikrant', 'Shivraj', 'Ishwar', 'Vinayak', 'Balkishan', 'Jitendra', 'Kailas', 'Narendra', 'Rameshwar', 'Mahesh', 'Kailash', 'Chandrapal', 'Rajendra Pratap', 'Jeevan', 
        'Tej', 'Ashish', 'Nirmal', 'Ashok', 'Arjun Singh', 'Premendra', 'Manvendra', 'Rajkumar', 'Sarvagya', 'Arjit', 'Manoj', 'Lokesh', 'Saurabh', 'Amit', 'Abhishek', 'Naveen', 
        'Shashank', 'Ajay', 'Pintu', 'Kishore', 'Subhash', 'Karanveer', 'Rishabh', 'Rajvendra', 'Shakti', 'Vir', 'Suryanarayan', 'Yashvardhan', 'Vishwajeet', 'Sunil', 
        'Surendra', 'Vishvesh', 'Prabhu', 'Ashesh', 'Chandreshwar', 'Swarup', 'Jagdeep', 'Krishna', 'Nitesh', 'Bhupender', 'Sahdev', 'Pramod', 'Shamsher', 'Pawan', 
        'Rajiv', 'Harsh', 'Omprakash', 'Dilip', 'Rajender', 'Jagat', 'Hari', 'Ansh', 'Anil', 'Chandresh', 'Madhusudan', 'Raghavendra', 'Uday', 'Jodh', 'Mukul', 
        'Nikhil', 'Brij', 'Bheem', 'Rana', 'Hemraj', 'Gaurav', 'Ambarish', 'Raju', 'Ratan', 'Dhanraj', 'Raghunath Singh', 'Vikram', 'Kamal', 'Lalit', 'Pankaj', 
        'Radheshyam', 'Tejendra', 'Girdhar', 'Chandrasen', 'Ladu', 'Gajendra', 'Satish', 'Kanak', 'Harishankar', 'Nitin', 'Vikramjit', 'Satyam', 'Sonu', 'Kishor', 
        'Suraj', 'Ravindra Singh', 'Chandrashekhar', 'Kesar', 'Prakash', 'Tejpal Singh', 'Balkrishna', 'Prathmesh', 'Bhanuprasad', 'Madan', 'Shankar', 'Ashok Kumar', 
        'Yash', 'Shailendra', 'Manish', 'Maan', 'Bhavar', 'Abhay', 'Ranjit', 'Suman', 'Chirag', 'Rajnish', 'Pravin', 'Shatrunjay', 'Chandran', 'Dharmendra', 'Karamveer', 
        'Vijay', 'Prem', 'Prabhakar', 'Shravan', 'Anwar', 'Udai', 'Surender', 'Rajkumar Singh', 'Ranvijay', 'Pradeep', 'Aniruddh', 'Rajat', 'Mahipal', 'Amardeep', 'Pratap', 'Tulsiram', 
        'Bhupendra', 'Gulab', 'Tejveer', 'Bhim', 'Harishchandra', 'Rakesh', 'Aarav', 'Krish', 'Girish', 'Chhagan', 'Narayan', 'Vikramaditya', 'Manmohan', 'Ramkishan', 'Balvir', 'Vinod', 
        'Rajaram', 'Raghbir', 'Chetan', 'Tanmay', 'Chiranjeev', 'Vikas', 'Vinay',
        "Vallabh", "Harish", "Bhavesh", "Jignesh", "Milan", "Madhav", "Shyam", "Rakesh", "Tushar", "Sandeep",
        "Jai", "Nirmal", "Chintan", "Madhusudan", "Raghav", "Vijay", "Bhaskar", "Bhim", "Rajesh", "Arvind",
        "Ashish", "Prakash", "Nirav", "Ujjwal", "Mahesh", "Vishal", "Jatin", "Siddharth", "Kiran", "Dinesh",
        "Bharat", "Vijay", "Rajendra", "Ketan", "Hitesh", "Amit", "Sanjay", "Manish", "Hardik", "Kunal",
        "Anand", "Girish", "Raghunath", "Ramesh", "Chandresh", "Vishnu", "Nilesh", "Harsh", "Manoj", "Vishwajeet",
        "Pravin", "Devendra", "Suryakant", "Kirit", "Amitabh", "Shubham", "Harit", "Ashok", "Sandeep", "Jayshree",
        "Ravindra", "Dinesh", "Vishal", "Bhanu", "Mahendra", "Ganesh", "Lalji", "Chandra", "Nathu", "Ramesh",
        "Narendra", "Amit", "Manoj", "Paresh", "Vikram", "Ranjit", "Dev", "Kishore", "Raj", "Jitendra",
        "Shatrughan", "Gulshan", "Akshay", "Sachin", "Amitabh", "Ravi", "Harbhajan", "Shah", "Bhavik", "Ravi",
        "Govind", "Bhavesh", "Kailash", "Jayant", "Bhaumik", "Gaurav", "Yash", "Parth", "Krishna", "Viral",
        "Rohit", "Vivek", "Sumit", "Hardik", "Kartik", "Jatin", "Tejas", "Madhur", "Vipul", "Chirag",
        "Abhishek", "Aman", "Saurabh", "Rishabh", "Shubham", "Aayush", "Siddharth", "Anshul", "Gyanendra", "Sahil",
        "Ritesh", "Punit", "Nitin", "Harshil", "Ruchir", "Niraj", "Shubhit", "Nihal", "Arjun", "Rahul",
        "Chirag", "Krish", "Suraj", "Alok", "Ravip", "Yogesh", "Chaitanya", "Raghavendra", "Manav", "Tushar",
        "Ashwin", "Hemanth", "Nandan", "Ajay", "Bhavya", "Mohan", "Chirag", "Samarth", "Tarun", "Vatsal",
        "Zahid", "Manav", "Tushar", "Milan", "Nikhil", "Sumit", "Mitesh", "Mehul", "Rupal", "Vipul",
        "Amitesh", "Shaan", "Chirag", "Umesh", "Nandkishore", "Brijesh", "Naveen", "Shivendra", "Ravindra", "Harish",
        "Yogendra", "Gajendra", "Ashok", "Ravindra", "Pravin", "Raghunath", "Babulal", "Chintan", "Virendra", "Tejal",
        "Ajay", "Pankaj", "Ajit", "Devendra", "Shankar", "Ravindra", "Madhav", "Vasudev", "Jai", "Rajendra"]

    # gurjat Male Surnames
    gujrati_male_surname = [
        "Patel", "Shah", "Bavani", "Vora", "Joshi", "Parikh", "Mehta", "Chaudhary", "Trivedi", "Pandya",
        "Sharma", "Dixit", "Mishra", "Purohit", "Joshi", "Chauhan", "Rathod", "Thakur", "Yadav", "Brahmbhatt",
        "Soni", "Bavishi", "Jani", "Chandran", "Raval", "Prajapati", "Desai", "Rajput", "Shukla", "Thakkar",
        "Patel", "Makwana", "Chavda", "Mistry", "Rana", "Vaghela", "Barai", "Raj", "Khant", "Prajapati",
        "Shukla", "Tiwari", "Pandey", "Vishwakarma", "Upadhyay", "Brahmbhatt", "Chaudhary", "Sharma", "Pandya", "Saraswat",
        "Rathod", "Chauhan", "Raval", "Rajput", "Solanki", "Deshmukh", "Vaghela", "Singh", "Shah", "Sengar",
        "Bhil", "Warli", "Gamit", "Rathwa", "Sabar", "Sodha", "Dubla", "Lohana", "Rathva",
        "Modi", "Patel", "Gandhi", "Thackeray", "Ambani", "Agarwal", "Shah", "Rupani", "Bajpai", "Hirani",
        "Desai", "Bachchan", "Sharma", "Kumar", "Nanda", "Bedi", "Mehta",
        "Prabhu", "Singh", "Pandya", "Soni", "Joshi", "Kailash", "Gandhi", "Nair", "Jain", "Dhar",
        "Naik", "Siddiqui", "Sarabhai", "Patel", "Thakkar", "Tiwari", "Lohar", "Kundra", "Hirani", "Mehta",
        "Rathi", "Bhat", "Parmar", "Bhagat", "Sharma", "Kumawat", "Soni", "Singh", "Verma", "Yadav",
        "Ravani", "Solanki", "Soni", "Goswami", "Sheth", "Patel", "Vankar", "Bava", "Vora", "Nayak",
        "Khunt", "Mevani", "Jogi", "Gandhi", "Vasava", "Rajgor", "Panjwani", "Modh", "Vaniya", "Khatri",
        "Sanghvi", "Upadhyay", "Panchal", "Bansal", "Thaker", "Vekariya", "Kothari", "Raval", "Mistry",
        "Parmar", "Goyani", "Bhavsar", "Nadkarni", "Kalani", "Patel", "Agarwal", "Sanghvi", "Jain",
        "Deshmukh", "Surani", "Soni", "Gokani", "Sarvani", "Vakharia", "Vaswani", 
        "Bansal", "Kothari", "Wala", "Dholakia", "Tiwari", "Maru", "Bharadwaj", "Sura",
        "Bachchani", "Dixit", "Vaghela", "Jadhav", "Gokul", "Mehta", "Tewari", "Vadera", "Rathod",
        "Vasani", "Khushwaha", "Chandra", "Nadgouda", "Pate", "Vanka", "Nair", "Panchal", "Vahora",
        "Chaudhary", "Jasani", "Patil", "Kumar", "Sodha", "Sarma", "Mishra", "Chawla", "Raval",
        "Rathi", "Rana", "Suthar", "Kavedia", "Singh", "Varma", "Kale", "Soni", "Mavani", "Desai",
        "Gokhani", "Jariwala", "Rupani", "Chandran", "Nayak", "Jadeja", "Kali", "Zaveri", "Hirji",
        "Wagh", "Patil", "Shah", "Mistry", "Jeevraj", "Bhagat", "Sangvi", "Nagori", "Pujara", "Lad",
        "Kambhoj", "Singhvi", "Thakor", "Sodhi", "Khariwala", "Jindal", "Bajpai", "Ruparelia", "Bansal",
        "Kapadia", "Tiwari", "Mathur", "Bhimani", "Gupta", "Vora", "Vaghela", "Solanki", "Dewani",
        "Sivach", "Patwari", "Soni", "Vaghani", "Vasava", "Makwana", "Panwala", "Raval", "Sarvaiya"
    ]


    # gurjat Male Suffix
    gujrati_male_suffix = ["bhai","","",""]


    # gurjat Female First Names
    gujrati_female_firstname = names = [
        "Radha", "Laxmi", "Madhavi", "Vandana", "Pooja", "Nisha", "Bhakti", "Seema", "Janki", "Rupal",
        "Durga", "Savitri", "Anjali", "Sita", "Priya", "Bharati", "Kajal", "Manju", "Ranjana", "Sunita",
        "Jasmine", "Trupti", "Aishwarya", "Snehal", "Kavita", "Dipika", "Swati", "Shubhi", "Nirali", "Sonali",
        "Shalini", "Rupal", "Deepika", "Ashwini", "Harini", "Sangeeta", "Radhika", "Meenal", "Kiran", "Kanchan",
        "Komal", "Anita", "Neha", "Ritika", "Simran", "Pranjal", "Ankita", "Khushbu", "Ruchi", "Sonal",
        "Rina", "Chandni", "Tanuja", "Neetu", "Leela", "Narmada", "Sita", "Gulab", "Bharti", "Chandrika",
        "Indira", "Sonia", "Narmada", "Poonam", "Rupal", "Kajal", "Tina", "Rita", "Swati", "Meher",
        "Hema", "Sakshi", "Parul", "Rekha", "Vidya", "Aishwarya", "Madhuri", "Karishma", "Kajol", "Deepika",
        "Kangana", "Priyanka", "Madhavi", "Rani", "Jaya", "Kriti", "Shraddha", "Chitrangada",
        "Manisha", "Lata", "Kiran", "Sushmita", "Radhika", "Bhavini", "Sonal", "Dipika", "Pranjali", "Shubhi",
        "Vandana", "Anjali", "Neelam", "Simran", "Aarti", "Tejal", "Pooja", "Rupal", "Swati", "Harini",
        "Rina", "Nisha", "Divya", "Madhavi", "Ashwini", "Madhuri", "Alka", "Vandana", "Priti", "Manju",
        "Tanu", "Shilpa", "Rupal", "Sonali", "Mansi", "Radhika", "Madhuri", "Rupal", "Nutan", "Bhakti",
        "Tina", "Kajal", "Gargi", "Hina", "Meenal", "Kanchan", "Ritika", "Snehal", "Kavita", "Bharati",
        "Pooja", "Dipika", "Ruchi", "Disha", "Aarti", "Komal", "Aishwarya", "Poonam", "Tanuja", "Shubhi",
        "Sakshi", "Chandrika", "Pranjal", "Shruti", "Leela", "Tina", "Rama", "Soniya", "Meenal", "Kiran",
        "Narmada", "Yashoda", "Aishwarya", "Sonia", "Priti", "Sushmita", "Ankita", "Sangeeta", "Rupal", "Sonal",
        "Sujata", "Kumud", "Savitri", "Shalini", "Swati", "Shubhi", "Nita", "Rita", "Kanchan", "Sumitra",
        "Sundari", "Manju", "Krishna", "Naina", "Tina", "Rekha", "Ravi", "Sarika", "Bhoomi", "Rupali",
        "Shilpa", "Jayshree", "Khushboo", "Tanvi", "Madhavi", "Kiran", "Alka", "Neeti", "Rupal", "Soniya",
        "Aarti", "Chandini", "Nirali", "Tejal", "Parul", "Snehal", "Reena", "Ritika", "Geeta", "Ravi",
        "Rama", "Ruchi", "Vatsala", "Shubhi", "Jaya", "Kavita", "Neha", "Bhavini", "Madhvi", "Priya",
        "Priti", "Trupti", "Ami", "Bhakti", "Manjula", "Parvati", "Nidhi", "Rupali", "Soni", "Yogita",
        "Tanu", "Kajal", "Isha", "Nisha", "Poonam", "Seema", "Aarti", "Radha", "Asha", "Suman"
    ]

    gujrati_female_surname = [
        "Patel", "Shah", "Bavani", "Vora", "Joshi", "Parikh", "Mehta", "Chaudhary", "Trivedi", "Pandya",
        "Sharma", "Dixit", "Mishra", "Purohit", "Joshi", "Chauhan", "Rathod", "Thakur", "Yadav", "Brahmbhatt",
        "Soni", "Bavishi", "Jani", "Chandran", "Raval", "Prajapati", "Desai", "Rajput", "Shukla", "Thakkar",
        "Patel", "Makwana", "Chavda", "Mistry", "Rana", "Vaghela", "Barai", "Raj", "Khant", "Prajapati",
        "Shukla", "Tiwari", "Pandey", "Vishwakarma", "Upadhyay", "Brahmbhatt", "Chaudhary", "Sharma", "Pandya", "Saraswat",
        "Rathod", "Chauhan", "Raval", "Rajput", "Solanki", "Deshmukh", "Vaghela", "Singh", "Shah", "Sengar",
        "Bhil", "Warli", "Gamit", "Rathwa", "Sabar", "Sodha", "Dubla", "Lohana", "Rathva",
        "Modi", "Patel", "Gandhi", "Thackeray", "Ambani", "Agarwal", "Shah", "Rupani", "Bajpai", "Hirani",
        "Desai", "Bachchan", "Sharma", "Kumar", "Nanda", "Bedi", "Mehta",
        "Prabhu", "Singh", "Pandya", "Soni", "Joshi", "Kailash", "Gandhi", "Nair", "Jain", "Dhar",
        "Naik", "Siddiqui", "Sarabhai", "Patel", "Thakkar", "Tiwari", "Lohar", "Kundra", "Hirani", "Mehta",
        "Rathi", "Bhat", "Parmar", "Bhagat", "Sharma", "Kumawat", "Soni", "Singh", "Verma", "Yadav",
        "Ravani", "Solanki", "Soni", "Goswami", "Sheth", "Patel", "Vankar", "Bava", "Vora", "Nayak",
        "Khunt", "Mevani", "Jogi", "Gandhi", "Vasava", "Rajgor", "Panjwani", "Modh", "Vaniya", "Khatri",
        "Sanghvi", "Upadhyay", "Panchal", "Bansal", "Thaker", "Vekariya", "Kothari", "Raval", "Mistry",
        "Parmar", "Goyani", "Bhavsar", "Nadkarni", "Kalani", "Patel", "Agarwal", "Sanghvi", "Jain",
        "Deshmukh", "Surani", "Soni", "Gokani", "Sarvani", "Vakharia", "Vaswani", 
        "Bansal", "Kothari", "Wala", "Dholakia", "Tiwari", "Maru", "Bharadwaj", "Sura",
        "Bachchani", "Dixit", "Vaghela", "Jadhav", "Gokul", "Mehta", "Tewari", "Vadera", "Rathod",
        "Vasani", "Khushwaha", "Chandra", "Nadgouda", "Pate", "Vanka", "Nair", "Panchal", "Vahora",
        "Chaudhary", "Jasani", "Patil", "Kumar", "Sodha", "Sarma", "Mishra", "Chawla", "Raval",
        "Rathi", "Rana", "Suthar", "Kavedia", "Singh", "Varma", "Kale", "Soni", "Mavani", "Desai",
        "Gokhani", "Jariwala", "Rupani", "Chandran", "Nayak", "Jadeja", "Kali", "Zaveri", "Hirji",
        "Wagh", "Patil", "Shah", "Mistry", "Jeevraj", "Bhagat", "Sangvi", "Nagori", "Pujara", "Lad",
        "Kambhoj", "Singhvi", "Thakor", "Sodhi", "Khariwala", "Jindal", "Bajpai", "Ruparelia", "Bansal",
        "Kapadia", "Tiwari", "Mathur", "Bhimani", "Gupta", "Vora", "Vaghela", "Solanki", "Dewani",
        "Sivach", "Patwari", "Soni", "Vaghani", "Vasava", "Makwana", "Panwala", "Raval", "Sarvaiya"
    ]


    gujrati_female_suffix= ["bha", "ben", "bhen"]

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(gujrati_male_firstname)
        last_name_male = random.choice(gujrati_male_surname)
        suffix_male = random.choice(gujrati_male_suffix)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male + suffix_male  # Only first name with suffix
        else:
            name_male = first_name_male + suffix_male + " " + last_name_male  # Full name with suffix

        # Female Name Generation
        first_name_female = random.choice(gujrati_female_firstname)
        last_name_female = random.choice(gujrati_female_surname)
        suffix_female = random.choice(gujrati_female_suffix)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female + suffix_female  # Only first name with suffix
        else:
            name_female = first_name_female + suffix_female + " " + last_name_female  # Full name with suffix

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_gujarat_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df