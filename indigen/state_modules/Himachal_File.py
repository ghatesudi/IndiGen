import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Himachal Male and Female First Names and Surnames
def generate_himachal_names(n, user_preference=None):

    # Himachal Male First Names
    himachal_male_firstnames = [
        'Mohit', 'Lokesh', 'Virendra', 'Vinay', 'Madan', 'Chandra', 'Abhay', 'Rajinder', 'Ashwani', 'Pakanj', 'Nitin', 'Karna', 'Piyush', 
        'Rajesh', 'Pranav', 'Parveen', 'Som', 'Karan', 'Karthik', 'Kishore', 'Atul', 'Jitendra', 'Vijay', 'Sameer', 'Manoj', 'Ajay', 'Uday', 
        'Harinder', 'Gaurav', 'Padam', 'Gulshan', 'Shashi', 'Sonam', 'Lalit', 'Baldev', 'Paras', 'Abhinav', 'Kushal', 'Ravinder', 'Anup', 'Raman', 
        'Vikram', 'Karma', 'Amit', 'Gagan', 'Mahesh', 'Vineet', 'Amitabh', 'Baljeet', 'Rajat', 'Harish', 'Saurabh', 'Avinash', 'Surajpal', 
        'Akshit', 'Kunal', 'Pradeep', 'Naresh', 'Kesar', 'Vinod', 'Rajbir', 'Narendra', 'Vivek', 'Sher', 'Dinesh', 'Bhupender', 'Sushil', 'Om', 
        'Pravesh', 'Ankit', 'Yudhveer', 'Kamaldeep', 'Tarun', 'Ramphal', 'Subash', 'Rakesh', 'Dixit', 'Shyam', 'Sunil', 'Raj', 'Ajit', 'Tejinder', 
        'Yashwant', 'Prakash', 'Rajiv', 'Inderpal', 'Nikhil', 'Parminder', 'Surender', 'Deep', 'Hrithik', 'Jasbir', 'Rabindra', 'Ghanshyam', 
        'Arjun', 'Ashok', 'Raghunandan', 'Joginder', 'Devi', 'Anshul', 'Nitish', 'Chandrapal', 'Panma', 'Ratan', 'Shiva', 'Rohit', 'Munish', 
        'Pardeep', 'Santosh', 'Ayush', 'Veer', 'Guru', 'Daya', 'Kuldeep', 'Jaswinder', 'Ankur', 'Tej Singh', 'Lal', 'Shiv', 'Rahul', 'Dharma', 
        'Pawan', 'Harpal', 'Suresh', 'Puneet', 'Ashvin', 'Sachin', 'Anil', 'Anish', 'Mahendra', 'Aditya', 'Ashutosh', 'Balram', 'Krishna', 
        'Tashi', 'Bajrang', 'Bhim', 'Kundan', 'Shaktiprakash', 'Harishchandra', 'Ratan Singh', 'Raghav', 'Durga', 'Nand Kishore', 'Sham', 
        'Sangram', 'Abhishek', 'Rajan', 'Ram', 'Ashish', 'Keshav', 'Prashant', 'Sanjay', 'Jaideep', 'Sahdev', 'Devesh', 'Gurvinder', 'Inder', 
        'Rajeev', 'Vikramjeet', 'Madhav', 'Ankush', 'Sanjeev', 'Akash', 'Bishan', 'Vikas', 'Maharaj Singh', 'Nitesh', 'Tejas', 'Aman', 'Jagat', 
        'Sukhdev', 'Jagtar', 'Bharat', 'Amar', 'Dheeraj', 'Vikrant', 'Mukul', 'Sunny', 'Neeraj', 'Anand', 'Akhil', 'Indra', 'Himanshu', 'Harsh', 
        'Brij', 'Raghavendra', 'Chaman', 'Rajveer', 'Manpreet', 'Umesh', 'Dhruv', 'Mukesh', 'Anmol', 'Shubham', 'Shivam', 'Yogendra', 'Ravi', 
        'Hemant', 'Anuj', 'Naveen', 'Chetan', 'Bhawani Singh', 'Arvind', 'Aryan', 'Sumeet', 'Rajneesh', 'Rishi', 'Kunwar', 'Shankar', 'Gopal', 
        'Bal', 'Harvinder', 'Jatin', 'Jasvir', 'Yashpal', 'Praveen', 'Kapil', 'Heera', 'Surendra', 'Tanuj', 'Sandeep', 'Devansh', 'Hari', 
        'Subhash', 'Jai', 'Ravindra', 'Narender', 'Bikram', 'Harjeet', 'Jagdish', 'Varun', 'Prince', 'Manojveer', 'Kesar Singh', 'Sahil', 
        'Ganesh', 'Dharmendra', 'Prem', 'Mohan', 'Thakur', 'Nishant', 'Sagar', 'Gurmeet', 'Rishabh', 'Rajendra', 'Devender', 'Jeevan', 'Suraj', 
        'Virender', 'Narinder', 'Dev', 'Kishan', 'Nirbhay', 'Uttam', 'Hem', 'Deepak', 'Vishal', 'Bhupendra', 'Gurpreet', 'Rameshwar', 'Brijendra', 
        'Tejpal', 'Akshay', 'Mandeep', 'Yash', 'Tej', 'Satish', 'Kamal', 'Govind', 'Ranjit', 'Pankaj', 'Sumit', 'Arun', 'Sourav', 'Shivendra', 
        'Tariq', 'Krishan', 'Manish', 'Ramesh', 'Gur', 'Yogesh', 'Hitesh', 'Bhimsen']

    # Himachal Male Surnames
    himachal_male_surnames = [
        'Kapoor', 'Beniwal', 'Misra', 'Tashi', 'Chandran', 'Rathi', 'Kushwaha', 'Balmiki', 'Bumde', 'Shekhawat', 'Dixit', 
        'Chandel', 'Sikarwar', 'Rastogi', 'Rathod', 'Bagaria', 'Lohar', 'Tripathi', 'Pundir', 'Mehra', 'Paliwal', 'Kothari', 
        'Yunthang', 'Awasthi', 'Bairwa', 'Rao', 'Rajgarhia', 'Bansal', 'Chaurasia', 'Chauhan', 'Nath', 'Karma', 'Bishnoi', 
        'Gaddi', 'Mali', 'Siwach', 'Yeshe', 'Dorje', 'Gautam', 'Bhatt', 'Bisht', 'Vikram', 'Rana', 'Thakur', 'Chand', 
        'Jangid', 'Purbia', 'Chaudhary', 'Vyas', 'Bhotia', 'Suryavanshi', 'Kumawat', 'Bisen', 'Prasad', 'Yonten', 'Negi', 
        'Lamba', 'Rangar', 'Gupta', 'Rathore', 'Vats', 'Chokpa', 'Bhardwaj', 'Kohli', 'Pant', 'Sood', 'Pandit', 'Maharaj', 
        'Khanna', 'Kashyap', 'Tandon', 'Mori', 'Choden', 'Chohan', 'Dawa', 'Panchal', 'Pratap', 'Semwal', 'Jampa', 
        'Phuntsok', 'Shabnam', 'Pathak', 'Gohil', 'Kaul', 'Tanwar', 'Baghel', 'Mahawar', 'Nautiyal', 'Prajapati', 'Mishra', 
        'Raghav', 'Shastri', 'Chaturvedi', 'Upadhyay', 'Lama', 'Solanki', 'Kumar', 'Rinchen', 'Dhanwade', 'Soni', 'Joshi', 
        'Bajpai', 'Choudhary', 'Kundra', 'Bhandari', 'Rajput', 'Nyima', 'Chandela', 'Jadeja', 'Lobsang', 'Gahlot', 'Chamar', 
        'Ngawang', 'Mawpa', 'Saxena', 'Yangchen', 'Sharma', 'Yadav', 'Tiwari', 'Tsering', 'Pathania', 'Hada', 'Tenzin', 'Singh', 
        'Dubey', 'Vishwakarma', 'Shukla', 'Koli', 'Pema', 'Trivedi', 'Gahoi', 'Jain', 'Jai', 'Kachhawa', 'Sonam', 'Tomar', 'Rai', 
        'Sahni', 'Gorakh', 'Rawat', 'Pandey', 'Chopra', 'Sengar', 'Agarwal', 'Tshering', 'Kadian', 'Bhavsar']


    # Himachal Female First Names
    himachal_female_firstnames = [
        'Sangeeta', 'Tashi', 'Anjana', 'Snehal', 'Rashmi', 'Priyanka', 'Minakshi', 'Anu', 'Shivani', 'Ritika', 'Geetika', 
        'Deepa', 'Lalita', 'Radha', 'Charul', 'Sakshi', 'Renu', 'Aarti', 'Ranjana', 'Kanchan', 'Tamanna', 'Shreya', 'Suhana', 'Padma', 
        'Parveen', 'Sonu', 'Chandni', 'Priya', 'Niharika', 'Meenakshi', 'Aditi', 'Tanu', 'Shalu', 'Ankita', 'Urmila', 'Gita', 'Anupama', 
        'Vanita', 'Pranjali', 'Kamlesh', 'Nikita', 'Vandana', 'Kashish', 'Maya', 'Ravita', 'Shanti', 'Indra', 'Poonam', 'Sheetal', 'Tara', 
        'Sonia', 'Shanta', 'Madhavi', 'Shobha', 'Madhu', 'Laxmi', 'Rita', 'Sonal', 'Pushpa', 'Champa', 'Anjali', 'Kavita', 'Jaspreet', 
        'Ragini', 'Neelam', 'Monica', 'Anuradha', 'Jayshree', 'Kajal', 'Meera', 'Yashika', 'Shweta', 'Pratibha', 'Kumud', 'Manisha', 
        'Isha', 'Santosh', 'Tanvi', 'Dolma', 'Pooja', 'Shakti', 'Madhuri', 'Preeti', 'Sushma', 'Sonam', 'Rupali', 'Leela', 'Kanta', 
        'Nidhi', 'Sadhna', 'Sumantha', 'Sarika', 'Radhika', 'Ritu', 'Aruna', 'Simran', 'Kesar', 'Swati', 'Rakhi', 'Babita', 'Rama', 
        'Nisha', 'Kiran', 'Chandra', 'Alka', 'Neha', 'Rachna', 'Divya', 'Payal', 'Deeksha', 'Bindu', 'Savita', 'Anju', 'Jyoti', 'Kusum', 
        'Yasmin', 'Sonali', 'Bhavika', 'Komal', 'Monika', 'Srishti', 'Palak', 'Asha', 'Nutan', 'Meenal', 'Norbu', 'Shikha', 'Dawa', 'Bimla', 
        'Indu', 'Mamta', 'Usha', 'Rukmini', 'Bhavna', 'Rajkumari', 'Sunita', 'Uma', 'Kanika', 'Rekha', 'Nirmala', 'Dimple', 'Tanuja', 'Raksha', 
        'Deepika', 'Prem', 'Anita', 'Sapna', 'Tenzin', 'Aanchal', 'Shalini', 'Pinky', 'Bimala', 'Reena', 'Aishwarya', 'Naina', 'Pallavi', 
        'Sadhana', 'Bharti', 'Ruchi', 'Saroj', 'Sarita', 'Parul', 'Kritika', 'Rajni', 'Riya', 'Praveen', 'Bhawna', 'Seema', 'Shashi', 'Nancy', 
        'Lata', 'Veena', 'Geeta', 'Indira', 'Vandita', 'Kalpana', 'Sahiba', 'Manju', 'Meena', 'Kamini', 'Suman', 'Krishna', 'Neetu', 'Sita', 
        'Akanksha', 'Shilpa', 'Rani']

    # Himachal Female Surnames
    himachal_female_surnames = [
        'Gautam', 'Bhavsar', 'Sharma', 'Lobsang', 'Mawpa', 'Panchal', 'Chaudhary', 'Dubey', 'Gahoi', 'Pathak', 'Tsering', 'Rai', 'Tiwari', 
        'Tanwar', 'Rastogi', 'Saxena', 'Kundra', 'Sahni', 'Karma', 'Beniwal', 'Rinchen', 'Purbia', 'Khanna', 'Siwach', 'Thakur', 'Rajgarhia', 
        'Tripathi', 'Bansal', 'Gohil', 'Nath', 'Lamba', 'Paliwal', 'Chauhan', 'Negi', 'Rathore', 'Jampa', 'Rathod', 'Dhanwade', 'Kumar', 
        'Pandey', 'Yadav', 'Bhardwaj', 'Sonam', 'Nautiyal', 'Chopra', 'Lohar', 'Trivedi', 'Pathania', 'Mali', 'Gorakh', 'Chamar', 'Jadeja', 
        'Tashi', 'Joshi', 'Bhotia', 'Gupta', 'Kushwaha', 'Gaddi', 'Tandon', 'Chaturvedi', 'Kashyap', 'Phuntsok', 'Bishnoi', 'Kaul', 'Kumawat', 
        'Choudhary', 'Chand', 'Singh', 'Chandel', 'Baghel', 'Semwal', 'Mori', 'Bagaria', 'Mahawar', 'Pratap', 'Shabnam', 'Bajpai', 'Bhatt', 'Pant', 
        'Mehra', 'Kapoor', 'Dixit', 'Jai', 'Chohan', 'Upadhyay', 'Kothari', 'Tshering', 'Chandran', 'Dawa', 'Misra', 'Shekhawat', 'Kohli', 'Pundir', 
        'Balmiki', 'Raghav', 'Rathi', 'Prasad', 'Awasthi', 'Yonten', 'Gahlot', 'Yeshe', 'Agarwal', 'Vikram', 'Suryavanshi', 'Bisht', 'Rawat', 
        'Pema', 'Sengar', 'Choden', 'Nyima', 'Shukla', 'Vyas', 'Mishra', 'Chaurasia', 'Vishwakarma', 'Vats', 'Shastri', 'Soni', 'Koli', 'Bisen', 
        'Jangid', 'Tenzin', 'Sood', 'Rao', 'Prajapati', 'Solanki', 'Rangar', 'Maharaj', 'Pandit', 'Lama', 'Kachhawa', 'Tomar', 'Bhandari', 'Kadian', 
        'Rajput', 'Rana', 'Bairwa', 'Yunthang', 'Ngawang', 'Chandela', 'Jain', 'Dorje', 'Sikarwar', 'Bumde', 'Yangchen', 'Chokpa', 'Hada']

     # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(himachal_male_firstnames)
        last_name_male = random.choice(himachal_male_surnames)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(himachal_female_firstnames)
        last_name_female = random.choice(himachal_female_surnames)

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
    file_path = 'generated_himachal_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df