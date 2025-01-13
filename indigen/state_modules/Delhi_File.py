import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_delhi_names(n, user_preference=None):
    # delhi Male First name
    delhi_male_firstname = [
        'Tejinder', 'Pankaj', 'Vineet', 'Vikash', 'Atul', 'Mitesh', 'Harinder', 'Harjeet', 'Yogesh', 'Madhav', 'Akshay', 'Raghvendra', 'Darshan', 'Nilesh', 'Sanjiv', 'Puneet',
        'Shamsher', 'Dinesh', 'Sudhanshu', 'Arun', 'Bhavesh', 'Deepak', 'Raghav', 'Sharad', 'Ashish', 'Sharv', 'Chirag', 'Somesh', 'Kunal', 'Ishwar', 'Girish', 'Sohan', 'Gaurav',
        'Sushil', 'Ayush', 'Tushar', 'Virendra', 'Saurabh', 'Naren', 'Umesh', 'Mohan', 'Siddhanth', 'Brijesh', 'Vijay', 'Nirbhay', 'Devesh', 'Saurav', 'Rahul', 'Aarav', 'Anish',
        'Inderjit', 'Indrajit', 'Sunil', 'Yogendra', 'Pravin', 'Dhruv', 'Adarsh', 'Sandeep', 'Nikhil', 'Ashwin', 'Avinash', 'Ansh', 'Gyan', 'Chandan', 'Lakhan', 'Hari', 'Kartik',
        'Rohit', 'Jitender', 'Keshav', 'Tanu', 'Devendra', 'Harish', 'Vinay', 'Bishal', 'Ketan', 'Jaspreet', 'Jitendra', 'Raj', 'Arjun', 'Dhanraj', 'Manish', 'Devansh',
        'Ashutosh', 'Vimal', 'Rajiv', 'Siddharth', 'Nitesh', 'Jai', 'Dheeraj', 'Nashit', 'Bhavik', 'Chandresh', 'Prakash', 'Shankar', 'Rakesh', 'Raghavendra', 'Mithun',
        'Madhur', 'Hemant', 'Pradeep', 'Suraj', 'Ravi', 'Shivansh', 'Sarthak', 'Vishal', 'Sumeet', 'Rajesh', 'Manoj', 'Aman', 'Aayush', 'Mukul', 'Vivek', 'Jeevan', 'Shashank', 'Vikas',
        'Vikram', 'Vasudev', 'Basant', 'Kailash', 'Rajeev', 'Ashok', 'Chetan', 'Harpreet', 'Suman', 'Virender', 'Shashwat', 'Gokul', 'Parveen', 'Alok', 'Jayant', 'Jitesh',
        'Omkar', 'Vaibhav', 'Kashish', 'Jatin', 'Nirav', 'Ishaan', 'Tarun', 'Harvinder', 'Bhupendra', 'Surendra', 'Vansh', 'Aakash', 'Lalit', 'Ravindra', 'Anurag', 'Shahid', 'Bhanu',
        'Rajendra', 'Krishna', 'Virat', 'Akhil', 'Rohan', 'Sohail', 'Ankit', 'Lakshay', 'Arvind', 'Subhash', 'Luv', 'Sanjay', 'Dev', 'Dharmendra', 'Kushal', 'Uday', 'Nitin', 'Nakul',
        'Om', 'Abhishek', 'Abhinav', 'Anil', 'Bharat', 'Mayank', 'Shailendra', 'Prem', 'Shivendra','Sahil', 'Tanmay', 'Pranav', 'Sushant', 'Karan', 'Hitesh', 'Suresh', 'Mithilesh', 'Gurpreet', 'Yash', 'Aaditya', 'Praveen', 'Ujjwal']
    # delhi Female First name
    delhi_female_firstname = [
        'Tanuja', 'Deepali', 'Divya', 'Rupa', 'Chitrani', 'Kavita', 'Deepika', 'Aaradhya', 'Arpita', 'Rakhi', 'Shweta', 'Ishita', 'Sharanya', 
        'Sheetal', 'Shubhi', 'Sadhna', 'Ankita', 'Geetika', 'Vishali', 'Kumari', 'Nisha', 'Sonali', 'Namrata', 'Aradhana', 'Vishakha', 'Shruti', 
        'Usha', 'Shilpa', 'Rekha', 'Rashi', 'Madhuri', 'Lalita', 'Ujjwala', 'Kamini', 'Gargi', 'Saniya', 'Minal', 'Alisha', 'Aishwarya', 'Gitanjali', 
        'Akanksha', 'Barkha', 'Sonia', 'Sheela', 'Sanya', 'Bina', 'Priya', 'Sarika', 'Juhi', 'Swati', 'Gayatri', 'Divisha', 'Vaishali', 'Poonam', 
        'Chandana', 'Aarushi', 'Gita', 'Chanchal', 'Pallavi', 'Sonal', 'Sweta', 'Archana', 'Isha', 'Purnima', 'Sumantra', 'Sunita', 'Aakriti', 
        'Tanya', 'Kajal', 'Durga', 'Charul', 'Kriti', 'Komal', 'Monika', 'Anamika', 'Aditi', 'Urmi', 'Jaya', 'Sapna', 'Shalini', 'Samantha', 
        'Sharmila', 'Ananya', 'Alokita', 'Preeti', 'Yogita', 'Renu', 'Amisha', 'Laxmi', 'Seema', 'Vaidehi', 'Avni', 'Nandini', 'Varsha', 'Shivani', 
        'Urvesh', 'Urmila', 'Vaishnavi', 'Rupal', 'Deepshikha', 'Vandana', 'Sakshi', 'Trisha', 'Bhavana', 'Pragya', 'Neelam', 'Vidya', 'Vidhi', 
        'Chandni', 'Hema', 'Ravina', 'Ritika', 'Tanu', 'Bhumika', 'Chavi', 'Deeksha', 'Nikita', 'Ekta', 'Yamini', 'Neha', 'Meera', 'Suman', 'Kiran', 
        'Kavya', 'Rita', 'Sangeeta', 'Diksha', 'Amita', 'Simran', 'Chhavi', 'Madhavi', 'Radhika', 'Veena', 'Tanvi', 'Deepa', 'Sneha', 'Meenal', 
        'Surbhi', 'Indu', 'Shraddha', 'Anjali', 'Manisha', 'Rupali', 'Aarti', 'Indira', 'Shabnam', 'Bhavna', 'Karuna', 'Yashika', 'Rina', 'Kumud', 
        'Vibha', 'Pooja', 'Sarla', 'Jagruti', 'Chhaya', 'Arti', 'Charvi', 'Anju', 'Shikha', 'Ruchi', 'Bharti', 'Manju', 'Pranjal', 'Disha', 'Kirti', 
        'Vanshika', 'Bhavya']

    delhi_surname = [
                'Narang', 'Goenka', 'Jain', 'Brahman', 'Nath', 'Pahwa', 'Khullar', 'Bali', 'Sundriyal', 'Malhotra', 'Khurana', 'Bajpai', 
                 'Singla', 'Tanwar', 'Sahni', 'Hooda', 'Monga', 'Bhagat', 'Goel', 'Vaidya', 'Chauhan', 'Saini', 'Saraf', 'Kadian', 'Gahlot', 
                 'Sharma', 'Mangal', 'Mathur', 'Bhatia', 'Chaturvedi', 'Dixit', 'Rastogi', 'Rangra', 'Jindal', 'Yadav', 'Khatri', 'Bhargav', 
                 'Rajora', 'Mehta', 'Sachdeva', 'Anand', 'Rohilla', 'Arora', 'Kumar', 'Joshi', 'Pande', 'Gulati', 'Bihari', 'Mishra', 'Bansal', 
                 'Thakur', 'Rajput', 'Vaid', 'Rana', 'Soni', 'Chawla', 'Kushwaha', 'Suri', 'Rathi', 'Nand', 'Tripathi', 'Dhawan', 'Mehrotra', 
                 'Jagga', 'Bhatt', 'Choudhury', 'Goswami', 'Gupta', 'Nambiar', 'Luthra', 'Rathore', 'Sood', 'Chaudhary', 'Agarwal', 'Chopra', 
                 'Panchal', 'Singh', 'Kashyap', 'Nanda', 'Kapoor', 'Vishwakarma', 'Sarkar', 'Ranjan', 'Goyal', 'Sangwan', 'Chhabra', 'Maheshwari', 
                 'Bajwa', 'Lamba', 'Bagga', 'Pandey', 'Chand', 'Chhikara', 'Kapur', 'Talwar', 'Chadha', 'Awasthi', 'Parmar', 'Sethi', 'Wadhwa', 
                 'Bishnoi', 'Madaan', 'Khanna', 'Kohli', 'Tiwari', 'Khandelwal', 'Vohra', 'Kumawat', 'Bhargava', 'Chandel', 'Bhardwaj', 'Narayan', 
                 'Sodhi', 'Bisht', 'Verma', 'Bedi', 'Sarin', 'Shukla', 'Dua', 'Garg', 'Nagpal','Kandpal', 'Puri', 'Mittal', 'Mahajan', 'Bhandari', 
                 'Chandna', 'Saxena', 'Tandon']

    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(delhi_male_firstname)
        last_name_male = random.choice(delhi_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(delhi_female_firstname)
        last_name_female = random.choice(delhi_surname)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female  # Full name

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Ensure file writing happens
    file_path = 'generated_delhi_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df