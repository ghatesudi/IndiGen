import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_bihar_names(n, user_preference=None):
    
    bihari_male_firstname = [
        'Saroj', 'Anirudh', 'Sukesh', 'Bhavesh', 'Bhairav', 'Suman', 'Ashok', 'Tilak', 'Madan', 'Shankar Lal', 'Amarendra', 
    'Durgesh', 'Mudit', 'Mohit', 'Ashish', 'Yashwant', 'Dayanand', 'Ajit', 'Santosh', 'Raghvendra', 'Arvind', 'Anup', 'Ashutosh', 
    'Lakhan', 'Dharmendra', 'Anil', 'Loknath', 'Sitaram', 'Baleshwar', 'Tanay', 'Pushkar', 'Ramesh', 'Uday', 'Keshavdas', 'Mangesh', 
    'Ujjwal', 'Pritam', 'Amar', 'Kishore', 'Ghanashyam', 'Ramanuj', 'Raj', 'Mohan', 'Kripal', 'Jagmohan', 'Raghav', 'Ketan', 'Daksh', 
    'Raghunandan', 'Lalchand', 'Sudarshan', 'Hemendra', 'Gajendra', 'Indrapal', 'Vivekanand', 'Sanjeev', 'Nitin', 'Eklavya', 
    'Tejendra', 'Bhaskar', 'Hariram', 'ShravanKunal', 'Vardhan', 'Sundar', 'Prem', 'Yogendra', 'Sachin', 'Bikram', 'Lalit', 
    'Pitambar', 'Narinder', 'Aryan', 'Shailendra', 'Umeshwar', 'Satyendra', 'Naveen', 'Dhananjay', 'Premnath', 'Vimal', 'Udayan', 
    'Omveer', 'Atmaram', 'Ishwar', 'Pratap', 'Satish', 'Somesh', 'Jayant', 'Satendra', 'Anand', 'Chirag', 'Rajbir Singh', 
    'Ganeshwar', 'Jaikishan', 'Ashvath', 'Ranvijay', 'Naresh', 'Munendra', 'Ashwin', 'Rohan', 'Devraj', 'Zakir', 'Devendra', 
    'Hemant', 'Mandar', 'Rajan', 'Harsha', 'Ganesh', 'Surajit', 'Krishna', 'Indrajeet', 'Jai', 'Rajeev', 'Jitender', 'Ekendra', 
    'Murari', 'Rishabh', 'Nandlal', 'Dineshwar', 'Shyam Sundar', 'Shiv', 'Surendra', 'Dinesh', 'Aditya', 'Puran', 'Vedant', 
    'Prabhat', 'Raghunath', 'Rudra', 'Utsav', 'Hariprasad', 'Bholanath', 'Jugal', 'Padmanabh', 'Vikash', 'Rajesh', 'Suresh', 
    'Parmeshwar', 'Vaibhav', 'Suraj', 'Punit', 'Pandit', 'Ajeet', 'Keshar', 'Vedprakash', 'Kapil', 'Tulsiram', 'Dharamveer', 
    'Mahesh', 'Jashvendra', 'Chhoteylal', 'Nirmal', 'Karan', 'Vijayendra', 'Kamal', 'Lakshman', 'Shubhendra', 'Bijay', 
    'Chhaganlal', 'Trilok Chand', 'Harish', 'Mahavir', 'Kanhaiya', 'Tarsem', 'Nabin', 'Subhendu', 'Rishikesh', 'Gopal', 
    'Chandra', 'Sumit', 'Ranveer', 'Sandeep', 'Omprakash', 'Kuldeep', 'Kashyap', 'Kanaiya', 'Kamesh', 'Shankar Prasad', 
    'Shravan', 'Manohar', 'Suryakant', 'Rajiv', 'Vishesh', 'Ranbir', 'Vipin', 'Subodh', 'Bachan', 'Keshav', 'Yadunandan', 
    'Siddharth', 'Baliram', 'Shubhendu', 'Aman', 'Viren', 'Prakash', 'Shatrughan', 'Pritesh', 'Vivek', 'Govind', 'Jeetendra', 
    'Virendra', 'Shyam', 'Sujit', 'Swarnim', 'Charan', 'Surya', 'Kailash', 'Upendra', 'Yash', 'Avinash', 'Shubham', 'Chandrakant', 
    'Neeraj', 'Dharam', 'Janardan', 'Bhagwan', 'Vishwajeet', 'Subhash', 'Vijay', 'Sagar', 'Vishwa', 'Inder', 'Krishnan', 'Mukul', 
    'Yugal', 'Ajay', 'Chaturbhuj', 'Gokul', 'Vijendra', 'Arjun', 'Sharad', 'Satyam', 'Uttam', 'Chetan', 'Saurabh', 'Triveni', 
    'Priteshwar', 'Ritesh', 'Vrajendra', 'Sourav', 'Bharatendra', 'Niranjan', 'Himanshu', 'Mahender', 'Trilog', 'Abhay', 'Vinay', 
    'Indrajit', 'Jagannath', 'Sudhir', 'Kamraj', 'Harvinder', 'Ratan', 'Vishvajit', 'Jagdish', 'Debendra', 'Ramakant', 'Yatindra', 
    'Narottam', 'Keshavprasad', 'Rohit', 'Prashant', 'Vinit', 'Girish', 'Ram', 'Harsh', 'Jitesh', 'Nandkishore', 'Kaushal', 'Ranjan', 
    'Yashveer', 'Rajendra Prasad', 'Brahmdev', 'Girdhar', 'Ramendra', 'Rituraj', 'Nilesh', 'Bindeshwar', 'Nand Kishore', 'Jagat', 
    'Dipankar', 'Chhagan', 'Shivendra', 'Vishnu', 'Harendra', 'Damodar', 'Shree', 'Kartik', 'Chitrak', 'Karamvir', 'Sunil', 'Hiral', 
    'Bhanu', 'Bhupendra', 'Vidyapati', 'Nagendra', 'Madhukar', 'Rakesh', 'Navin', 'Jatin', 'Prithvi', 'Vishvendra', 'Kedar', 'Jashan', 
    'Laxman', 'Atul', 'Chandan', 'Nishant', 'Lalji', 'Harihar', 'Shailesh', 'Eshwar', 'Jagan', 'Shankar', 'Ravindra Prasad', 
    'Bhagirath', 'Kumar', 'Binod', 'Rajbir', 'Sandeepan', 'Dushyant', 'Prahlad', 'Lakhwinder', 'Dhanesh', 'Mahendra', 'Kamlesh', 
    'Nagesh', 'Madhav', 'Bharat', 'Ravindra', 'Mukesh', 'Yogesh', 'Pankaj', 'Basant', 'Manas', 'Om', 'Sanjay', 'Achyut', 'Lokesh', 
    'Vishal', 'Surendra Prasad', 'Trilok', 'Subhankar', 'Rameshwarnath', 'Bansidhar', 'Balaram', 'Rajendra', 'Umesh', 'Narayan', 
    'Gaurav', 'Rahul', 'Anandeshwar', 'Yograj', 'Aniket', 'Ravi', 'Rupesh', 'Ramil', 'Rameshwari', 'Brijesh', 'Shashank', 'Hitesh', 
    'Mukund', 'Darshan', 'Padmesh', 'Pranav', 'Shivam', 'Yatin', 'Vikas', 'Anant', 'Dilip', 'Akash', 'Vinod', 'Babulal', 'Gulshan', 
    'Sankar', 'Piyush', 'Manish', 'Ranjit', 'Ganpat', 'Jitendra', 'Gyanesh', 'Pradeep', 'Chanchal', 'Yudhishthir', 'Deepak', 'Bhola', 
    'Tarun', 'Manoj'
    ]

    bihari_male_surname = [
        "Agarwal", "Anjaria", "Arya", "Babu", "Bansal", "Baranwal", "Baran", "Bhagat", "Kumar", 
    "Bhartiya", "Bhaskar", "Bhumihar", "Chaudhary", "Chaurasia", "Chawla", "Choudhary", 
    "Das", "Dasgupta", "Dey", "Dubey", "Ghosh", "Gaur", "Gupta", "Jha", "Jaiswal", "Joshi", "Raj" 
    "Katiyar", "Khandelwal", "Koirala", "Mallick", "Mehta", "Mishra", "Nath", "Pandey", "Pathak", 
    "Prasad", "Rajak", "Ranjan", "Rathi", "Ranjit", "Rao", "Roy", "Sahu", "Sahni", "Sinha", "Singh", 
    "Srivastava", "Thakur", "Tiwari", "Tripathi", "Yadav", "Yadunandan", "Verma", "Vats", "Upadhyay", 
    "Agrahari", "Ajmani", "Arora", "Bajpai", "Banerjee", "Basu", "Bihari", "Bhupendra", "Chhattis", 
    "Chitnis", "Chauhan", "Chakraborty", "Dhanraj", "Dehri", "Dutt", "Gautam", "Ganguly", "Harish", 
    "Kanjirath", "Lall", "Lal", "Rajeshwar", "Rajiv", "Sahoo", "Satyendra", "Sharma", 
    "Singhal", "Vishwakarma", "Agarhary", "Dube", "Shekhar", "Shukla", "Nirala", "Patil", "Malviya", 
    "Bharti", "Puri", "Sahar", "Rajvanshi", "Dubay", "Mahto", "Mandal", "Kumar", "Rajput", "Narayan", 
    "Raaz", "Saket", "Soni"
    ]

    bihari_female_firstname = [
        'Sita', 'Dharmitha', 'Dhanwati', 'Padmini', 'Bhanumati', 'Gauri', 'Ashmita', 'Rohitha', 'Aalima', 'Deepti', 
    'Gayatri', 'Leela', 'Mona', 'Harsita', 'Kavindra', 'Nabanita', 'Aarini', 'Harini', 'Ghodaya', 'Prabhavati', 
    'Chhavi', 'Nirmla', 'Chhaya', 'Durga', 'Raji', 'Rupal', 'Menaka', 'Smita', 'Kamla', 'Devi', 'Mohana', 'Divya', 
    'Jyoti', 'Alpana', 'Vimla', 'Suranitha', 'Poonam', 'Aaradhya', 'Aparna', 'Rubina', 'Architha', 'Shreya', 'Supriya', 
    'Bhanuni', 'Bhumiksha', 'Deeptha', 'Jayanti', 'Shilpa', 'Anju', 'Shikha', 'Hema', 'Radha', 'Arpita', 'Shefali', 
    'Reena', 'Nirupama', 'Parvati', 'Kalpita', 'Damyanti', 'Lavitha', 'Smritha', 'Radhika', 'Tejaswitha', 'Sonia', 
    'Ganga', 'Shobha', 'Ananta', 'Shubhi', 'Kanak', 'Surabhi', 'Jaishree', 'Balika', 'Mandira', 'Priyanka', 
    'Rakshitha', 'Laxmi', 'Pallita', 'Rani', 'Dhriti', 'Roopa', 'Rinki', 'Rajni', 'Meenal', 'Kusum', 'Shanta', 
    'Ambika', 'Usha', 'Revati', 'Chanchal', 'Lavita', 'Ranjita', 'Ranjana', 'Priya', 'Malvika', 'Lajwanti', 'Kashish', 
    'Rajlakshmi', 'Madhubala', 'Pushpita', 'Charulata', 'Renu', 'Rekha', 'Sadhna', 'Asmitha', 'Deepal', 'Dushita', 
    'Gudiya', 'Abhaya', 'Gaurika', 'Yamini', 'Sheetal', 'Niharika', 'Ahalta', 'Minal', 'Sulochana', 'Meera', 
    'Rina', 'Pushpika', 'Swapna', 'Vrinda', 'Vasudhaitha', 'Roopmati', 'Bina', 'Rukmani', 'Vandita', 'Poornitha', 
    'Meena', 'Vidya', 'Maithili', 'Nikita', 'Shraddha', 'Rochana', 'Ishita', 'Pavitha', 'Janita', 'Aaloka', 
    'Kajal', 'Rupa', 'Deepa', 'Suman', 'Abhilasha', 'Pranjal', 'Bijli', 'Shilpi', 'Sabita', 'Sarojini', 'Parimala', 
    'Chitra', 'Babita', 'Pratita', 'Aarti', 'Sumitra', 'Bhawna', 'Bhavana', 'Subhi', 'Harshita', 'Sarita', 
    'Nivedita', 'Arti', 'Richa', 'Sneha', 'Divija', 'Basanti', 'Sadhana', 'Anuja', 'Nalini', 'Prabha', 'Damayanti', 
    'Neha', 'Bindiya', 'Mohini', 'Nirmala', 'Snehal', 'Meenakshi', 'Shashi', 'Mishika', 'Durgeshwari', 'Madhu', 
    'Reshitha', 'Nilima', 'Rajashree', 'Santhitha', 'Vibhuti', 'Shweta', 'Chandni', 'Prarthana', 'Aparajita', 
    'Phoolkumari', 'Gitika', 'Tejaswini', 'Mishrita', 'Roshani', 'Beena', 'Maheshwari', 'Kusumita', 'Taruna', 
    'Dinesha', 'Payal', 'Sakina', 'Devika', 'Chandra', 'Nidhi', 'Ira', 'Garima', 'Phoolmati', 'Indrani', 
    'Akanksha', 'Triveni', 'Kumud', 'Gunjan', 'Anshi', 'Adhira', 'Laxmibai', 'Ramdulari', 'Sudha', 'Sunitha', 
    'Padma', 'Amba', 'Sonali', 'Ishani', 'Champa', 'Pallavi', 'Bela', 'Lavanya', 'Renuka', 'Neelam', 'Meeta', 
    'Kavita', 'Shakuntala', 'Lalita', 'Deepika', 'Tanuja', 'Jyothitha', 'Kanta', 'Pratibha', 'Damini', 'Himani', 
    'Akshata', 'Rakhi', 'Kamala', 'Pranitha', 'Kanchana', 'Sonu', 'Saraswati', 'Madira', 'Anitha', 'Anupama', 'Malti', 
    'Kanchan', 'Sunanda', 'Mahima', 'Savitri', 'Kiran', 'Simran', 'Gouri', 'Prathibha', 'Maya', 'Kamini', 'Sangita', 
    'Bhavani', 'Shubita', 'Anuradha', 'Mita', 'Karuna', 'Kalindi', 'Aalokita', 'Komal', 'Nirmayi', 'Kalavati', 'Savita', 
    'Kavya', 'Arundhati', 'Sandhya', 'Vina', 'Tanvi', 'Sakshi', 'Ishwari', 'Khushbu', 'Shwetha', 'Sharmila', 'Bijaya', 
    'Malini', 'Nandini', 'Amritha', 'Mythitha', 'Preeti', 'Rameshwari', 'Vandana', 'Jyotsna', 'Gargee', 'Asha', 'Bimla', 
    'Sahana', 'Ahalya', 'Shubha', 'Deepmala', 'Manisha', 'Samita', 'Rambha', 'Chandini', 'Megha', 'Ashwini', 'Shravanitha', 
    'Prerana', 'Mala', 'Madhavi', 'Tripti', 'Anita', 'Harita', 'Kadambari', 'Vanitha', 'Tanu', 'Ayesha', 'Ritu', 'Chintamani', 
    'Hemlata', 'Annapurna', 'Vishalakshi', 'Ashita', 'Avani', 'Devangana', 'Anindita', 'Mamta', 'Charitha', 'Anjali', 'Madhulika', 
    'Aadrita', 'Meenu', 'Mridita', 'Meenaktha', 'Bhavna', 'Rashmi', 'Bijoya', 'Rajani', 'Dhanshree', 'Shabana', 'Bharti', 'Anurita', 
    'Malika', 'Manju', 'Mansi', 'Rati', 'Saira', 'Sarla', 'Anshika', 'Pushpa', 'Raksha', 'Nirmitha', 'Vaidehi', 'Rajita', 
    'Purnima', 'Chhandita', 'Indumati', 'Farida', 'Meenalata', 'Ritambara', 'Adarsha', 'Indira', 'Prabhati', 'Prisha', 'Roshini', 
    'Lata', 'Khushboo', 'Alka', 'Sharvata', 'Amrita', 'Gargi', 'Tanushree', 'Uma', 'Manorma', 'Haritha', 'Saheli', 'Varsha', 
    'Manvita', 'Prachi', 'Diksha', 'Parineeta', 'Swati', 'Shobhana', 'Rudrani', 'Gitashree', 'Kalpana', 'Sharada', 'Charita', 
    'Anisha', 'Seema', 'Gulabi', 'Jasoda', 'Yashitha', 'Archana', 'Ujjwala', 'Shruti', 'Jhanvi', 'Bhagyashree', 'Janki', 'Pranita', 
    'Saloni', 'Sunaina', 'Madhuri', 'Divyani', 'Pavitra', 'Sushma', 'Mridula', 'Karishma', 'Indrata', 'Geeta', 'Roshni', 'Vibha', 
    'Kusumlata', 'Divyata', 'Rishita', 'Snehaitha', 'Pranjali', 'Bandana', 'Abhitha', 'Aanchal', 'Pranavi', 'Rangoli', 'Sunita', 
    'Vismita', 'Sanjukta', 'Aabha', 'Manorama', 'Priti', 'Archisha', 'Shanti', 'Bhavya', 'Shabnam', 'Parul', 'Ahilya', 'Sharvani', 
    'Shalini', 'Indu', 'Nandita', 'Shashwati', 'Kanti', 'Dakshata', 'Rajeshwari', 'Jaya', 'Keerthitha', 'Vatsala', 'Namita', 
    'Vasundhara', 'Rituja', 'Chandani', 'Sujata', 'Gunjita', 'Upasana', 'Nisha'
    ]

    bihari_female_surname = [
        "Agarwal", "Anjaria", "Arya", "Babu", "Bansal", "Baranwal", "Baran", "Bhagat", "Kumari","Devi",
    "Bhartiya", "Bhaskar", "Bhumihar", "Chaudhary", "Chaurasia", "Chawla", "Choudhary", 
    "Das", "Dasgupta", "Dey", "Dubey", "Ghosh", "Gaur", "Gupta", "Jha", "Jaiswal", "Joshi", 
    "Katiyar", "Khandelwal", "Koirala", "Mallick", "Mehta", "Mishra", "Nath", "Pandey", "Pathak", 
    "Prasad", "Rajak", "Ranjan", "Rathi", "Ranjit", "Rao", "Roy", "Sahu", "Sahni", "Sinha",
    "Srivastava", "Thakur", "Tiwari", "Tripathi", "Yadav", "Yadunandan", "Verma", "Vats", "Upadhyay", 
    "Agrahari", "Ajmani", "Arora", "Bajpai", "Banerjee", "Basu", "Bihari", "Bhupendra", "Chhattis", 
    "Chitnis", "Chauhan", "Chakraborty", "Dhanraj", "Dehri", "Dutt", "Gautam", "Ganguly", "Harish", 
    "Kanjirath", "Lall", "Lal", "Modi", "Rajeshwar", "Rajiv", "Sahoo", "Satyendra", "Sharma", 
    "Singhal", "Vishwakarma", "Agarhary", "Dube", "Shekhar", "Shukla", "Nirala", "Patil", "Malviya", 
    "Bharti", "Puri", "Sahar", "Rajvanshi", "Dubay", "Mahto", "Mandal", "Rajput", "Narayan", 
    "Raaz", "Saket", "Soni"
    ]

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(bihari_male_firstname)
        last_name_male = random.choice(bihari_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(bihari_female_firstname)
        last_name_female = random.choice(bihari_female_surname)

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
    file_path = 'generated_bihar_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df
