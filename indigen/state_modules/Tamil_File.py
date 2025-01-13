import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_tamil_names(n, user_preference=None):

    # tamil Male First name
    tamil_male_firstname = [
        'Eshwaran', 'Muthuraj', 'Valluvan', 'Yamuneshwar', 'Periyasamy', 'Azhagan', 'Baskaran', 'Vishwarup',
        'Sankar', 'Hariharan', 'Devan', 'Raghu', 'Vijayendra', 'Sakthivel', 'Venkatraman',
        'Ravichandran', 'Maniraj', 'Thayalan', 'Sarvothaman', 'Bhaskar', 'Ravi', 'Kumar', 'Siddharthan',
        'Bharanidharan', 'Lakshmi Narayanan', 'Sankaralingam', 'Rajagopal', 'Manikandan', 'Murugesan', 'Ganesh',
        'Yuvanesh', 'Suresh', 'Kamalakannan', 'Yuvan', 'Thirupathi', 'Manohar', 'Siddharth', 'Dilip',
        'Vivek', 'Adithyakumar', 'Chandran', 'Manikaran', 'Muthu', 'Niranjan', 'Murugan', 'Prabhakaran', 'Arun',
        'Ravindran', 'Vijayakumar', 'Rathin', 'Arunkumar', 'Arulmozhi', 'Ganeshan', 'Vasanth', 'Sathish', 'Sujay',
        'Vishal', 'Rajalingam', 'Yogeshwaran', 'Madhavan', 'Thirumalai', 'Sarvesh', 'Vasudev', 'Kadhir', 'Vignesh',
        'Vishwanath', 'Balakrishnan', 'Chidambaram', 'Velmurugan', 'Natarajan', 'Ishwar', 'Yashvanth', 'Dinesh', 'Govind',
        'Keshavan', 'Aran', 'Nagendra', 'Vimal', 'Suriyan', 'Kothandaraman', 'Lakshmanan', 'Arunachalam', 'Raghuraman',
        'Velan', 'Thangaraj', 'Seetharaman', 'Vetrivel', 'Perumal', 'Sankaran', 'Karthikeyan', 'Thavakumar', 'Vasanthan',
        'Kannan', 'Vishwaraj', 'Sethu', 'Dineshwaran', 'Govindan', 'Ashwin', 'Vasanthakumar', 'Tharun', 'Ayyappan',
        'Venkatesan', 'Sivadas', 'Muthiah', 'Madhusudhanan', 'Sundaramurthy', 'Vittal', 'Gopal', 'Thavapalan', 'Raghavan',
        'Veeramani', 'Dharmarajan', 'Nandhan', 'Bharani', 'Vasikaran', 'Chandrakant', 'Vijayan', 'Sundararajan', 'Nataraj',
        'Sivaraman', 'Jagannathan', 'Kovalan', 'Rajesh', 'Muthuvel', 'Dharma', 'Aadithya', 'Subramanian', 'Vinay',
        'Thiruvengadam', 'Kanchana', 'Naga', 'Santhosh', 'Srinivasan', 'Yogesh', 'Saravanan', 'Sajith', 'Vishnu', 'Vinayak',
        'Vasudevan', 'Anandan', 'Karthick', 'Rathinavel', 'Sampath', 'Aravindan', 'Krishnan', 'Balasubramanyam', 'Ilango',
        'Thavendran', 'Ramesh', 'Venu', 'Naveen', 'Ayyadurai', 'Sundaram', 'Sundar', 'Vajendra', 'Arul', 'Vishwanathan',
        'Aadhavan', 'Kumaraswamy', 'Ananthan', 'Jayachandran', 'Balasubramanian', 'Aarav', 'Karthik','Ganapathi',
        'Ganapathiraj', 'Sivakumar', 'Suryakumar', 'Ilanthirayan', 'Abinesh', 'Lakshman', 'Sriram', 'Varadarajan',
        'Vigneshwar', 'Muthusamy', 'Balaraman', 'Nadhiyal', 'Nithyanand', 'Vikram', 'Vikraman', 'Kandhan', 'Ramakrishnan',
        'Ganapathy', 'Raghul', 'Kavi', 'Dhandapani', 'Vinod', 'Vidhyaraj', 'Hari', 'Kali', 'Rajendran', 'Vithyapriya', 'Rajakumar', 
        'Tharv', 'Shankar','Muthuraman', 'Thirumal', 'Srirangan', 'Gajenran', 'Senthilkumar', 'Achuthan', 'Ravinder', 'Venkataraman',
        'Senthil', 'Ravi Shankar', 'Sivapalan', 'Ramasamy', 'Sundarajan']

    tamil_male_surname = [
        'Anand', 'Arumugam', 'Baskar', 'Chandran', 'Chidambaram', 'Devarajan', 'Duraisamy', 'Ganapathy', 'Gopalakrishnan', 'Iyer',
        'Jayaraman', 'Karthikeyan', 'Kumarasamy', 'Lakshman', 'Madhavan', 'Manoharan', 'Muthiah', 'Nagarajan', 'Natarajan',
        'Raghavan', 'Ramesh', 'Rajagopal', 'Rajendran', 'Ravi', 'Ravindran', 'Ramanan', 'Ravichandran', 'Sankar', 'Sivakumar',
        'Subramanian', 'Sundararajan', 'Thavapalan', 'Thirumalai', 'Vaidyanathan', 'Vasudevan', 'Venkatesan', 'Vijayakumar',
        'Vishwanathan', 'Vignesh', 'Yoganathan', 'Annamalai', 'Bhaskar', 'Chellappan', 'Dinesh', 'Elangovan', 'Ganesh', 'Hariharan',
        'Jagannathan', 'Karthik', 'Kovalan', 'Lakshmanan', 'Mahalingam', 'Manickam', 'Muthuraman', 'Nagappan', 'Nandhini', 'Nithyanand',
        'Prabhu', 'Raghul', 'Ramanathan', 'Ravishankar', 'Senthil', 'Shanmugam', 'Sivasamy', 'Sundaram', 'Suryanarayan', 'Tharun',
        'Vasanthan', 'Venkataraman', 'Yugantar', 'Achuthan', 'Chandrasekar', 'Durai', 'Ganapathiraj', 'Gopalan', 'Kamaraj', 'Kavi',
        'Manickan', 'Mahadevan', 'Nadar', 'Palanisamy', 'Parthiban', 'Ravi Kumar', 'Saravanan', 'Sundara', 'Srinivasan', 'Siddharth',
        'Thayalan', 'Vasishth', 'Vijayan', 'Vigneshwaran', 'Vikraman', 'Vishnu', 'Yathish', 'Arunachalam', 'Baskaran', 'Dhinesh',
        'Gowtham', 'Harish', 'Jeevan', 'Krishnan', 'Lakshmi Narayanan', 'Madhusudhan', 'Muthuraj', 'Nadhiyal', 'Prakash', 'Ravindra',
        'Sakthivel', 'Sivapalan', 'Shivakumar', 'Sundar', 'Srinivas', 'Vijayakant', 'Vasanthi', 'Vinayak', 'Vittal', 'Yoganesh',
        'Anandaraj', 'Chandru', 'Devaraj', 'Ezhil', 'Ganeshwaran', 'Kannan', 'Karthikeya', 'Mahendran', 'Murugan', 'Nagaraj', 'Rajalingam',
        'Ravi Shankar', 'Rajashekar', 'Sambath', 'Shanmugapriya', 'Shivendra', 'Sundaran', 'Tharv', 'Vasudev', 'Yogeshwaran',
        'Arulmozhivarman', 'Balaji', 'Bhavani', 'Chandrakumar', 'Devan', 'Hariprasad', 'Kartik', 'Kuppusamy', 'Manohar', 'Muthupandi',
        'Siddhi', 'Vasundhara', 'Yashwanth', 'Aiyer', 'Ayappan', 'Brahman', 'Dharmarajan', 'Kanchan', 'Kari', 'Nandhan', 'Periyasamy',
        'Ramasamy', 'Sankaran', 'Vettar', 'Yogesh', 'Ilanthirayan', 'Kali', 'Nagendra', 'Nirmal', 'Perumal', 'Raghuraman', 'Sankari',
        'Sundaraman', 'Suresh', 'Vikram', 'Vinod', 'Azhagiri', 'Kumar', 'Manikandan', 'Raghuraj', 'Sudarshan', 'Subramanyam', 'Vishal',
        'Brahmanathan', 'Kaliappan', 'Lakshmikanth', 'Nandhakumar', 'Periyanayaki', 'Raghunathan', 'Sarvesh', 'Vasanthakumar',
        'Vishwanath', 'Yogendra', 'Balasubramanian', 'Elangapathy', 'Ganapathi', 'Kandasamy', 'Kaviyanan', 'Nataraj', 'Rajapandiyan',
        'Raghupathi', 'Sundaralingam', 'Sundaramurthy', 'Vairam', 'Vishwakarma', 'Azhagar', 'Devakumar', 'Haridran', 'Raghavendra', 'Sundararaj', 'Vinoth',
        'Vithalaraman', 'Achuthapandiyan', 'Chandrashekhar']
    # tamil Female First name
    tamil_female_firstname = [
        'Aparna', 'Surya', 'Sathvika', 'Kasturi', 'Kalpana', 'Latha', 'Sanjana', 'Bala', 'Radhika', 'Shobana', 'Sundararani', 'Ira', 
        'Arpita', 'Ezhil', 'Jothika', 'Bhuvana', 'Vasundra', 'Sadhana', 'Kalyani', 'Hema', 'Yasoda', 'Yashini', 'Kousalya', 'Chitra', 
        'Saranjali', 'Chandramukhi', 'Neelam', 'Madhuri', 'Eswari', 'Malar', 'Bhanu', 'Madhuravani', 'Tamilarasi', 'Diya', 'Anjali', 
        'Saranya', 'Subha', 'Chithra', 'Rani', 'Parvathi', 'Sangeetha', 'Madhubala', 'Aiswarya', 'Sumangali', 'Yashoda', 'Janani', 
        'Harini', 'Yamini', 'Nagalakshmi', 'Karpagam', 'Poomalai', 'Akhila', 'Indira', 'Suhasini', 'Rajani', 'Bhuvaneshwari', 'Kanchana', 
        'Bhavani', 'Manimegalai', 'Akshara', 'Bhavadharini', 'Kaveri', 'Jeevitha', 'Kavitha', 'Nithya', 'Abinaya', 'Poornima', 'Padmavathi', 
        'Ezhini', 'Anushka', 'Rashmi', 'Selvi', 'Amrutha', 'Geetha', 'Chandrakala', 'Kamala', 'Padma', 'Vijaya', 'Uma', 'Vidhya', 'Ravindran', 
        'Deepika', 'Manasa', 'Rajeshwari', 'Meena', 'Usha', 'Iravathi', 'Sudha', 'Tharini', 'Sushma', 'Vanisha', 'Vasanti', 'Saraswati', 
        'Narmada', 'Ganga', 'Vasanthi', 'Kumari', 'Suma', 'Tamarai', 'Chandrika', 'Hamsa', 'Manju', 'Ramya', 'Revathi', 'Yalini', 'Sakthi', 
        'Azhagi', 'Nila', 'Ranjani', 'Kowsalya', 'Dhanya', 'Divya', 'Rajalakshmi', 'Thavapalan', 'Vimala', 'Lakshmi', 'Kamadhenu', 'Anju', 
        'Thayarani', 'Valliammai', 'Sithara', 'Elamathi', 'Chithirai', 'Muthumani', 'Muthulakshmi', 'Vani', 'Sujatha', 'Bhuvi', 'Natarani', 
        'Lakshmi Priya', 'Sumathi', 'Vasundhra', 'Keerthana', 'Lakshana', 'Thiripura', 'Kanimozhi', 'Haripriya', 'Shree', 'Dayanidhi', 
        'Sumitha', 'Kamalamani', 'Meenakshi', 'Kajal', 'Rukmini', 'Shashvathi', 'Ramaa', 'Aadhini', 'Balamani', 'Nandini', 'Srinidhi', 'Durga', 
        'Chitradevi', 'Sharmila', 'Aadhira', 'Ananyaa', 'Sakina', 'Lakshmipriya', 'Kavya', 'Dharini', 'Sathya', 'Kaviya', 'Sindhu', 'Nandhini', 
        'Vandana', 'Vasuki', 'Adivi', 'Sandhya', 'Malini', 'Priya', 'Yasmin', 'Jagathiya', 'Jayanthi', 'Ravi', 'Ananya', 'Kundhavi', 'Thulasi', 
        'Dhivya', 'Ila', 'Madhavi', 'Madhurima', 'Vennila', 'Sahithya', 'Sundari', 'Pavithra', 'Tharani', 'Ankitha', 'Eshwarya', 'Akila', 
        'Vasundhara', 'Vishali', 'Aadhya', 'Gayathri', 'Varsha', 'Divyadharshini', 'Devika', 'Shanvika', 'Vidya', 'Mithra', 'Ravathi', 
        'Sabarinath', 'Pavina', 'Valli', 'Subadra', 'Indra', 'Maya', 'Sasi', 'Malathi', 'Sivarani', 'Santoshi', 'Aaradhya', 'Swathi', 
        'Shalini', 'Vanathi', 'Shivani', 'Geethika', 'Shanthi', 'Pavani', 'Thavani', 'Vijayalakshmi', 'Rajalakshmii', 'Meenal', 'Uthara', 
        'Lalitha', 'Sudhamani', 'Vishnupriya', 'Ishita', 'Nandita', 'Veda', 'Indrakshi', 'Chandini', 'Gokila', 'Bhuvneshwari', 'Shobha', 
        'Vishalini', 'Ishwari', 'Balaji', 'Anjalin']
    tamil_female_surname = [
        'Vairam', 'Vannammal', 'Madhavi', 'Rukmini', 'Vimaladevi', 'Shanthi', 'Valarmathi', 'Geethashree', 'Kavandhi', 'Vasanthavalli', 
        'Arpudhamani', 'Vijayalaksmi', 'Jothimathi', 'Pavithram', 'Thirupavani', 'Eshwari', 'Sarojini', 'Valliyamma', 'Devapriya', 'Kalyanika', 
        'Vanniyar', 'Rajavalli', 'Udayakumari', 'Vellammal', 'Sukanya', 'Pavalar', 'Arunthathi', 'Ramavathi', 'Karpagam', 'Nallammal', 
        'Lalithambal', 'Vikramavathi', 'Madhuram', 'Poomalar', 'Chidambaramani', 'Malarvizhi', 'Vasundaradevi', 'Bhuvaneshwari', 'Vaidehi', 
        'Periyamma', 'Annamma', 'Suvira', 'Sundaravalli', 'Sudarani', 'Vithalapriya', 'Pudhumai', 'Sivaprakasam', 'Sivagami', 'Periyar', 
        'Ranganayaki', 'Manju', 'Vasanthika', 'Vilasini', 'Eswari', 'Bhanumathi', 'Subhadra', 'Vadhini', 'Ramasundari', 'Sundararani', 
        'Indumathi', 'Sitharaman', 'Subramaniam', 'Viruthambal', 'Nirmala', 'Sathyavathi', 'Kamaraj', 'Meenakshi', 'Meenambal', 'Ravindran', 
        'Ravichandran', 'Bhavani', 'Alagammal', 'Vallambal', 'Rajalakshmi', 'Savitri', 'Vedavati', 'Kavitha', 'Vengai', 'Nagarathnam', 
        'Muthulakshmi', 'Sivamani', 'Kanakammal', 'Kaviya', 'Azhagan', 'Avvaiyar', 'Vanniar', 'Sabarivalli', 'Saraswatidevi', 'Ravinthra', 
        'Rajeswari', 'Bhuvankanni', 'Shanthakumari', 'Viththiya', 'Selvamani', 'Ranjanai', 'Devarajani', 'Azhagarai', 'Chellamma', 
        'Karpagamani', 'Manimekalai', 'Vishalakshi', 'Thulasi', 'Thavapalan', 'Kanchanadevi', 'Venkateshwari', 'Jeyalakshmi', 'Sakuntala', 
        'Poomalai', 'Selvarani', 'Rajamani', 'Umaiyal', 'Shanvi', 'Azhagammal', 'Varadarajan', 'Subramanyam', 'Sundari', 'Chandramukhi', 
        'Vandana', 'Kudimagan', 'Vijayanthi', 'Aadhilakshmi', 'Ravivarma', 'Dhanalakshmi', 'Rasathi', 'Sivarasani', 'Sundarapandi', 'Krithika', 
        'Dayanidhi', 'Thyagaraja', 'Rajamanikam', 'Sivanthi', 'Subadra', 'Thayalan', 'Balarani', 'Selvathal', 'Chandramathi', 'Usharani', 
        'Venkatalakshmi', 'Vasanta', 'Kalyanavalli', 'Lakshmikutty', 'Vijayalakshmi', 'Vasundharammal', 'Vidyanjali', 'Rathinapriya', 
        'Vishvakannan', 'Vadamalar', 'Vishnukundala', 'Chidambaram', 'Adivarai', 'Sivaraman', 'Thirumalar', 'Chandhini', 'Srinivasa', 
        'Yamunavalli', 'Srinivasan', 'Geethalakshmi', 'Kavivallal', 'Sivakami', 'Prithivimala', 'Lakshmi', 'Chellarani', 'Vasumathi', 
        'Sithamathi', 'Shyama', 'Yamunammal', 'Rangammal', 'Azhagi', 'Radhika', 'Yasodha', 'Kavitharaj', 'Arangammal', 'Malarvani']

        # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(tamil_male_firstname)
        last_name_male = random.choice(tamil_male_surname)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        first_name_female = random.choice(tamil_female_firstname)
        last_name_female = random.choice(tamil_female_surname)

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
    file_path = 'generated_tamil_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df