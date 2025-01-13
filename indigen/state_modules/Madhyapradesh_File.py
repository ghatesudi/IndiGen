import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_madhyapradesh_names(n, user_preference=None):# madhyapradesh Male First name


    # madhyapradesh Male First name
    madhyapradesh_male_firstname=  [
        "Ramlal", "Mohanlal", "Shyamlal", "Raghunathlal", "Vijaylal", "Jailal", "Brijlal", "Nandlal",
        "Ramchand", "Shivchand", "Radhachand", "Bishanchand", "Rameshchand", "Dineshchand", "Harishchand",
        "Ravindrachand", "Manojchand", "Rajendrachand", "Prakashchand", "Sureshchand", "Surajdev", "Ramdev",
        "Shankardev", "Krishnadev", "Brahmadev", "Vishnu-dev", "Mahadev", "Chandresh", "Raghavdas", "Vishnudas",
        "Krishnadas", "Gopaldas", "Shankardas", "Brajdas", "Shivdas", "Ramdas", "Harshdas", "Sundardas",
        "Dineshdas", "Rameshdas", "Bhimasdas", "Manojdas", "Mahendrasdas", "Ganeshdas", "Rajdas", "Arvindlal",
        "Mithileshlal", "Manojlal", "Kailashlal", "Sureshlal", "Chandrakant", "Chandresh", "Vikramlal",
        "Anillal", "Bharatlal", "Krishnalal", "Niranjanlal", "Shivendra", "Ramkishore", "Chandramohan", "Raghavendra",
        "Vishwanath", "Ranjitlal", "Maheshwar", "Ravindra", "Rajkumar", "Kishore", "Anil", "Subhash", "Arvind", "Ashok",
        "Lalit", "Vishal", "Narendra", "Pankaj", "Rajan", "Raghav", "Vikram", "Manoj", "Sushil", "Anil", "Ashoklal",
        "Rameshwar", "Chandrakant", "Prabhakar", "Anilchand", "Mahendra", "Sanjay", "Ravi", "Basant", "Mukesh", "Tushar",
        "Harish", "Jagannath", "Madhusudan", "Nitin", "Amit", "Sunil", "Pradeep", "Tejendra", "Krishan", "Pradeep", "Kailash",
        "Dinesh", "Ravishankar", "Rajendra", "Ashutosh", "Manojdas", "Govind", "Mithilesh", "Jagdish", "Gopal", "Harvinder",
        "Raghunath", "Rajpal", "Narmadaprasad", "Chandrapal", "Raghavpal", "Brijesh", "Nandkishore", "Bhaskar", "Arvinddas",
        "Subodh", "Krishandas", "Raghubir", "Jeevandas", "Tulsidas", "Vinod", "Pritam", "Prashant", "Satyendra", "Narayan",
        "Bhoopendra", "Sohan", "Jitendra", "Gurudev", "Raghunathji", "Dineshji", "Shivaji", "Sureshji", "Balram", "Rajendra",
        "Gaurishankar", "Jaichand", "Vijaydas", "Himanshu", "Sandeep", "Shashikant", "Pritamdas", "Premchand", "Vinodji",
        "Ravindraji", "Subham", "Inderjeet", "Krishnakant", "Santosh", "Yogendra", "Lalchand", "Maheshlal",
        "Ravindrakant", "Bhupendra", "Hiralal", "Madhav", "Sumer", "Ravindrakumar", "Jaishankar", "Prabhu", "Veerendra",
        "Samar", "Dineshji", "Mahadeva", "Ajeet", "Harvinder", "Bhupender", "Laxman", "Nandlal", "Vijendra", "Puneet",
        "Shashank", "Pankajji", "Chandramohanji", "Vikramjit", "Madhusudhanji", "Rameshwarlal", "Ravishankarlal",
        "Satyam", "Pranav", "Kundan", "Sushilji", "Pankajlal", "Chandreshlal", "Ramkishorelal", "Tejpal", "Vishwajeet",
        "Surendra", "Shankarji", "Nirmal", "Chandreshdas", "Rajnish", "Premlal", "Shivendralal", "Vikas", "Raghavendralal",
        "Sureshkumar", "Ramendra", "Lalitbabu", "Rishabh", "Vikash", "Sanjiv", "Madhavendra", "Rajpalji", "Santoshlal",
        "Bharatji", "Raghunathlal", "Shyamji", "Ravidas", "Anirudh", "Basantkumar", "Ashokdas", "Vikrampal", "Harvinderlal",
        "Manojpal", "Amitdas", "Brijendra", "Sandeepkumar", "Suryakant", "Gyanendra", "Rajendrapal", "Himanshulal",
        "Jitender", "Madhurji", "Raviprajapati", "Prempal", "Jitenderlal", "Mukul", "Ravilal", "Shivendrapatel", "Sidharth",
        "Gopalchand", "Bipinlal", "Surajpal","Sushant", "Subramani", "Amritji", "Rohit", "Subodhji", "Umesh",
        "Kishorelal", "Vinodpatel", "Ravindrasdas", "Shivendra", "Tejendralal", "Girish", "Chandran", "Sohanlal", "Narayanlal"]

    #   madhyapradesh Male Surname
    madhyapradesh_male_surname= [
        'Lodha', 'Sharma', 'Bhatti', 'Tripathi', 'Patil', 'Shah', 'Meena', 'Raghav', 'Vashist', 'Bashar', 'Lodh', 'Pattnaik', 'Tiwari', 
        'Giri', 'Kandari', 'Parihar', 'Gandhi', 'Prasad', 'Desai', 'Jalota', 'Gulia', 'Malviya', 'Bohra', 'Bhaskar', 'Agrawal', 'Seth', 
        'Daga', 'Kashyap', 'Bansal', 'Dandotiya', 'Awasthi', 'Karodia', 'Baheti', 'Chand', 'Chandorkar', 'Sodha', 'Goyal', 'Rawat', 'Jain', 
        'Saraf', 'Khare', 'Thakur', 'Patel', 'Agarwal', 'Saxena', 'Mann', 'Laxman', 'Dhamani', 'Nayak', 'Rajput', 'Bairagi', 'Raghuwanshi', 
        'Khatri', 'Dewangan', 'Singh', 'Hada', 'Kapadia', 'Zadafia', 'Chaturvedi', 'Dixit', 'Pandey', 'Gupta', 'Yadav', 'Bharati', 'Soni', 
        'Gohil', 'Verma', 'Kothari', 'Mehra', 'Jadhav', 'Bhatnagar', 'Mungli', 'Bhargava', 'Kataria', 'Kachhadiya', 'Chaudhary', 'Malik', 
        'Deora', 'Mishra', 'Garhwal', 'Panchal', 'Pathak', 'Nayyar', 'Jadoun', 'Dewan', 'Bishnoi', 'Deshmukh', 'Chandwani', 'Joshi', 'Rana', 
        'Vyas', 'Chaurasia', 'Goud', 'Baishya', 'Baghel', 'Chhabra', 'Gahoi', 'Shivhare', 'Kandhadi', 'Kumar', 'Rathore', 'Bhardwaj', 'Kansal', 
        'Dhawan', 'Sahu', 'Paliwal', 'Prajapati', 'Khandelwal', 'Shukla', 'Rishidev', 'Bhil', 'Solanki', 'Chouhan', 'Chandrapal', 'Rathi']

    # madhyapradesh Female First name
    madhyapradesh_female_firstname = [
        'Shashi', 'Bhavana', 'Ankita', 'Riya', 'Shubhechha', 'Anjali', 'Kumari', 'Indira', 'Yashvi', 'Nutan', 'Gopika', 'Ravina', 'Kamini', 
        'Vimala', 'Namrata', 'Sejal', 'Aarti', 'Sadhana', 'Rupa', 'Nivriti', 'Poonam', 'Manika', 'Durvani', 'Apsara', 'Ravita', 'Aruna', 
        'Manorama', 'Veena', 'Sumi', 'Kalyani', 'Arpita', 'Chandrika', 'Snehal', 'Harsha', 'Amita', 'Usha', 'Prabhavati', 'Shreya', 'Rachna', 
        'Sakshi', 'Shalini', 'Sitalakshi', 'Vibhuti', 'Karuna', 'Padmini', 'Swarupa', 'Kavita', 'Yogita', 'Vidya', 'Ranjana', 'Meera', 'Diksha', 
        'Manisha', 'Renuka', 'Tanu', 'Lata', 'Sneha', 'Sudha', 'Durga', 'Sushma', 'Chhavi', 'Minal', 'Divya', 'Sonal', 'Saanvi', 'Narmada', 
        'Neelam', 'Suhani', 'Agnishikha', 'Laxmi', 'Shivani', 'Gulika', 'Megha', 'Swati', 'Vandita', 'Priti', 'Manjula', 'Ritika', 'Sujata', 
        'Urvashi', 'Rohini', 'Aishwarya', 'Tanvi', 'Bhakti', 'Rajashree', 'Chaitali', 'Saraswati', 'Jivika', 'Sumita', 'Vimalika', 'Kiran', 
        'Daya', 'Jahnavi', 'Rupika', 'Rajalakshmi', 'Ruchi', 'Vishali', 'Simran', 'Sharmila', 'Malini', 'Amrita', 'Shubhini', 'Vineeta', 
        'Mahika', 'Hemlata', 'Komal', 'Jaya', 'Pranjal', 'Nandini', 'Manju', 'Bhavita', 'Ashwati', 'Seema', 'Kamala', 'Deepika', 'Kanchana', 
        'Bhavani', 'Madhulika', 'Radhika', 'Yamuna', 'Nitika', 'Pallavi', 'Sharmistha', 'Rajni', 'Shital', 'Neha', 'Asha', 'Madhuri', 'Sampada', 
        'Rashmi', 'Yamini', 'Tarini', 'Sushila', 'Bhawna', 'Isha', 'Nisha', 'Ami', 'Kumud', 'Suman', 'Bhargavi', 'Pranjali', 'Kiranvati', 
        'Vishaka', 'Neelima', 'Urmi', 'Pramila', 'Rupali', 'Tulsi', 'Sumanthi', 'Kiranmayi', 'Anika', 'Esha', 'Aaradhya', 'Rajeshwari', 'Soni', 
        'Shubhra', 'Bina', 'Kanchan', 'Chandana', 'Lalita', 'Pratibha', 'Vandana', 'Mitali', 'Vaidehi', 'Shubha', 'Vidushi', 'Puja', 'Vasavi', 
        'Shraddha', 'Shruti', 'Leela', 'Urmila', 'Radhini', 'Surbhi', 'Yasoda', 'Charulata', 'Tanya', 'Nivya', 'Savitri', 'Sheetal', 'Gargi', 
        'Tanuja', 'Rekha', 'Rama', 'Madhavi', 'Rukmini', 'Nandita', 'Geetika', 'Hina', 'Vasundhara', 'Meenal', 'Indu', 'Pooja', 'Shubhi', 
        'Vinita', 'Bhavika']


    madhyapradesh_female_surname = [
        'Chand', 'Jalota', 'Sahu', 'Karodia', 'Gahoi', 'Baheti', 'Deora', 'Bhatnagar', 'Kandhadi', 'Tiwari', 'Tripathi', 'Bansal', 
        'Malik', 'Solanki', 'Paliwal', 'Dandotiya', 'Sharma', 'Khatri', 'Chaudhary', 'Shukla', 'Bharati', 'Joshi', 'Goyal', 'Chouhan', 
        'Vashist', 'Rathi', 'Gandhi', 'Dhawan', 'Agarwal', 'Chandwani', 'Rishidev', 'Dixit', 'Deshmukh', 'Khandelwal', 'Shah', 'Patil', 
        'Kothari', 'Bishnoi', 'Kashyap', 'Bhardwaj', 'Mungli', 'Pathak', 'Yadav', 'Lodh', 'Malviya', 'Desai', 'Gulia', 'Khare', 'Chaturvedi', 
        'Raghuwanshi', 'Pattnaik', 'Chaurasia', 'Chandorkar', 'Panchal', 'Verma', 'Goud', 'Kataria', 'Mehra', 'Dewan', 'Sodha', 'Rajput', 'Jain', 
        'Dewangan', 'Bhatti', 'Dhamani', 'Baghel', 'Kandari', 'Shivhare', 'Patel', 'Rathore', 'Jadhav', 'Laxman', 'Baishya', 'Lodha', 'Prasad', 
        'Kansal', 'Mann', 'Rana', 'Awasthi', 'Bhaskar', 'Agrawal', 'Bhil', 'Chandrapal', 'Pandey', 'Saxena', 'Bhargava', 'Kumar', 'Giri', 
        'Bohra', 'Hada', 'Meena', 'Nayyar', 'Bashar', 'Raghav', 'Prajapati', 'Jadoun', 'Garhwal', 'Daga', 'Chhabra', 'Kapadia', 'Gohil', 
        'Parihar', 'Kachhadiya', 'Nayak', 'Zadafia', 'Bairagi', 'Soni', 'Thakur', 'Vyas', 'Rawat', 'Seth', 'Mishra', 'Saraf', 'Gupta']

    madhyapradesh_female_suffix= ["Rani", "Devi", "Bai", " ", " ", " ", " ",  " ", " ", " ", " ",  " ", " ", " ", " "]

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(madhyapradesh_male_firstname)
        last_name_male = random.choice(madhyapradesh_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(madhyapradesh_female_firstname)
        suffix_female = random.choice(madhyapradesh_female_suffix)
        last_name_female = random.choice(madhyapradesh_female_surname)

        if preferences.get('name_type') == 'first':
            name_female = first_name_female + suffix_female  # First name with suffix
        else:
            name_female = first_name_female + suffix_female + " " + last_name_female  # Full name with suffix

        # Append names with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_madhyapradesh_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df
