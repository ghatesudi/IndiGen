import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# uttarpradesh Male and Female First Names and Surnames
def generate_uttarpradesh_names(n, user_preference=None):

    # uttarpradesh Male First name
    uttarpradesh_male_firstname = [
        "Aarav", "Abhay", "Abhishek", "Achyut", "Adarsh", "Aditya", "Agastya", "Ajay", "Akash", "Akhilesh", "Alok", "Amar",
        "Amarnath", "Ambar", "Amit", "Anand", "Anant", "Anil", "Anirudh", "Ankit", "Ansh", "Anupam", "Arjun", "Arvind",
        "Ashish", "Ashok", "Atmaram", "Atul", "Avadhesh", "Avinash", "Ayodhya", "Ayush", "Badrinath", "Balram",
        "Bhanu", "Bharat", "Bhaskar", "Bhavesh", "Bhim", "Bhishma", "Bhuvan", "Bikram", "Chandan", "Chandra",
        "Chandrabhanu", "Chandrahas", "Charan", "Darpan", "Darshan", "Daya", "Deepak", "Dev", "Devdutt", "Devendra",
        "Dhanraj", "Dharmendra", "Dhruv", "Dinesh", "Dipak", "Dipesh", "Durgesh", "Ganesh", "Gaurav", "Girish", "Gopal",
        "Govind", "Gulab", "Gunjan", "Gyanendra", "Hardik", "Harendra", "Hari", "Harish", "Harivansh", "Hemant", "Himmat",
        "Hrithik", "Inder", "Indrajit", "Ishaan", "Ishwar", "Jagannath", "Jagat", "Jagdish", "Jai", "Jaidev", "Janardhan",
        "Jitendra", "Jyotiprakash", "Kailash", "Kalicharan", "Kalyan", "Kamal", "Kanhaiya", "Karan", "Karunesh", "Kashinath",
        "Keshav", "Kiran", "Kishore", "Krishan", "Krishna", "Krishnendu", "Kulbhushan", "Kuldeep", "Lakshman", "Lakshmi Kant",
        "Lakshmi Narayan", "Lalit", "Lokesh", "Madan", "Madhav", "Mahavir", "Mahendra", "Mangal", "Manoj", "Mayank",
        "Mithilesh", "Mohan", "Mukesh", "Mukund", "Munna", "Narayan", "Narendra", "Naresh", "Narinder", "Navin", "Nayan",
        "Nikhil", "Nilesh", "Niranjan", "Nirmal", "Omkar", "Omprakash", "Padmanabh", "Pankaj", "Param", "Parashuram",
        "Parshad", "Parth", "Phoolchand", "Prabhat", "Pradeep", "Pradyumna", "Prahlad", "Prakash", "Pranav", "Prashant",
        "Prem", "Priyanshu", "Pushpendra", "Radheshyam", "Raghav", "Raghavendra", "Raghunath", "Raghuveer", "Rahul", "Raj",
        "Rajan", "Rajat", "Rajendra", "Rajesh", "Rajiv", "Rakesh", "Ramakant", "Rambir", "Ramesh", "Ramgopal", "Ramkishan",
        "Ramnarayan", "Rampratap", "Ramu", "Ranveer", "Ravi", "Rishabh", "Rishi", "Ritesh", "Rohit", "Roopchand", "Sachin",
        "Sagar", "Sahadev", "Sameer", "Sandeep", "Sanjay", "Sanjeev", "Santosh", "Sarvesh", "Satendra", "Satish", "Shankar",
        "Sharad", "Shashank", "Shekhar", "Shiv", "Shivam", "Shivendra", "Shivraj", "Shobhit", "Shravan", "Shridhar", "Shyam",
        "Shyamsunder", "Somesh", "Subhash", "Sudarshan", "Sudeep", "Sudesh", "Sudhir", "Sukhdev", "Sunder", "Suraj",
        "Surendra", "Suresh", "Suryakant", "Tapan", "Tarun", "Tejas", "Trilok", "Uday", "Ujjwal", "Umashankar", "Umesh",
        "Upendra", "Vaibhav", "Vallabh", "Vanraj", "Vedprakash", "Veerbhadra", "Vibhuti", "Vidyadhar", "Vijay", "Vikas",
        "Vikram", "Vikrant", "Vimal", "Vinay", "Vishal", "Vishnu", "Yash", "Yashpal", "Yashwant", "Yatindra"]

    uttarpradesh_male_surname =  [
        "Agrawal", "Ahuja", "Awasthi", "Babu", "Baghel", "Bajpai", "Bajaj", "Bais", "Bakshi", "Bansal", "Baranwal",
        "Bhadauria", "Bhardwaj", "Bhargava", "Bhatnagar", "Bharadwaj", "Bisht", "Chaubey", "Chauhan", "Chaturvedi",
        "Chaurasia", "Dixit", "Dubey", "Dwivedi", "Garg", "Gautam", "Gaur", "Goel", "Gupta", "Harit", "Jaiswal", "Jain",
        "Joshi", "Kaul", "Kesarwani", "Khare", "Kashyap", "Kapoor", "Khandelwal", "Khanna", "Kulshreshtha", "Katiyar",
        "Kaushik", "Khatik", "Lodhi", "Lohia", "Madan", "Malhotra", "Mani", "Mathur", "Maurya", "Mishra", "Mittal", "Kumar"
        "Modi", "Morya", "Nag", "Nagar", "Nagpal", "Namdev", "Nath", "Nautiyal", "Nigam", "Ojha", "Pal", "Pandey",
        "Parashar", "Pathak", "Patel", "Patwa", "Paliwal", "Pandit", "Prasad", "Rastogi", "Rawat", "Rathi", "Sachdeva",
        "Sahai", "Sahay", "Saini", "Saraswat", "Saxena", "Sehgal", "Seth", "Shahi", "Sharma", "Shandilya", "Shukla",
        "Singh", "Sisodia", "Somvanshi", "Srivastava", "Suryavanshi", "Tandon", "Tewari", "Thakur", "Tomar", "Tripathi",
        "Tyagi", "Upadhyay", "Vaidya", "Vajpayee", "Vashishta", "Verma", "Vyas", "Yadav", "Agarwal", "Anand", "Adhikari",
        "Bhandari", "Bhatti", "Chauhary", "Dahiya", "Dayal", "Datta", "Deshpande", "Goswami", "Goyal", "Gulati", "Harish",
        "Johar", "Kamboj", "Kesari", "Khurana", "Lal", "Maheshwari", "Mandal", "Nagori", "Narang", "Nayyar", "Panchal",
        "Pande", "Pareek", "Parikh", "Rathore", "Sahni", "Saluja", "Sheoran", "Solanki", "Sood", "Tiwari", "Upasani",
        "Varma", "Vats", "Vishwakarma"]

    # uttarpradesh Female First name
    uttarpradesh_female_firstname = [
        "Aabha", "Aarti", "Aasha", "Abha", "Abhilasha", "Achala", "Aditi", "Adya", "Aishwarya", "Akanksha", "Alka", "Amba",
        "Ambika", "Amita", "Amrita", "Anandi", "Ananya", "Anasuya", "Anjali", "Anjana", "Anju", "Ankita", "Annapurna",
        "Anshika", "Anuradha", "Anushka", "Aparajita", "Aparna", "Archana", "Arpita", "Aruna", "Arundhati", "Asha",
        "Ashima", "Ashwini", "Asita", "Avanti", "Babita", "Bageshwari", "Bani", "Bhagyashree", "Bhanumati", "Bharati",
        "Bharti", "Bhavani", "Bhavna", "Bhuvana", "Bina", "Chaitali", "Chanchal", "Chanda", "Chandi", "Chandra",
        "Chandrakala", "Chhavi", "Chhaya", "Daksha", "Damini", "Darshana", "Deepa", "Deepali", "Deepti", "Devaki",
        "Devanshi", "Devika", "Dhanalakshmi", "Dhara", "Dharmavati", "Dimple", "Dipali", "Divya", "Dolly", "Drishti",
        "Durga", "Ganga", "Gauri", "Gayatri", "Geeta", "Girija", "Gulab", "Gulika", "Hema", "Hemlata", "Hiral", "Indira",
        "Indu", "Ishita", "Ishwari", "Jagriti", "Jagruti", "Jamuna", "Janki", "Jaya", "Jayalakshmi", "Jayanti", "Jyoti",
        "Jyotsna", "Kalindi", "Kalpana", "Kamakshi", "Kamala", "Kamini", "Kanchan", "Kanika", "Kanta", "Karuna", "Kavita",
        "Kavya", "Ketaki", "Khushboo", "Kiran", "Komal", "Kumari", "Kusum", "Lalita", "Lata", "Lavanya", "Laxmi", "Leela",
        "Lila", "Lisha", "Madhavi", "Madhu", "Madhubala", "Madhumita", "Mahima", "Malati", "Mamta", "Manasi", "Manisha",
        "Manju", "Manorama", "Meena", "Meera", "Megha", "Meher", "Mehul", "Mohini", "Mridula", "Mukta", "Naina", "Nanda",
        "Nandini", "Narmada", "Nayana", "Neelam", "Neerja", "Neeta", "Neha", "Nidhi", "Nikita", "Nirmala", "Nirupama",
        "Nisha", "Nupur", "Nutan", "Padma", "Padmini", "Pallavi", "Parul", "Parvati", "Pooja", "Poonam", "Poornima",
        "Prabha", "Prabhavati", "Pragya", "Pratibha", "Preeti", "Priya", "Purnima", "Pushpa", "Rachna", "Radha",
        "Rajalakshmi", "Rajani", "Rajeshwari", "Raji", "Rajni", "Raksha", "Rama", "Ramaa", "Rani", "Ranjana", "Rashi",
        "Rashmi", "Reema", "Rekha", "Renuka", "Revati", "Richa", "Riddhi", "Ritu", "Riya", "Roopa", "Roshni", "Rukmini",
        "Rupali", "Sadhana", "Sahana", "Saheli", "Sajal", "Sakshi", "Saloni", "Samridhi", "Sandhya", "Sangeeta", "Sangita",
        "Sanjana", "Sapna", "Saraswati", "Sarita", "Saroja", "Savitri", "Seema", "Shailaja", "Shakti", "Shakuntala",
        "Shalini", "Shanta", "Shanti", "Sharada", "Sharda", "Shashi", "Shikha", "Shilpa", "Shivani", "Shobha", "Shraddha",
        "Shradha", "Shreya", "Shruti", "Shubha", "Shubhangi", "Shweta", "Simran", "Sita", "Smita", "Sneha", "Sohini",
        "Sona", "Sonal", "Sonia", "Sonu", "Sreelakshmi", "Sridevi", "Sritama", "Sudha", "Sugandha", "Sujata", "Suman",
        "Sumanlata", "Sunaina", "Sunanda", "Sundari", "Sunita", "Supriya", "Surabhi", "Surya", "Sushila", "Sushma", "Swati",
        "Tanuja", "Tanvi", "Tapasi", "Tejal", "Tripti", "Trupti", "Tulsi", "Uma", "Urmila", "Usha", "Ushas", "Vaidehi",
        "Vaishali", "Vandana", "Varalakshmi", "Varsha", "Vasanti", "Vasudha", "Vidya", "Vimal", "Vimla", "Vinita",
        "Vinodini", "Viresh", "Vishakha", "Yamini", "Yashoda", "Yogini"]

    uttarpradesh_female_surname =  [
        "Agrawal", "Ahuja", "Awasthi", "Babu", "Baghel", "Bajpai", "Bajaj", "Bais", "Bakshi", "Bansal", "Baranwal", "Devi",
        "Bhadauria", "Bhardwaj", "Bhargava", "Bhatnagar", "Bharadwaj", "Bisht", "Chaubey", "Chauhan", "Chaturvedi",
        "Chaurasia", "Dixit", "Dubey", "Dwivedi", "Garg", "Gautam", "Gaur", "Goel", "Gupta", "Harit", "Jaiswal", "Jain",
        "Joshi", "Kaul", "Kesarwani", "Khare", "Kashyap", "Kapoor", "Khandelwal", "Khanna", "Kulshreshtha", "Katiyar",
        "Kaushik", "Khatik", "Lodhi", "Lohia", "Madan", "Malhotra", "Mani", "Mathur", "Maurya", "Mishra", "Mittal",
        "Modi", "Morya", "Nag", "Nagar", "Nagpal", "Namdev", "Nath", "Nautiyal", "Nigam", "Ojha", "Pal", "Pandey", "Kumari",
        "Parashar", "Pathak", "Patel", "Patwa", "Paliwal", "Pandit", "Prasad", "Rastogi", "Rawat", "Rathi", "Sachdeva",
        "Sahai", "Sahay", "Saini", "Saraswat", "Saxena", "Sehgal", "Seth", "Shahi", "Sharma", "Shandilya", "Shukla",
        "Singh", "Sisodia", "Somvanshi", "Srivastava", "Suryavanshi", "Tandon", "Tewari", "Thakur", "Tomar", "Tripathi",
        "Tyagi", "Upadhyay", "Vaidya", "Vajpayee", "Vashishta", "Verma", "Vyas", "Yadav", "Agarwal", "Anand", "Adhikari",
        "Bhandari", "Bhatti", "Chauhary", "Dahiya", "Dayal", "Datta", "Deshpande", "Goswami", "Goyal", "Gulati", "Harish",
        "Johar", "Kamboj", "Kesari", "Khurana", "Lal", "Maheshwari", "Mandal", "Nagori", "Narang", "Nayyar", "Panchal",
        "Pande", "Pareek", "Parikh", "Rathore", "Sahni", "Saluja", "Sheoran", "Solanki", "Sood", "Tiwari", "Upasani",
        "Varma", "Vats", "Vishwakarma"]
    
    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(uttarpradesh_male_firstname)
        last_name_male = random.choice(uttarpradesh_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(uttarpradesh_female_firstname)
        last_name_female = random.choice(uttarpradesh_female_surname)

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
    file_path = 'generated_uttarpradesh_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df