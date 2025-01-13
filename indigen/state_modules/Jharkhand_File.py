import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_jharkhand_names(n, user_preference=None):
# Jharkhand Male First Names
    jharkhand_male_firstname = [
        'Hathiram', 'Narendra', 'Sharad', 'Arvind', 'Lakshman', 'Hemant', 'Jagannath', 'Lakra', 'Virendra', 'Madan', 'Tejas', 
        'Chandu', 'Lal', 'Madhusudan', 'Vivek', 'Uday', 'Dev', 'Rishi', 'Harendra', 'Sagar', 'Ajit', 'Jaswinder', 'Subodh', 'Sugan', 'Mohan', 
        'Pratap', 'Anil', 'Tushar', 'Rakesh', 'Koch', 'Yogeshwar', 'Subham', 'Madhav', 'Rajiv', 'Shivansh', 'Bhupendra', 'Bairagi', 'Subhash', 
        'Vijay', 'Jalal', 'Jagdish', 'Prakash', 'Adarsh', 'Vishal', 'Raghavendra', 'Vasudev', 'Shakti', 'Mangal', 'Kalam', 'Ajay', 'Krishna', 
        'Vishwajeet', 'Deepak', 'Surendra', 'Shravan', 'Sukhdev', 'Pundit', 'Raj', 'Sikram', 'Jotu', 'Akash', 'Kumar', 'Raajeev', 'Kandru', 
        'Ishwar', 'Sushil', 'Babu', 'Shubham', 'Rajesh', 'Rahul', 'Umesh', 'Kisram', 'Manav', 'Jamu', 'Udit', 'Manu', 'Ganesh', 'Tarun', 'Harish', 
        'Shubhendu', 'Ritesh', 'Muni', 'Amit', 'Vishnu', 'Vimal', 'Suraj', 'Durgesh', 'Muniya', 'Kavindra', 'Kishan', 'Alok', 'Sudhir', 'Lekh', 
        'Pawan', 'Ajeet', 'Siddharth', 'Ram', 'Omkar', 'Rameshwar', 'Lalit', 'Bhavesh', 'Om', 'Rishabh', 'Hitesh', 'Nitin', 'Tiru', 'Govind', 
        'Neelesh', 'Sumeet', 'Harsh', 'Shibu', 'Purna', 'Kunal', 'Dinesh', 'Bhushan', 'Shivendra', 'Pravin', 'Sanjay', 'Babulal', 'Yash', 'Chandan', 
        'Raaj', 'Satyan', 'Kamla', 'Neeraj', 'Subramaniam', 'Pulin', 'Karan', 'Narayan', 'Kishore', 'Ravindra', 'Sachin', 'Dhanraj', 'Kailas', 
        'Sohan', 'Mukul', 'Milan', 'jharkhandlal', 'Sunder', 'Sandeep', 'Ramu', 'Kartik', 'Tanay', 'Kiran', 'Pritesh', 'Inder', 'Ujjwal', 'Santosh', 
        'Ramesh', 'Pranav', 'Ravi', 'Mithilesh', 'Jai', 'Jatu', 'Pankaj', 'Yogendra', 'Girish', 'Manish', 'Pahar', 'Raghav', 'Amar', 'Basant', 
        'Suryakant', 'Jilam', 'Shyam', 'Rangin', 'Pati', 'Ankur', 'Mahendra', 'Chandran', 'Inderjeet', 'Tej', 'Pradeep', 'Nadir', 'Gaurav', 
        'Chandrakant', 'Kissam', 'Sudeep', 'Yuvraj', 'Bhavin', 'Suman', 'Pranjal', 'Tirul', 'Chhagan', 'Rishikesh', 'Rajendra', 'Raghunath', 
        'Chetan', 'Sonu', 'Kamlesh', 'Shashi', 'Nandkishore', 'Kamran', 'Tapan', 'Vinod', 'Nilesh', 'Vinay', 'Jitendra', 'Balraj', 'Keshav', 
        'Dattatreya', 'Madhur', 'Mangesh', 'Vikash', 'Rupesh', 'Suryanarayan', 'Nagesh', 'Mundal', 'Karma', 'Jayant', 'Shailendra', 'Brijesh', 
        'Ashwin', 'Chandresh', 'Dharmendra', 'Abhinav', 'Kapil', 'Gopal', 'Aaditya', 'Lalith', 'Pavan', 'Suresh', 'Vikas', 'Kailash', 'Ishaan', 
        'Bharat', 'Yashvardhan', 'Tanuj', 'Shankar', 'Indrajeet', 'Lakhan', 'Manoj', 'Nikhil', 'Niraj', 'Satish', 'Saurabh', 'Komal', 'Vikram', 
        'Kamak', 'Sakti', 'Pahen', 'Atul', 'Rohit', 'Toppo', 'Bansal', 'Chottu', 'Darshan', 'Hemendra', 'Prem', 'Arjun', 'Kerketta', 'Ashok', 
        'Aakash', 'Anand', 'Chinmay', 'Somesh', 'Devendra', 'Naman', 'Abhay', 'Leko', 'Shashank', 'Yogesh', 'Baba', 'Kherwar', 'Viral', 'Satyam', 
        'Minz', 'Chirag', 'Vineet', 'Pahuja', 'Nakul', 'Birendra', 'Vivekanand']

    # Jharkhand Male Surnames
    jharkhand_male_surname = [ 
        "Murmu", "Soren", "Tudu", "Hembrom", "Biru", "Roya", "Munda",
        "Jalim", "Karma", "Birsamunda", "Kerketta", "Minz", "Kerketta",
        "Tila", "Lakra", "Horo", "Sundar", "Kandul", "Ranchi", "Reko", "Sah",
        "Godi", "Kharia", "Bhumij", "Munda", "Kessari", "Sundar", "Kisko", "Bhumij",
        "Kisku", "Toppo", "Tudu", "Pahari", "Sinha", "Prasad", "Choudhary", "Kumar",
        "Yadav", "Rai", "Pandey", "Jha", "Thakur", "Singh", "Sharma", "Tiwari", "Verma",
        "Gupta", "Chand", "Ranjan", "Jaiswal", "jharkhand", "Chauhan", "Mishra","Kumar"]


    # Jharkhand Female First Names
    jharkhand_female_firstname = [
        'Rati', 'Mansi', 'Vimala', 'Dhriti', 'Asha', 'Rajani', 'Trisha', 'Lota', 'Simran', 'Dulma', 'Ruthri', 'Sampada', 
        'Nayantara', 'Karishma', 'Kusum', 'Rasiya', 'Sadhana', 'Shikha', 'Tarini', 'Lalima', 'Rani', 'Ekisha', 'Mishri', 'Koyal', 
        'Harini', 'Ananya', 'Ishita', 'Durga', 'Mina', 'Tripti', 'Tina', 'Sharika', 'Sujata', 'Daku', 'Komal', 'Chandni', 'Nadiya', 
        'Preeti', 'Sakti', 'Deepika', 'Tanvi', 'Dhulma', 'Nirupa', 'Swati', 'Chandini', 'Janta', 'Tilu', 'Shanta', 'Mithila', 'Sachi', 
        'Babli', 'Adiva', 'Kamli', 'Rangli', 'Palvi', 'Gauri', 'Kanika', 'Kanchan', 'Kajal', 'Nagma', 'Priya', 'Richa', 'Janki', 'Urmi', 
        'Jeevika', 'Lalitha', 'Daksha', 'Manju', 'Buli', 'Sushmita', 'Rupal', 'Rachna', 'Aanya', 'Risha', 'Diya', 'Jagruti', 'Alka', 'Raghu', 
        'Ankita', 'Jaya', 'Roshni', 'Shweta', 'Yamuna', 'Bhumika', 'Sangeeta', 'Ganga', 'Kohli', 'Jalpa', 'Vimla', 'Sridevi', 'Jaswanti', 
        'Chuni', 'Padmini', 'Anandita', 'Rekha', 'Vasudha', 'Githa', 'Kavya', 'Pavani', 'Jhilik', 'Vaishali', 'Purnima', 'Amrita', 'Somita', 
        'Aradhya', 'Tari', 'Beni', 'Teji', 'Sumita', 'Kamla', 'Saloni', 'Sneha', 'Balkrishna', 'Abha', 'Sampoorna', 'Charulata', 'Arpita', 
        'Shruti', 'Suman', 'Kalpana', 'Hema', 'Vandini', 'Vishakha', 'Sonal', 'Karma', 'Ishwari', 'Bina', 'Vidhi', 'Lalita', 'Nisha', 
        'Anshu', 'Yamini', 'Shashi', 'Sakshi', 'Tuni', 'Madhura', 'Pragya', 'Pooja', 'Kumari', 'Laxmi', 'Kriti', 'Anita', 'Ritika', 'Vishali', 
        'Gargee', 'Sarla', 'Ruchi', 'Anju', 'Anku', 'Vineeta', 'Rakhi', 'Anamika', 'Prachi', 'Kiran', 'Tulika', 'Ravina', 'Yashika', 'Shivani', 
        'Chhaya', 'Shakti', 'Aditi', 'Shalini', 'Nidhi', 'Ekta', 'Narmada', 'Kavita', 'Sanika', 'Devaki', 'Seema', 'Dharini', 'Dalu', 'Sita', 
        'Savita', 'Vandana', 'Murli', 'Sari', 'Pratibha', 'Anjali', 'Juni', 'Harsha', 'Tanya', 'Ashi', 'Dulari', 'Shilpa', 'Dhani', 'Vasanti', 
        'Sonali', 'Bansari', 'Binu', 'Uma', 'Neha', 'Gargi', 'Surbhi', 'Malti', 'Mintu', 'Jhumka', 'Deepa', 'Kamini', 'Isha', 'Naina', 'Avni', 
        'Geeta', 'Chandana', 'Manjari', 'Tanu', 'Gulika', 'Barkha', 'Asmita', 'Pallavi', 'Madhuri', 'Hiruni', 'Rita', 'Aparna', 'Varsha', 
        'Gouri', 'Madhavi', 'Vidya', 'Ira', 'Vasundhara', 'Aloka', 'Kala', 'Sheetal', 'Indumati', 'Geetika', 'Bhavna', 'Indira', 'Deepali', 
        'Tara', 'Aarti', 'Kavitha', 'Divya', 'Munia', 'Sanya', 'Sumanthika', 'Vidushi', 'Kunti', 'Sundari', 'Soni', 'Yashoda', 'Draupadi', 
        'Poonam', 'Maya', 'Chandramukhi', 'Kirti', 'Jasmin', 'Nupur', 'Diksha', 'Archana', 'Arundhati', 'Bajhi', 'Swarnima', 'Garima', 
        'Shubhi', 'Zarina', 'Esha', 'Bira', 'Vani', 'Deepshikha', 'Tanuja', 'Ragini', 'Meena', 'Sashi', 'Bhoomi', 'Chandrika', 'Aishwarya', 
        'Nandu', 'Shraddha', 'Rupa', 'Tarika', 'Rimpa', 'Meenakshi', 'Snehal', 'Zara', 'Meenal', 'Jhalak', 'Gulki', 'Mona', 'Neelam', 'Lulki', 
        'Kirmi', 'Pankhuri', 'Urmila', 'Manisha', 'Sona', 'Rina', 'Sushila', 'Vina', 'Kanak', 'Asita', 'Meera', 'Chunri', 'Deepti', 'Rukmini', 
        'Sheela', 'Tanisha', 'Nandini', 'Aadya', 'Jali', 'Nira', 'Kanha', 'Sharmila', 'Giri', 'Jivika', 'Adiya', 'Hira', 'Srishti', 'Rajni', 
        'Sharini', 'Radhika', 'Ranjita', 'Niharika', 'Nikita', 'Vishnu', 'Chhavi', 'Mahua', 'Bipasha', 'Sabi', 'Vibha', 'Vandita', 'Birsa', 
        'Shailja', 'Veda', 'Alisha']


    jharkhand_female_surname = [
        "Munda", "Soren", "Tudu", "Kerketta", "Mahato", "Bedia", "Hembrom", "Sah", "Horo",
        "Minz", "Murmu", "Kisku", "Manki", "Baskey", "Toppo", "Jharia", "Sahdeo", "Pahan",
        "Lota", "Dhanwar", "Chakraborty", "Kumar", "Lal", "Rajak", "Rani", "Sadhukhan",
        "Bedi", "Mahapath", "Sharma", "Singh", "Singhvi", "Agarwal", "Patel", "Bhumij",
        "Dundhi", "Gurusaria", "Nayak", "Pattanaik", "Mishra", "Choudhury", "Rathore",
        "Bhoi", "Chaudhary", "Naik", "Barmania", "Rajwar", "Bairagi", "Savant", "Mahapathak", "Siddharth", "Thakur", "Dewri"]

    jharkhand_female_suffix = ['', '', '', "devi", "rani", "kumari", '']

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(jharkhand_male_firstname)
        last_name_male = random.choice(jharkhand_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(jharkhand_female_firstname)
        last_name_female = random.choice(jharkhand_female_surname)
        suffix_female = random.choice(jharkhand_female_suffix)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female + " " + suffix_female  # Full name with optional suffix

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female.strip(), "Female"))  # Strip extra spaces from female name

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_jharkhand_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df

