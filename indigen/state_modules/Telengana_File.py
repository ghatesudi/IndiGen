import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_telengana_names(n, user_preference=None):

    # telengana Male First name
    telengana_male_firstname = [
        "Aadhithya", "Aadi", "Aaditya", "Aakash", "Aaryan", "Abhay", "Abhinav", "Abhishek", "Achyut", "Adarsh", "Aditya", 
        "Aja", "Ajeet", "Akash", "Akhilesh", "Akshay", "Aman", "Amarendra", "Amarnath", "Amrit", "Anand", "Anil", "Anjaneya", 
        "Anjaneyulu", "Anoop", "Appa", "Apparao", "Arav", "Arjun", "Arun", "Arvind", "Ashok", "Ashwin", "Babu", "Bairagi", 
        "Balaji", "Balakrihna", "Balakrishna", "Balaram", "Balu", "Balveer", "Banumathi", "Basava", "Baskar", "Bhagat", 
        "Bhanu", "Bhanuprasad", "Bharath", "Bhargav", "Bhaskar", "Bhaskara", "Bhavan", "Bhavani", "Bhavya", "Bhushan", 
        "Bhuvan", "Bhuvaneshwar", "Chaitanya", "Chakrapani", "Chakravarthy", "Chakri", "Chandra", "Chandramohan", 
        "Chandramouli", "Chandran", "Chandrasekar", "Chandrasekhar", "Chandrashekar", "Chandresh", "Charan", "Charvik", 
        "Chetan", "Chinna", "Chintan", "Chiranjeev", "Chiranjeevi", "Daksh", "Dasarathi", "Dattaprasad", "Dattatreya", 
        "Devaiah", "Devanand", "Devendra", "Dhanraj", "Dharmendra", "Dheeraj", "Dinesh", "Divya", "Durga", "Durvendra", 
        "Eshan", "Eshwar", "Gagan", "Gajendra", "Ganapathi", "Ganapati", "Ganesh", "Ganeshwar", "Gautam", "Gautham", 
        "Giri", "Girish", "Gokul", "Gokulraj", "Gopal", "Gopala", "Gopalakrishna", "Gopalan", "Goutam", "Goutham", "Govind", 
        "Harendra", "Hari", "Haribabu", "Haribhakta", "Hariharan", "Harinder", "Hariram", "Harirama", "Harish", "Harishchandra", 
        "Harsh", "Harsha", "Harshith", "Hemant", "Hemanth", "Indra", "Irfan", "Ishaan", "Jagadish", "Jagan", "Jagannatha", 
        "Jagdish", "Jai", "Janak", "Janardhan", "Jaya", "Jayant", "Jayaram", "Jayendra", "Jeevan", "Jeevendra", "Jitesh", 
        "Jnanendra", "Jyothi", "Kalyan", "Kalyana", "Kalyani", "Karthik", "Karthikeya", "Kiran", "Kishore", "Koteswara", 
        "Koushik", "Krish", "Krishan", "Krishna", "Krishnadev", "Krishnamurthy", "Krishnan", "Kumar", "Kumara", "Kunal", 
        "Lakhan", "Lakhendra", "Lakshman", "Lakshminarayana", "Lakshya", "Lavanya", "Laxman", "Laxminarayana", "Lingaiah", 
        "Lingaraj", "Lokesh", "Maanik", "Madhav", "Madhu", "Madhusri", "Madhusudan", "Madhusudhan", "Mahadevan", "Mahesh", 
        "Maheswar", "Mahi", "Mahindra", "Manav", "Manikanta", "Manmohan", "Manohar", "Manoj", "Mayur", "Mithun", "Mohan", 
        "Mukunda", "Murali", "Muralidhar", "Nabil", "Nagendra", "Nagesh", "Nageswar", "Nageswara", "Nanda", "Nandkishore", 
        "Narasimha", "Narasimharao", "Narayana", "Naresh", "Narsimhulu", "Naveen", "Neelesh", "Nihar", "Nikhil", "Niranjan", 
        "Nirmal", "Nitin", "Omkar", "Omprakash", "Padmaja", "Padmanabha", "Panneer", "Parameshwar", "Parthiban", "Pavan", 
        "Prabhakar", "Pradeep", "Prakash", "Pramod", "Pranav", "Pratap", "Puranjay", "Radhakrishna", "Raghav", "Raghava", 
        "Raghavendra", "Raghul", "Raghunandan", "Raghunath", "Raghuraman", "Rajamohan", "Rajaramesh", "Rajasekhar", 
        "Rajat", "Rajeev", "Rajendra", "Rajesh", "Rajeshwar", "Rajinder", "Rajinikanth", "Rajiv", "Rajkumar", "Rakeshwar", 
        "Ramakrishna", "Ramasundaram", "Ramaswamy", "Ramesh", "Rameshwar", "Rameswar", "Ranjan", "Ranjith", "Ravi", "Rekha", 
        "Renuka", "Rishi", "Rithik", "Rithvik", "Rohan", "Rudra", "Sadananda", "Sagar", "Sahil", "Sai", "Sai Aditya", 
        "Sai Ajay", "Sai Ankit", "Sai Ashwin", "Sai Charan", "Sai Hari", "Sai Jayant", "Sai Kiran", "Sai Krishna", 
        "Sai Kumar", "Sai Kumar Rao", "Sai Mahesh", "Sai Manish", "Sai Nikhil", "Sai Prakash", "Sai Pranav", "Sai Raghav", 
        "Sai Ram", "Sai Ramesh", "Sai Sandeep", "Sai Sankar", "Sai Shankar", "Sai Shubham", "Sai Sudarshan", "Sai Sudhir", 
        "Sai Teja", "Sai Venkatesh", "Sai Vimal", "Sai Vishnu", "Samarth", "Sambasiva", "Sampath", "Sandeep", "Sanjay", 
        "Sanjeev", "Sankara", "Santosh", "Sarveshwar", "Satish", "Satyamurthy", "Satyanarayana", "Shailendra", "Shakti", 
        "Shankar", "Shankarappa", "Shanmugam", "Sharad", "Sharvan", "Shashank", "Shiva", "Shivanand", "Shravan", "Shubham", 
        "Shyam", "Sidharth", "Siva", "Somnath", "Sreekanth", "Sreenivas", "Srinivas", "Srinivasa", "Srinivasan", "Srinivasulu", 
        "Sriram", "Subba", "Subbu", "Subhash", "Subodh", "Subrahmanyam", "Subramaniam", "Subramanyam", "Sudhakar", "Sumanth", 
        "Suraj", "Surendar", "Surendra", "Suresh", "Surya", "Suryanarayana", "Sushil", "Swaroop", "Tanay", "Tanjay", "Tanuj", 
        "Tapan", "Tarun", "Teja", "Tejas", "Tejeshwar", "Tharun", "Tharv", "Tharvik", "Thimmaiah", "Thirupathi", "Tilak", 
        "Tushar", "Uday", "Udayendra", "Umesh", "Vaidyanathan", "Vamshi", "Vamsi", "Varadarajan", "Varun", "Vasanth", 
        "Vasudev", "Veerendra", "Velmurugan", "Venkata", "Venkatachalam", "Venkatapathy", "Venkatesh", "Venkateshwar", 
        "Venkateshwarlu", "Venkateswar", "Venkatraman", "Venu", "Vicky", "Vignesh", "Vijay", "Vijayan", "Vikas", "Vikram", 
        "Vikraman"]
    # telengana Female First name
    telengana_female_firstname = [
        "Aadharani", "Aadhya", "Aaradhya", "Aarohi", "Aarti", "Aasha", "Aditi", "Aishwarya", "Akhila", "Akshita", "Alisha",
        "Amala", "Amita", "Amitha", "Amrita", "Amritha", "Ananya", "Anika", "Anitha", "Anjali", "Anjana", "Anshika",
        "Anvitha", "Aparna", "Aranya", "Archana", "Arpita", "Arpitha", "Ashwini", "Avani", "Avantika", "Barsha", "Bhagya",
        "Bhanu", "Bhanupriya", "Bharathi", "Bhavana", "Bhavani", "Bhavika", "Bhavitha", "Bhuvana", "Chaitanya", "Chaitra",
        "Chandana", "Chandini", "Chandra", "Chandrika", "Charitha", "Charulata", "Charulatha", "Chavi", "Chinmayi", "Chintu",
        "Chitralekha", "Daksha", "Damini", "Darshini", "Deepti", "Devika", "Dhanalakshmi", "Dhara", "Dhriti", "Divya",
        "Divyanka", "Divyaprabha", "Durga", "Ektha", "Eshwari", "Ganga", "Gargee", "Gayathri", "Gayatri", "Geetha",
        "Geetika", "Gokila", "Gomathi", "Hamsa", "Harini", "Haripriya", "Haritha", "Hema", "Hemalata", "Hemalatha",
        "Hemali", "Indira", "Indrani", "Indu", "Ishita", "Jagriti", "Janani", "Janhavi", "Jaya", "Jyothi", "Kalpana",
        "Kalyani", "Kamala", "Kamini", "Kanak", "Kanaka", "Kanmani", "Karishma", "Karthika", "Kashish", "Kavitha",
        "Kavya", "Kiran", "Kirti", "Komal", "Krishitha", "Krithika", "Kumudini", "Lajwanti", "Lakshmi", "Laksmi", "Lalitha",
        "Lata", "Latha", "Lathika", "Lavanya", "Laxmi", "Madhavi", "Madhu", "Madhuri", "Mahi", "Mahitha", "Manasa",
        "Manasi", "Manisha", "Manjari", "Manju", "Manvi", "Meena", "Meenal", "Meera", "Megha", "Meher", "Midhuna", "Minal",
        "Mithali", "Mithra", "Mohana", "Monika", "Monisha", "Mridula", "Muthu", "Nagma", "Naina", "Namita", "Namitha",
        "Namrata", "Nandini", "Nandita", "Nanditha", "Narmada", "Nayana", "Neela", "Neelam", "Neelima", "Neeraja", "Neha",
        "Niharika", "Nirmala", "Nithya", "Nitya", "Nivetha", "Padma", "Padmavathi", "Padmini", "Palli", "Parvati", "Pavani",
        "Pooja", "Poojitha", "Poonam", "Pranitha", "Prasanna", "Prashanti", "Prathima", "Praveena", "Pritika", "Priya",
        "Priyanka", "Raagini", "Radhana", "Radhika", "Rajani", "Rajitha", "Raksha", "Rameshwari", "Rani", "Ranjani", "Rekha",
        "Renuka", "Rishitha", "Rithika", "Rukmini", "Rupa", "Sabitha", "Sadhana", "Sadhavi", "Sadhvika", "Sakshi", "Saloni",
        "Sameera", "Samyuktha", "Sandhya", "Sangeeta", "Sangeetha", "Sanika", "Sanjana", "Sasi", "Satyavathi", "Savitha",
        "Seetha", "Shailaja", "Shakini", "Shakuntala", "Shalini", "Sharanya", "Sharda", "Sharika", "Sharmila", "Sharvani",
        "Shashi", "Sheela", "Shobha", "Shraddha", "Shreya", "Shruti", "Shubha", "Shubhalakshmi", "Shubhika", "Shweta",
        "Smita", "Sneha", "Snehal", "Snehalatha", "Sonal", "Sonali", "Subha", "Subhadra", "Subhani", "Subhiksha", "Sudha",
        "Suhani", "Sujatha", "Suma", "Suman", "Sumathi", "Sunita", "Sunitha", "Supriya", "Surabhi", "Sushma", "Sushmita",
        "Sushmitha", "Suvitha", "Swarna", "Swathi", "Tanvi", "Tarini", "Teena", "Tejal", "Tejashwini", "Tharini", "Tripura",
        "Trisha", "Tulasi", "Ujjwala", "Uma", "Urmila", "Usha", "Vaidehi", "Vaishali", "Vaishnavi", "Vandana", "Vani",
        "Vanitha", "Vardhini", "Varsha", "Varshini", "Vasudha", "Vasundhara", "Veda", "Veena", "Vibha", "Vidhitha", "Vidhya",
        "Vidushi", "Vidya", "Vijaya", "Vimala", "Vina", "Vini", "Vinitha", "Vishaka", "Vishakha", "Vishali", "Vratika",
        "Vrinda", "Vrushali", "Yamini", "Yashasvi", "Yashika", "Yashoda", "Sai Priya", "Sai Lakshmi", "Sai Shruti", "Sai Shree",
        "Sai Anjali", "Sai Bhavani", "Sai Meera", "Sai Varsha", "Sai Sandhya", "Sai Vani", "Sai Rupa", "Sai Kiran", "Sai Devi",
        "Sai Anusha", "Sai Sreeja", "Sai Nidhi", "Sai Manisha", "Sai Priyanka", "Sai Rekha", "Sai Smita", "Sai Radha", 
        "Sai Deepa", "Sai Charitha", "Sai Shalini", "Sai Divya", "Sai Swathi", "Sai Durga", "Sai Krupa", "Sai Vidya"]
    telengana_surname = [
        "Reddy", "Naidu", "Varma", "Yadav", "Rao", "Babu", "Choudhary", "Sharma", "Kumar", "Shetty", "Prasad", "Patel", 
        "Iyer", "Pandey", "Jadhav", "Pillai", "Sarma", "Nayak", "Swamy", "Srinivas", "Murthy", "Singh", "Janga", "Kothari", 
        "Venkatesh", "Kale", "Madhav", "Panchal", "Goud", "Kshatriya", "Gowda", "Chakravarthy", "Choudary", "Agarwal", 
        "Vemula", "Sandeep", "Raghavan", "Ravindran", "Vijayan", "Reddy Narayan", "Subrahmanyam", "Sastry", "Tiwari", 
        "Venkat", "Lakshman", "Chary", "Awasthi", "Kumaraswamy", "Dixit", "Srinivasan", "Jandhyala", "Apparao", 
        "Sundararajan", "Brahman", "Shastri", "Varah", "Bhaskar", "Sundaram", "Rathod", "Sathya", "Peddireddy", 
        "Koundinya", "Raghuveer", "Kodali", "Vasudeva", "Yellapragada", "Bhavani", "Aditya", "Rajagopal", "Paturi", 
        "Jasti", "Adivi", "Kandula", "Bhaskar Reddy", "Chintala", "Ramakrishna", "Kandukuri", "Gurrala", "Dammalapati", 
        "Ramaswamy", "Sudhakar", "Madhur", "Rajendra", "Adusumilli", "Peddamma", "Vasanta", "Sambasiva", "Shivaji", 
        "Sriram", "Kodandaram", "Uppalapati", "Shanbhag", "Chitturi", "Veeranna", "Kanthala", "Tummala", "Veeravalli", 
        "Shivaprasad", "Tirumala", "Madhu", "Lingam", "Mannem", "Venkata", "Hemanth", "Ganapathi", "Choudhary Reddy", 
        "Jonnalagadda", "Sreenivasa", "Jangra", "Bodla", "Gopichand", "Veeravarma", "Jagadish", "Kamarthy", "Varadarajan", 
        "Seshadri", "Dondapati", "Vemulapalli", "Taneja", "Patwari", "Nandi", "Bokkalagutta", "Rangareddy", 
        "Ramakrishna Reddy", "Surya Narayana", "Murthy Reddy", "Madhusudhan", "Pandurangi", "Nallapareddy", 
        "Yerramsetti", "Vangalapudi", "Sarveshwar", "Venkataramana", "Sitaram", "Golla", "Acharya", "Shivalingam", 
        "Sundar", "Sahithi", "Palle", "Jaya Lakshmi", "Srihari", "Narsing Rao", "Subbiah", "Macherla", "Vanga", 
        "Tummalapalli", "Zachariah", "Subbareddy"]
    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(telengana_male_firstname)
        last_name_male = random.choice(telengana_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(telengana_female_firstname)
        last_name_female = random.choice(telengana_surname)

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
    file_path = 'generated_telengana_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df
