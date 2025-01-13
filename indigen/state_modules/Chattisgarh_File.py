import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_chattisgarh_names(n, user_preference=None):

    # chattisgarh Male First Names
    chhattisgarh_male_firstname= [
        'Sushil', 'Ashwin', 'Vinod', 'Laxman Singh', 'Manoj', 'Chandan', 'Suman Kumar', 'Parmeshwar', 'Jagadish', 'Amit', 'Santosh', 
        'Suman', 'Siddharth', 'Anant', 'Tushar', 'Harbhajan', 'Durgesh', 'Laxminarayan', 'Nirmal', 'Raman', 'Gangaadhar', 'Krishandev', 
        'Ravi Shankar', 'Harishchandra', 'Prithviraj', 'Girish', 'Rajkumar', 'Kishen', 'Suresh', 'Nandkishore', 'Suraj', 'Vikash', 'Tanuj', 
        'Piyush', 'Nandan', 'Jai', 'Chandrikant', 'Vikram', 'Raghavendra', 'Ashok', 'Krishna', 'Sanjay', 'Biharilal', 'Ravindra Singh', 
        'Shivendra', 'Deendayal', 'Tanu', 'Shankar Prasad', 'Harendra', 'Vishwajeet', 'Krishnan', 'Nayan', 'Niranjan', 'Ramesh', 'Shyam', 
        'Dhanraj', 'Saurabh', 'Manojendra', 'Raj', 'Narayan', 'Kripal', 'Krishan Pal', 'Kailas', 'Balram', 'Pranav', 'Hemant', 'Vikramaditya', 
        'Tej Singh', 'Dharmendra', 'Mahendra', 'Deepak', 'Rohan Kumar', 'Sumanth', 'Ankit', 'Charan', 'Kailashchandra', 'Kushal', 'Kartik', 
        'Mohan', 'Gulab', 'Ashish', 'Pradeep', 'Chandrakishore', 'Pritam', 'Manish', 'Virendra', 'Krishan', 'Vijay', 'Pranjal', 'Jagannath', 
        'Yash', 'Tejpal', 'Nirav', 'Navin', 'Dinesh', 'Chandran', 'Jitendra', 'Rajat', 'Ravindra', 'Chandrakant', 'Mukesh', 'Rajendra', 
        'Anirudh', 'Vijender', 'Devraj', 'Manoj Kumar', 'Suraj Kumar', 'Tejendra', 'Vivekanand', 'Mahavir', 'Vishal Kumar', 'Jagat', 
        'Aaditya', 'Gulzar', 'Chandra', 'Mithun', 'Gauransh', 'Chandrapal', 'Prashant', 'Shashank', 'Harishankar', 'Lalit Kumar', 'Hemraj', 
        'Mudit', 'Tejasvi', 'Kiran', 'Madhav', 'Jayesh', 'Vinay', 'Kailashnath', 'Nashit', 'Nandu', 'Chhagan', 'Indranil', 'Abhishek', 
        'Chhatrapal', 'Govind', 'Brahma', 'Chintan', 'Raghav', 'Pawan', 'Jagatveer', 'Dineshwar', 'Rameshwar', 'Arjun', 'Vishnu', 'Mithilesh', 
        'Aakash', 'Bhavesh', 'Kanshi', 'Jaswant', 'Rishabh', 'Sushant', 'Yogesh', 'Ishwar', 'Rohan', 'Sandeep', 'Rajendra Prasad', 'Bhojraj', 
        'Kartikay', 'Raghunath', 'Tejas', 'Harish', 'Omkar', 'Swaraj', 'Vishal', 'Shyam Sundar', 'Lakhan', 'Brijesh', 'Balkishan', 'Ganpat', 
        'Vivek', 'Krishna Prasad', 'Manik', 'Deepankar', 'Shankar Singh', 'Ajay', 'Madhur', 'Prabhat', 'Virat', 'Laxman', 'Avinash', 'Pravin', 
        'Madhusudan', 'Shankar', 'Satyendra', 'Kundan', 'Yogendra', 'Rohit', 'Mahesh', 'Yashpal', 'Nikhil', 'Uday', 'Gopal', 'Kailash', 'Manav', 
        'Punit', 'Jaiwant', 'Vishnuprasad', 'Chirag', 'Balveer', 'Vikrant', 'Rajender Kumar', 'Paras', 'Omprakash', 'Vikramjeet', 'Devendra', 
        'Ravi', 'Aarav', 'Inder', 'Chandresh', 'Karan', 'Arvind', 'Sudhir', 'Pushkar', 'Babu', 'Pankaj', 'Ganesh', 'Surendra', 'Rakesh', 
        'Kalyan', 'Gaurav', 'Deependra', 'Sujay', 'Anil', 'Amitesh', 'Rajesh', 'Naveen', 'Ishaan', 'Umesh', 'Bipin', 'Gokul', 'Bhanu', 
        'Balaram', 'Lalit', 'Nitin', 'Dushyant', 'Lakshman', 'Yogeshwar', 'Sanjiv', 'Kishore', 'Prakash', 'Rajender', 'Siddhesh', 'Madan', 
        'Jai Kishan', 'Raghuraj', 'Shivraj', 'Jayant', 'Vandit', 'Umesh Kumar']


    # chattisgarh Male Surnames
    chhattisgarh_male_surname= [
        'Kushwaha', 'Soni', 'Tiwari', 'Khalifa', 'Sardar', 'Kansari', 'Baria', 'Pandey', 'Rai', 'Bhande', 'Gulzar', 'Lohar', 'Rajput', 
        'Chandrawanshi', 'Chhattisgarhiya', 'Bajpayee', 'Chitariya', 'Baghel', 'Sahu', 'Shrivastava', 'Dikshit', 'Bhil', 'Ratan', 'Puwar', 
        'Rawat', 'Kadam', 'Sarin', 'Sundrani', 'Sarkar', 'Disha', 'Shukla', 'Kachhap', 'Chawan', 'Gupta', 'Chandar', 'Negi', 'Dewangan', 'Nayak', 
        'Bhotia', 'Pillai', 'Upadhyay', 'Manjhi', 'Malik', 'Hirwani', 'Hoo', 'Mishri', 'Raghunath', 'Saray', 'Mishra', 'Arvind', 'Sushil', 
        'Kothari', 'Pujari', 'Nihal', 'Maravi', 'Das', 'Parmar', 'Bhushan', 'Kumawat', 'Jaiswani', 'Gandhi', 'Singh', 'Patwardhan', 'Pratap', 
        'Jadhavpuri', 'Suresh', 'Kachhwa', 'Jogi', 'Bhagat', 'Mathur', 'Teg', 'Yadav', 'Rani', 'Devpura', 'Bhat', 'Chaudhary', 'Garg', 'Majhi', 
        'Jaiswal', 'Nand', 'Adhikari', 'Agarwal', 'Dewange', 'Ravindra', 'Ahuja', 'Dhakad', 'Chhipa', 'Sahai', 'Thokar', 'Agrawal', 'Chouhan', 
        'Raval', 'Salve', 'Kheda', 'Kailash', 'Bansal', 'Sethi', 'Pahuja', 'Bhatt', 'Sareen', 'Mithilesh', 'Chandran', 'Dudhva', 'Bairagi', 
        'Kandala', 'Mahato', 'Baiga', 'Verma', 'Raghav', 'Radheshyam', 'Raut', 'Mahant', 'Rishav', 'Dewani', 'Bhandari', 'Mahana', 'Poddar', 
        'Kadli', 'Khatik', 'Garasiya', 'Sutar', 'Kishore', 'Sharma', 'Chaurasia', 'Modi', 'Kund', 'Munda', 'Koshik', 'Mahindra', 'Dhruv', 
        'Khuntia', 'Varma', 'Panchal', 'Kumar', 'Nirmal', 'Pandit', 'Prajapati', 'Kusum', 'Rathore', 'Mathews', 'Hirpara', 'Dharam', 'Bodh', 
        'Shekhawat', 'Patwari', 'Madhya', 'Ojh', 'Kuswaha', 'Pradhan', 'Brahman', 'Bendre', 'Chhalla', 'Kamath', 'Khalid', 'Vaghela', 'Tomar', 
        'Kharwar', 'Singhvi', 'Jadhav', 'Kale', 'Pasi', 'Kumbhakarna', 'Dewan', 'Sardana', 'Kalki', 'Rana', 'Mehta', 'Rathi', 'Pal', 'Panwar', 
        'Mundra', 'Kariya', 'Nagvanshi', 'Rajwar', 'Suryawanshi', 'Santhia', 'Sain', 'Gautam', 'Bastia', 'Kalia', 'Chikna', 'Gavandi', 
        'Kshatriya', 'Barman', 'Bihari', 'Wadhwa', 'Adivasi', 'Baira', 'Lal', 'Kansara', 'Dandekar', 'Nadkarni', 'Gond', 'Vidyarthi', 
        'Shindore', 'Sanghvi', 'Biswas', 'Bhujel', 'Mahapatra', 'Sah', 'Chaurasiya', 'Waghmare', 'Kaushal', 'Jaisal', 'Murmu', 'Sonkar', 
        'Chandela', 'Girela', 'Gurjar', 'Shinde', 'Tandel', 'Chandok', 'Suryakant', 'Trivedi', 'Vishwakarma', 'Gajbhiye', 'Thakur', 'Gope', 
        'Yadava', 'Bhaure', 'Chandravanshi', 'Yashwanshi', 'Mahajan', 'Mandavi', 'Mahale', 'Jain', 'Banjara', 'Shubham', 'Dubey', 'Dawra', 
        'Khare', 'Goswami', 'Bhuriya', 'Shekhar', 'Gore', 'Dangi', 'Mote', 'Kachroo']


    # chattisgarh Female First Names
    chhattisgarh_female_firstname = [
        'Bela', 'Geet', 'Chandni', 'Champa', 'Alpana', 'Aadya', 'Preeti', 'Rashmi', 'Shruti', 'Shalini', 'Shivani', 'Ganga', 'Sarika', 
        'Rukmini', 'Aanchal', 'Mansi', 'Parul', 'Pooja', 'Hemalata', 'Anjali', 'Kavita', 'Savitri', 'Isha', 'Madhuri', 'Aarti', 'Parvati', 
        'Urmila', 'Chandrika', 'Lakshmi', 'Ananya', 'Priti', 'Savita', 'Neha', 'Swati', 'Manju', 'Bindu', 'Rekha', 'Snehal', 'Tara', 'Sangeeta', 
        'Nisha', 'Lata', 'Ragini', 'Swarnima', 'Anju', 'Ranjana', 'Bhawna', 'Nita', 'Priya', 'Chhavi', 'Nidhi', 'Rishika', 'Chitra', 'Rati', 
        'Sundari', 'Geeta', 'Trisha', 'Bhairavi', 'Nutan', 'Sakhi', 'Bina', 'Arpita', 'Jaya', 'Sanyogita', 'Shashi', 'Jaspreet', 'Alka', 'Radha', 
        'Bhavana', 'Madhavi', 'Radhika', 'Seema', 'Gungun', 'Ishwari', 'Bhavya', 'Ravi', 'Chitrani', 'Shree', 'Narmada', 'Charulata', 'Sashi', 
        'Pavitra', 'Chandana', 'Sudha', 'Sunita', 'Deepa', 'Bhavna', 'Sana', 'Subha', 'Vidya', 'Yashoda', 'Maya', 'Dulari', 'Kriti', 'Tulsi', 
        'Sushma', 'Barkha', 'Tanuja', 'Shilpa', 'Kajal', 'Kamala', 'Sushila', 'Pranjal', 'Shubhi', 'Kashish', 'Kumud', 'Meera', 'Rani', 'Lalitha', 
        'Nikita', 'Jagrati', 'Basanti', 'Nirmala', 'Lakshita', 'Bansari', 'Yashika', 'Kamini', 'Gulika', 'Charul', 'Sakshi', 'Vandana', 'Rupali', 
        'Ishita', 'Saraswati', 'Kanak', 'Dhanashree', 'Gayatri', 'Chitralekha', 'Vasundhara', 'Nandini', 'Sushmita', 'Triveni', 'Abha', 'Vandita', 
        'Krishna', 'Smita', 'Shanti', 'Sita', 'Babli', 'Suman', 'Neelam', 'Rupa', 'Devika', 'Kalyani', 'Anshika', 'Tanu', 'Rama', 'Dayita', 
        'Tulika', 'Poonam', 'Indira', 'Durga', 'Lalita', 'Kirti', 'Mukti', 'Vasudha', 'Shobha', 'Ujjwala', 'Pallavi', 'Yamini', 'Shraddha', 
        'Madhurima', 'Kalpana', 'Gauri', 'Asha', 'Kiran', 'Madhvi', 'Meenal', 'Geetanjali']

    chhattisgarh_female_surname = [
        'Sharma', 'Garasiya', 'Panchal', 'Saray', 'Barman', 'Manjhi', 'Hirpara', 'Rajput', 'Sain', 'Shukla', 'Kachroo', 'Suresh', 'Radheshyam', 
        'Dhakad', 'Jaiswal', 'Banjara', 'Wadhwa', 'Singhvi', 'Kheda', 'Kund', 'Rathi', 'Kumari', 'Bhil', 'Chhattisgarhiya', 'Nirmal', 'Baiga', 
        'Gore', 'Nagvanshi', 'Shrivastava', 'Kishore', 'Mahindra', 'Bendre', 'Gavandi', 'Kumbhakarna', 'Mishri', 'Koshik', 'Chandravanshi', 
        'Pradhan', 'Kadli', 'Kumawat', 'Singh', 'Malik', 'Sanghvi', 'Hoo', 'Madhya', 'Sonkar', 'Mishra', 'Bhaure', 'Gurjar', 'Modi', 'Kumar', 
        'Murmu', 'Tomar', 'Sarin', 'Kalki', 'Kamath', 'Rawat', 'Kailash', 'Mahana', 'Thokar', 'Nihal', 'Baghel', 'Sahu', 'Khare', 'Kothari', 
        'Jadhav', 'Gope', 'Kaushal', 'Chaurasiya', 'Chawan', 'Tiwari', 'Dawra', 'Garg', 'Trivedi', 'Kshatriya', 'Lohar', 'Thakur', 'Dikshit', 
        'Chandrawanshi', 'Chitariya', 'Chhipa', 'Nand', 'Prajapati', 'Khalifa', 'Kachhwa', 'Gond', 'Kansara', 'Adivasi', 'Ravindra', 'Panwar', 
        'Soni', 'Bansal', 'Suryakant', 'Munda', 'Goswami', 'Raghav', 'Shubham', 'Girela', 'Rishav', 'Chhalla', 'Mahajan', 'Chandar', 'Kachhap', 
        'Sundrani', 'Majhi', 'Arvind', 'Rathore', 'Dewange', 'Jogi', 'Kusum', 'Jaiswani', 'Baira', 'Santhia', 'Chikna', 'Pillai', 'Verma', 
        'Poddar', 'Kadam', 'Bhujel', 'Dewani', 'Biswas', 'Agrawal', 'Kharwar', 'Tandel', 'Bhagat', 'Chouhan', 'Varma', 'Bhushan', 'Khalid', 
        'Shinde', 'Raut', 'Ojh', 'Bhandari', 'Negi', 'Salve', 'Bastia', 'Disha', 'Sareen', 'Jadhavpuri', 'Lal', 'Sarkar', 'Kansari', 'Bhatt', 
        'Dandekar', 'Pasi', 'Kalia', 'Kariya', 'Dharam', 'Dudhva', 'Chaurasia', 'Dangi', 'Mithilesh', 'Bhotia', 'Suryawanshi', 'Teg', 'Jaisal', 
        'Agarwal', 'Khuntia', 'Bodh', 'Kushwaha', 'Yashwanshi', 'Bihari', 'Pahuja', 'Yadav', 'Baria', 'Rana', 'Bajpayee', 'Pandey', 'Sutar', 
        'Mahato', 'Gandhi', 'Maravi', 'Gautam', 'Das', 'Gulzar', 'Chaudhary', 'Vishwakarma', 'Chandran', 'Adhikari', 'Mathur', 'Mandavi', 
        'Rajwar', 'Gajbhiye', 'Mundra', 'Nayak', 'Pandit', 'Brahman', 'Khatik', 'Bairagi', 'Bhuriya', 'Ahuja', 'Mahant', 'Puwar', 'Devpura', 
        'Kale', 'Patwari', 'Rai', 'Gupta', 'Mahale', 'Kandala', 'Chandela', 'Rani', 'Dewangan', 'Chandok', 'Ratan', 'Jain', 'Yadava', 'Shindore', 
        'Kuswaha', 'Shekhawat', 'Mathews', 'Pratap', 'Dhruv', 'Sardar', 'Bhat', 'Mote', 'Hirwani']
    
    chhattisgarh_female_suffix = [ 
        "kumari", "amma", "devi", " ", " ", " ", " ", " "]


# Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(chhattisgarh_male_firstname)
        last_name_male = random.choice(chhattisgarh_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(chhattisgarh_female_firstname)
        last_name_female = random.choice(chhattisgarh_female_surname)
        suffix_female = random.choice(chhattisgarh_female_suffix)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female + " " + suffix_female  # Full name with suffix

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female.strip(), "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_chhattisgarh_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df

