import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_kerala_names(n, user_preference=None):
    # Kerala Male First Names
    malyali_male_firstname_hindu = [
        "Achuthan", "Aditya", 'Anup', 'Ajaneesh', 'Nijil', "Ajeesh", "Ajith", "Aravind", "Arjun", "Balakrishnan", "Binu", "Chandran", "Gokul",
        "Hari", "Hariharan", "Jagadeesh", "Jayan", "Jayesh", "Kailas", "Kannan", "Krishna", "Krishnan", "Kumar",
        "Lalith", "Manoj", "Madhavan", "Mahesh", "Mithun", "Nandakumar", "Narayana", "Nithin", "Nithya", "Pradeep",
        "Prakash", "Pranav", "Raghavan", "Rajesh", "Rajendra", "Ramesh", "Ravindran", "Rohit", "Rohin", "Sajan",
        "Sathish", "Sreenivasan", "Shankar", "Shyam", "Srinivasan", "Suresh", "Sushant", "Sivadas", "Suraj", "Sundar",
        "Shiva", "Shivendra", "Vasudevan", "Vijayan", "Vimal", "Vinod", "Vishnu", "Vishwanathan", "Vivek", "Yogesh",
        "Bharath", "Biju", "Chandresh", "Deepak", "Ganesh", "Girish", "Govind", "Harish", "Jayakrishnan", "Jinesh",
        "Kiran", "Kripal", "Lakshman", "Lijo", "Manish", "Midhun", "Nadeem", "Nashit", "Nilesh", "Nishad", "Nithesh",
        "Pranith", "Prem", "Rajiv", "Ramesh", "Ravi", "Renjith", "Rithvik", "Sandeep", "Sanjay", "Shanil", "Shivendra",
        "Sudhakar", "Sushil", "Tejas", "Vineet", "Vinit", "Vishal", "Akhil", "Ashwin", "Anoop", "Dinesh", "Hemanth", "Jagannath", "Jithin",
        "Karthik", "Kishore", "Mithilesh", "Sandeep", "Srinath", "Vijay", "Vivek", "Vikram", "Vishnupriya", "Vivekanand", "Sandeepan", "Sanjay",
        "Chandrashekharan", "Rajagopalan", "Rajashekharan", "Somashekharan", "Jambunadham", "Thungayya", "Siddharamaiah",
        "Venkataiah", "Vijayarajan", "Vellupillai","Padmavilasam", "Somasundaram", "Somarajan", "Gunashegaran", "Jayaraman"
    "Jayarajan", "Kumaradasa", "Kumareseņa", "Kuppuswamy", "Kuppukrisņan","Kanagasahaya", "Karumuth", "Kurumurthy", "Kunhirajan",
        "Kunhiraman","Kunhikrisnan", "Kannaswamy", "Kannukrisnan", "Gopikrisņa", "Gopiraghavan","Gopinathan", "Gopikumaran",
        "Gopimohana", "Kuttappan", "Ananthanarayaņa","Ananthamurthy", "Ananthakrisna", "Annadurai", "Annamalai", "Bopanna", 
    "Kuttiappa", "Kutțiamma", "Kuttikrishnan", "Kamatchi", "Balachandran","Balakrisnan", "Balasubramanyan", "Balamurugan", "Balaganapathy", 
    "Balasimham", "Balamohana", "Krishnamurthy", "Krishnamachari","Kunjunnirajan", "Munikundan", "Muniappan", "Manivannana", 
    "Manishankara", "Maniratnam", "Maniratnamma", "Manishankar", "Muthunayagam","Muthuswamy", "Muthukrisnan", "Muthukumaran", "Muthaiah",
        "Meekshisundaram","Meekshinathan", "Nagamani", "Nagaratnam", "Nagarajan", "Nagaratnamma","Nagaamma", "Nagalingam", "Nagabhusana",
        "Nagavardhana", "Nagaishwara", "Nagesha", "Nagindra", "Nagishvari", "Nendunchezhiyan", "Neduchezhiyan",
        "Adinarayaņan", "Arumuga", "Alladikrisņaswami", "Appu Kuttan", "Anbazhagan","Manjunatha", "Nanjandishwara","Venkata", "Ramakrisna", "Ananthakrisņa", "Ananthanarayana", 

    "Ananthapadmanabha", "Shivarama", "Shivashankara", "Shankaramahadeva", "Shankaranarayaņa", "Venkatarama", "Venkatanarayaņa", "Manikyam",
    "Maniratnam", "Nagamani", "Nagaratnam", "Shivaramakrisnan", "Rudrambika","Laxminarayaņa", "Janakirama", "Umamasheshwara", "Radhakrisņa", "Seetharama",
    "Vasava", "Ramanuja", "Agasthya", "Madhava", "Mallikarjuna", "Tyagaraja", "Ravi", "Surya", "Bhaskara", "Dinkara", "Chandra", "Soma", "Sudhakara",  "Chandrabhanu"]

    malyali_male_surname_hindu =  [
        'Raghavan', 'Kumar', 'Jayan', 'Nellikkal', 'Suresh', 'Venu', 'Kurup', 'Krishnan', 'Vaidyar', 'Gopal', 
        'Madhusoodhanan', 'Ramachandran', 'Rathnakaran', 'Thampi', 'Sarojini', 'Rajesh', 'Kochuparambil', 'Padmini', 
        'Shaan', 'Govindan', 'Sreenivasan', 'Nambiar', 'Kailas', 'Nadapran', 'Madhavan', 'Sankar', 'Prathapan', 
        'Ravindran', 'Kollath', 'Kannan', 'Chakyar', 'Pradeep', 'Anoop', 'Nirmal', 'Shaji', 'Sundaram', 'Venkiteswaran', 'Krishna', 'Sridhar', 
        'Prakash', 'Chidambaram', 'Vikram', 'Narayana', 'Gokul', 'Sivadas', 'Ganesh', 'Rajeev', 'Sreejith', 'Rajagopal', 'Nambudiripad', 
        'Warrier', 'Nair', 'Ravi', 'Sandeep', 'Murali', 'Ajayan', 'Sunil', 'Meenakshi', 'Sankaran', 'Hemanth', 'Sathish', 'Haridas', 'Shanil', 
        'Pillai', 'Harish', 'Chandran', 'Vijayan', 'Prasanna', 'Gopinathan', 'Ramesh', 'Ramani', 'Soman', 'Hariharan', 'Lakshmanan', 'Menon', 
        'Vayalil', 'Rajendran', 'Rathnakumar', 'Balan', 'Gopalakrishnan', 'Raghu', 'Balakrishnan', 'Aravind', 'Harikrishnan', 'Sundar', 
        'Srinivasan', 'Bharath', 'Raj', 'Kurian', 'Vishwanathan', 'Deepak', 'Eapen', 'Ramanan', 'Vasudevan']


    # Kerala Female First Names
    malyali_female_firstname_hindu =  [
        'Vidya', 'Kanaka', 'Yashoda', 'Charutha', 'Shruthi', 'Damini', 'Neeraja', 'Sumathi', 'Shubha', 'Pooja', 'Jyothi', 'Sadhvi', 'Avani',
        'Tejaswini', 'Ujjwala', 'Renuka', 'Aruna', 'Darika', 'Bhavini', 'Varsha', 'Gajani', 'Meena', 'Sajini', 'Tharini',
        'Vinaya', 'Dhanya', 'Navya', 'Bhavani', 'Thara', 'Jeevitha', 'Meenal', 'Preethi', 'Rama', 'Mohana', 'Ammu', 'Jagruti', 'Bhavana',
        'Lakshmi', 'Bhavya', 'Mithra', 'Amritha', 'Ishwari', 'Karthika', 'Arya', 'Gita', 'Chandralekha', 'Daksha', 'Manjula', 'Lakshmipriya',
        'Haritha', 'Alaka', 'Sadhana', 'Sarika', 'Nandhini', 'Sharmila', 'Devi', 'Sangeetha', 'Sharanya', 'Malathi', 'Rohini', 'Manjari',
        'Poornima', 'Pavani', 'Gokila', 'Maya', 'Suman', 'Nithila', 'Vennila', 'Gajini', 'Vidhitha', 'Prasanna', 'Anupama', 'Meera', 'Radha',
        'Aishwarya', 'Chithra', 'Kushala', 'Sangeeta', 'Charushila', 'Madhavi', 'Sushila', 'Krishna', 'Shanthi', 'Eshitha', 'Manasi', 'Sushmita',
        'Hamsini', 'Sujatha', 'Durga', 'Aiswarya', 'Chandrika', 'Anjana', 'Gajalakshmi', 'Gauri', 'Sindu', 'Anisha', 'Ragini',
        'Arundhathi', 'Lalitha', 'Sruthi', 'Sushma', 'Disha', 'Kalyanika', 'Bhavitha', 'Vishwajeet', 'Yogitha', 'Rajeswari',
        'Malini', 'Divya', 'Swathi', 'Gayathri', 'Amrutha', 'Usha', 'Charulatha', 'Seetha', 'Eshwari', 'Ishita', 'Vamika', 'Dharini',
        'Chaitanya', 'Hitha', 'Madhumathi', 'Sneha', 'Chinmayi', 'Shreya', 'Chitrani', 'Shradha', 'Lakshitha', 'Sharika', 'Pavithra',
        'Kumari', 'Radhika', 'Indu', 'Vimala', 'Harini', 'Divyapriya', 'Suhasini', 'Bhuvitha', 'Sakhi', 'Swarna', 'Ritha', 'Sowmya',
        'Gouri', 'Uma', 'Keerthana', 'Nalini', 'Madhurima', 'Kairavi', 'Sindhu', 'Sundari', 'Vaidehi', 'Akshaya', 'Aakriti', 'Anu',
        'Padmalochana', 'Savitha', 'Chandini', 'Gopika', 'Veda', 'Niveditha', 'Vidhya', 'Sreeja', 'Rajitha', 'Sahana', 'Pavitra',
        'Chitra', 'Dharitha', 'Chandana', 'Devika', 'Kavya', 'Narayani', 'Rukmini', 'Manorama', 'Sadhvika', 'Geetha', 'Vishaka',
        'Rekha', 'Madhuri', 'Madhumitha', 'Yogini', 'Raveena', 'Ananya', 'Pranitha', 'Sita', 'Esita', 'Lakshmi Priya', 'Abhaya',
        'Krishna Priya', 'Vasundhara', 'Prema', 'Sreelakshmi', 'Padmavati', 'Ravina', 'Nirmala', 'Swetha', 'Bhanumathi', 'Neela',
        'Vishalini', 'Vidhyashree', 'Manasa', 'Manju', 'Jaya', 'Bhuvana', 'Leena', 'Aalini', 'Vasavi', 'Aswathi', 'Sreevani',
        'Shanvika', 'Shanthini', 'Leela', 'Yamuna', 'Tulasi', 'Rajalakshmi', 'Sakshi', 'Siri', 'Janaki', 'Nandini', 'Anitha',
        'Anjali', 'Aadya', 'Padmavathi', 'Sanya', 'Malavika', 'Aadhya', 'Kiran', 'Keerti', 'Arpita', 'Rani', 'Nithya', 'Hamsa',
        'Ravika', 'Kalyani', 'Kavitha', 'Achyuta', 'Suma', 'Shashi', 'Kripa', 'Hema', 'Aanjali', 'Shakthi', 'Nisha', 'Rithika',
        'Indira', 'Pranathi', 'Vinitha', 'Shalini', 'Kiranmayi', 'Arathi', 'Parvathi', 'Karunya', 'Dhanalakshmi', 'Vishnupriya',
        'Deepti', 'Shilpa', 'Kalpana', 'Shrini', 'Riya', 'Vijaya', 'Sreelekshmi', 'Anagha', 'Nayana', 'Swara', 'Saranya', 'Bhadra']



    malyali_female_surname_hindu =  [
            'Madhavan', 'Vishwanathan', 'Hemanth', 'Balan', 'Rathnakumar', 'Raghu', 'Kailas', 'Kumar', 'Nambiar', 'Sankar', 'Eapen', 
            'Kollath', 'Kochuparambil', 'Harikrishnan', 'Jayan', 'Gopinathan', 'Shaji', 'Nambudiripad', 'Narayana', 'Venkiteswaran', 
            'Chakyar', 'Balakrishnan', 'Chandran', 'Soman', 'Sreenivasan', 'Sivadas', 'Pradeep', 'Nadapran', 'Padmini', 'Raghavan', 
            'Ramachandran', 'Raj', 'Govindan', 'Suresh', 'Sreejith', 'Ramani', 'Vikram', 'Vaidyar', 'Nair', 'Srinivasan', 'Sathish', 
            'Rajendran', 'Gokul', 'Kurup', 'Murali', 'Madhusoodhanan', 'Prasanna', 'Bharath', 'Chidambaram', 'Ramesh', 'Krishnan', 
            'Ajayan', 'Nellikkal', 'Ravindran', 'Sandeep', 'Gopalakrishnan', 'Rajeev', 'Hariharan', 'Sundaram', 'Haridas', 'Vasudevan', 
            'Meenakshi', 'Warrier', 'Pillai', 'Rajagopal', 'Ramanan', 'Lakshmanan', 'Vijayan', 'Rajesh', 'Harish', 'Sarojini', 'Kurian', 
            'Aravind', 'Rathnakaran', 'Anoop', 'Deepak', 'Gopal', 'Kannan', 'Ganesh', 'Shaan', 'Krishna', 'Sundar', 'Prakash', 'Vayalil', 
            'Nirmal', 'Sridhar', 'Sunil', 'Menon', 'Shanil', 'Ravi', 'Venu', 'Prathapan', 'Sankaran', 'Thampi']

    #Muslim names
    malyali_male_firstname_muslim= [
            'Abdul Rahman', 'Aarif', 'Khaled', 'Sami', 'Manzoor', 'Amin', 'Naseem', 'Hassan', 'Ayaan', 'Muneeb', 'Tariq', 'Fahad', 'Moazzam', 
            'Fayaz', 'Zayd', 'Basharat', 'Hisham', 'Osman', 'Shafiq', 'Arif', 'Mazhar', 'Mansoor', 'Ashraf', 'Irfan', 'Basheer', 'Burhan', 
            'Haytham', 'Rehan', 'Iqbal', 'Mujtaba', 'Nawaz', 'Nadir', 'Nadeem', 'Ehsan', 'Bashir', 'Saqib', 'Akram', 'Feroz', 'Adnan', 'Madhin', 
            'Ahsan', 'Zahid', 'Rashid', 'Azaan', 'Zaki', 'Umar', 'Ameen', 'Asif', 'Jameel', 'Afnan', 'Faisal', 'Majeed', 'Feroze', 'Anas', 
            'Marwan', 'Abdullah', 'Dawood', 'Imran', 'Shazib', 'Danish', 'Arshad', 'Yousuf', 'Ali', 'Afzal', 'Salim', 'Sahil', 'Sulaiman', 
            'Muhammad', 'Ibraheem', 'Furqan', 'Raza', 'Omer', 'Imad', 'Khalil', 'Zubair', 'Rizwan', 'Azim', 'Faraz', 'Wahid', 'Nabeel', 
            'Jibril', 'Nasir', 'Adil', 'Badar', 'Rafi', 'Shibli', 'Iftikhar', 'Latif', 'Saad', 'Malik', 'Yasir', 'Junaid', 'Farhan', 
            'Arsalan', 'Omar', 'Shahid', 'Farooq', 'Ayyub', 'Riyad', 'Azad', 'Shazad', 'Hasan', 'Mahmood', 'Salman', 'Zaid', 'Hussein', 
            'Qasim', 'Masood', 'Qamar', 'Ameer', 'Rayyan', 'Shakir', 'Sardar', 'Nazeer', 'Zuhair', 'Ghafoor', 'Taha', 'Akbar', 'Sharif', 
            'Wasiq', 'Mahmud', 'Mustafa', 'Faizan', 'Azhar', 'Yaseen', 'Zayyan', 'Aslam', 'Khalid', 'Kareem', 'Hamid', 'Aziz', 'Ismail', 
            'Jamal', 'Hamza', 'Sohail', 'Zain', 'Shaheen', 'Gazali', 'Ahmad', 'Abid', 'Nashit', 'Umair', 'Suhail', 'Maqbool', 'Murtaza', 
            'Bilal', 'Nashwan', 'Kashif', 'Irshad', 'Saeed', 'Ibrahim', 'Muneer', 'Abdul', 'Aasim', 'Siddiq', 'Shamsuddin', 'Firoz', 'Javed']

    malyali_male_surname_muslim = ['Tariq', 'Kutty', 'Vallikkunnu', 'Koroth', 'Imran', 'Muneerali', 'Abdu', 'Muthalali',
            'Rahman', 'Chirath', 'Ali', 'Hamza', 'Syeda', 'Jaseem', 'Chalappuram', 'Said', 'Salim',
            'Mannan', 'Nadapuram', 'Majid', 'Meethal', 'Siddique', 'Palliyath', 'Fareed', 'Musthafa',
            'Khalid', 'Shiraz', 'Jasim', 'Faisal', 'Vahid', 'Ashraf', 'Pasha', 'Musliyar', 'Rasid', 'Bilal',
            'Ameer', 'Yousuf', 'Khan', 'Riyad', 'Shahid', 'Tharini', 'Noor', 'Khaleel', 'Hamid',
            'Abdulkareem', 'Bashir', 'Madhavath', 'Umar', 'Abid', 'Hussain', 'Shinash', 'Jaleel', 'Kunjahammed', 'Yusuf', 'Arafath', 'Feroze',
            'Nazar', 'Fahad', 'Nashid', 'Kader', 'Zaheer', 'Sulaimankutty', 'Burhan', 'Riyadh', 'Zameer', 'Syed',
            'Harun', 'Maqbool', 'Shihab', 'Aziz', 'Farooq', 'Rauf', 'Shuvo', 'Ghaus', 'Javed', 'Barakat', 'Shan',
            'Abdullah', 'Iqbal', 'Mohiuddin', 'Sulaiman', 'Sami', 'Shiraj', 'Majeed', 'Naseer', 'Shereef', 'Fazal',
            'Omar', 'Malik', 'Ibrahim', 'Nasir', 'Niyaz', 'Kunhalan', 'Azhar', 'Badr', 'Ilyas', 'Noorudeen', 'Jameel',
            'Amin', 'Manzil', 'Deen', 'Pookoya', 'Vaseem', 'Madar', 'Shamsu', 'Rafeeq', 'Saiful', 'Zulfikar', 'Adil',
            'Shahida', 'Vaidy', 'Ismail', 'Hafeez', 'Sajeer', 'Shanavas', 'Shahan', 'Al-Khansa', 'Nadir', 'Arshad',
            'Muneer', 'Shafi', 'Salahuddin', 'Rashid', 'Ashrafiya', 'Muhammad', 'Basheer', 'Madhav', 'Hassan', 'Kunhu',
            'Kareem', 'Latif', 'Kottayil', 'Naseem', 'Al-Hassan', 'Rayees', 'Zubair', 'Sharif', 'Zahra', 'Shihabudheen',
            'Suleman', 'Siddiq', 'Hashim', 'Shanmughan', 'Thangal', 'Aslam', 'Nassir', 'Rafi', 'Bashirudheen', 'Hidaya', 'Farook',
            'Rasak', 'Samiuddin', 'Ghani', 'Mustafa', 'Firoz', 'Nabir', 'Anwar', 'Ayoob', 'Ghouse', 'Saheer', 'Rukayya',
            'Javid', 'Riyaz', 'Zahid', 'Puthiyapalli', 'Alavi', 'Shamsudheen', 'Madrasi']

    malyali_female_firstname_muslim= [
            'Nawra', 'Farzana', 'Bint', 'Rafiya', 'Sumaya', 'Sofia', 'Reem', 'Shahira', 'Tabassum', 'Kainat', 'Shirin', 'Rimsha', 
            'Abeer', 'Suman', 'Lubna', 'Hasna', 'Raiza', 'Sumiya', 'Naila', 'Arifa', 'Esha', 'Fatma', 'Zubairah', 'Zehra', 'Sarai', 
            'Lailah', 'Shahida', 'Jameela', 'Zohra', 'Jasmine', 'Marwa', 'Maliha', 'Jabira', 'Najma', 'Aabida', 'Aisha', 'Ishraq', 
            'Maheen', 'Shazia', 'Sibah', 'Misha', 'Haneen', 'Arwa', 'Aysha', 'Areeba', 'Rida', 'Laila', 'Hawra', 'Shamima', 'Iqra', 
            'Fareeha', 'Shaista', 'Aila', 'Sundus', 'Nabila', 'Bilqis', 'Shaila', 'Raghda', 'Raniya', 'Simi', 'Zaynab', 'Rabiya', 
            'Fiza', 'Rabia', 'Amal', 'Sakina', 'Zahira', 'Shania', 'Sahar', 'Uzma', 'Gulsher', 'Ameera', 'Liya', 'Mariam', 'Muneera', 
            'Noor', 'Tasneem', 'Hamida', 'Ruqiah', 'Nashwa', 'Anjum', 'Anum', 'Madiha', 'Dina', 'Jumana', 'Ummul', 'Shaheena', 'Wafa', 
            'Nida', 'Raheel', 'Eman', 'Zainab', 'Poonam', 'Basma', 'Feroze', 'Fairooza', 'Sumaiya', 'Kamilah', 'Mirah', 'Kausar', 'Sobia', 
            'Fariha', 'Inas', 'Ruqayya', 'Mekka', 'Asma', 'Shanaz', 'Alima', 'Suma', 'Khatijah', 'Khadeeja', 'Sara', 'Ghazala', 'Nigha', 'Haya', 
            'Fathima', 'Mariya', 'Badriya', 'Haseena', 'Inaya', 'Sumaira', 'Rania', 'Afsana', 'Maisha', 'Nafisa', 'Tariqa', 'Jamila', 'Sima', 
            'Zara', 'Hafsa', 'Shayma', 'Aziza', 'Warda', 'Ghina', 'Abla', 'Ayesha', 'Farah', 'Zoya', 'Raheela', 'Tahira', 'Lana', 'Sadaf', 
            'Basmah', 'Kawthar', 'Aafiya', 'Ghadir', 'Dalal', 'Shaheen', 'Leena', 'Raheema', 'Afra', 'Rasha', 'Huda', 'Aleena', 'Anisa', 'Hina', 
            'Maha', 'Sajida', 'Jazmin', 'Rashida', 'Sanaa', 'Kamar', 'Syeda', 'Fatimah', 'Fatima', 'Maimuna', 'Fareeda', 'Ainul', 'Hanan', 
            'Muna', 'Asiya', 'Sana', 'Sufiya', 'Gulzar', 'Maheerah', 'Shireen', 'Zeenat', 'Rehama', 'Khadija', 'Ameerah', 'Meher', 'Nisreen', 
            'Sadia', 'Shatha', 'Khalida', 'Shanaya', 'Rima', 'Azra', 'Bushra', 'Alia', 'Raihana', 'Yasmin', 'Siti', 'Aminah', 'Lina', 'Asfiya', 
            'Samira', 'Bibi', 'Durrah', 'Hafeeza', 'Suhaila', 'Mehreen', 'Alya', 'Nehar', 'Saira', 'Dania', 'Shifa', 'Zubaida', 'Haniya', 
            'Zahra', 'Nisa', 'Muzna']



    malyali_female_surname_muslim= [
        "Abdullah", "Ali", "Khalid", "Ibrahim", "Muneer", "Said", "Shihab", "Rashid", "Nasir", "Zahid",
        "Amin", "Fahad", "Zubair", "Ameer", "Farooq", "Hassan", "Yusuf", "Riyad", "Rauf", "Feroze",
        "Alavi", "Kutty", "Kunjalikutty", "Muneer", "Pookoya", "Shihabudheen", "Madhavath", "Abdulkareem",
        "Thangal", "Fazal", "Vallikkunnu", "Mannan", "Muthalali", "Musliyar", "Nadapuram", "Chalappuram",
        "Koroth", "Palliyath", "Meethal", "Chekkan", "Syeda", "Zahra", "Hidaya", "Ashrafiya", "Rukayya",
        "Salahuddin", "Fatimah", "Al-Hassan", "Al-Khansa", "Shahida"]

    #christian names
    malyali_female_firstname_christian = [
        'Valsa', 'Veena', 'Cassia', 'Lydia', 'Aby', 'Deborah', 'Priscilla','Phoebe', 'Bethany', 'Princy',
        'Mili', 'Berenice', 'Glory', 'Nina', 'Saly','Abigail', 'Hannah', 'Anita', 'Noemi', 'Pamela', 'Mary',
        'Adah', 'Rahab', 'Esther', 'Thecla', 'Indu', 'Blessy', 'Hagar', 'Mercy', 'Juno', 'Gretta', 'Alma',
        'Dinah', 'Alina', 'Noadiah', 'Bilhah', 'Gracy', 'Judy', 'Phoebe', 'Delilah', 'Shiny', 'Miriam',
        'Eve', 'Clara', 'Madhavi', 'Elisheba', 'Rosy', 'Ednah', 'Naomi', 'Zeresh', 'Freda', 'Annu', 'Asha',
        'Avila', 'Bernice', 'Judith', 'Keziah', 'Catherine', 'Lana', 'Ester', 'Emily', 'Drusilla', 'Lizy',
        'Bathsheba', 'Elsa', 'Vashti', 'Sheryl', 'Julia', 'Alphonsa', 'Hilda', 'Nehemiah', 'Carmela',
        'Kavitha', 'Irene', 'Hephzibah', 'Cynthia', 'Zahra', 'Huldah', 'Harriet', 'Joan', 'Rebekah', 'Lilly',
        'Elizabeth',  'Hosanna', 'Carmel', 'Jemima', 'Ada', 'Susannah', 'Vineetha', 'Elisabeth', 'Michelle',
        'Anjali', 'Annamma', 'Jael', 'Leena', 'Galatia', 'carolin', 'smera', 'smitha','anny','shreya','kochumol',
        'rani','theresa','merin','neevan','preeval','jomol','Joanna','Zipporah','baby','Martha','neha','joshna',
        'angel','asha','ruth','lisha','binsha','sneha','aleena','jisty','ann','sona','navomi','maria','sara',
        'sera','ashley','aksa','aneeta','elisha','elona','anila','baby','sruthi',
        'susan','liyan','lena','sonia','steffy','benniticta','anu','anusha','anju',
        'anjusha','ajitha','shiny','febina','feby','jinsha','raechel','pearly','kochutheresa','kochurani','kochumaria','kunjumol',
        'kunjumariyam','mariyamma','anet','divya','deola','divina','rosy','rosamma','rose','soumya','Benna','binu','jinu','rhea','riya',
        'Janet','jessy','jaissy','mercy','stella','anna','celin','diana','jeni','jeny','moncy','lisha','jinsa','abi','abilin','mini','lovely',
        'jane','anisha','alisha','aneesha','nimmy','nimisha','mimi','jasna','merlin','jesslin','rosemary','annmaria','annmary','alinta']


    malyali_surname_christian= [
        'Thomasina', 'Chacko', 'philip','Rebecca', 'Changanassery', 'Kottayil', 'Salome', 'Mark', 'Mathew', 'Bernice', 'Tharayil', 
        'Puthankandy', 'Ellen', 'Vettukattil', 'Karimpalan', 'Mary', 'Kuriakose Elias', 'Peter', 'Cherian', 'Vellatt', 'Vattakuzhy', 
        'Kallookaran', 'David', 'Tharakan', 'Ruth', 'John', 'Chalakkudy', 'Freda', 'Thomas', 'Ouseph', 'Avittom', 'Jacob', 'Elizabeth', 
        'Kurian', 'Manalil', 'Catherine', 'Judith', 'Chali', 'Carmela', 'Martha', 'Jameson', 'Punnathoor', 'Huldah', 'Helen', 'Phoebe', 
        'Elisabeth', 'Matthew', 'Pillai', 'George', 'Edavanakkad', 'Poovathoor', 'Pathirikkal', 'Vadakkemadom', 'Davis', 'Joseph', 'Ester', 
        'Kuriakose', 'Kunnampurathu', 'Kappil', 'Kuttikkatt', 'Thottunga', 'Hannah', 'Kochuparambil', 'Rahab', 'Priscilla', 'Kizhakkethil', 
        'Kanjiramattom', 'Chavara', 'Mannappra', 'Maryann','mariyam', 'Bethel', 'Victoria', 'Tabitha', 'Abraham', 'Kallely', 'Clara', 
        'Charlotte', 'Karakatt', 'Sophia', 'Joanna', 'Pallath', 'Mazhavil', 'Annunziata', 'Miriam', 'Edward', 'Paul', 'Kottappuram', 
        'Sarah', 'James', 'Puthoor', 'Moolayil', 'Perera', 'Iype', 'Eve', 'Valanjickal', 'Jude', 'Varkey', 'Sally', 'Julia', 'Damaris', 
        'Esther', 'Mammen', 'Punnathra', 'Punnalan', 'Annie', 'Puthenveettil', 'Panayil', 'Varghese', 'Josephine', 'Magdalene', 'Lydia', 
        'Chittilapally', 'William', 'Benedict', 'Susannah', 'eepan''antony','Samuel','Kochu','kochuvadakel','kochuparambil','eepachen','joel',
        'Anoop','jose','thankachan','sunil','anand','Puthenpurackal','kudilil','jackson','godfrey','anish']
                            
    malyali_male_firstname_christian = [
        'Anand', 'Emanuel', 'Franklin', 'Leon', 'Shibu', 'Keith', 'Vinay', 'Alvin', 'Simon', 'Darwin', 'Nikhil', 'Benny',
        'Oliver', 'Nisam', 'Zachariah', 'Sajeev', 'arnold','Omar', 'Adarsh', 'Alfred', 'Levin', 'Winston', 'Sam', 'Arun',
        'Melvin', 'Nilesh', 'Glenn', 'Oscar', 'Aloysius', 'Vijay', 'David', 'Farhan', 'Markus', 'Loy', 'Vivek', 'Ivan',
        'Sibin', 'Nero', 'Irfan', 'Selvin', 'Titus', 'Abraham', 'Yohannan', 'Jomol', 'Uday', 'Savio', 'Salvio','sunny',
        'Sidney', 'James', 'Anil', 'Jude', 'Vishnu', 'Errol', 'Gerry', 'Luther', 'Yohan', 'Pradeep', 'Rishikesh', 'Rolf',
        'George', 'Josiah', 'Stefan', 'Philip', 'Dennis', 'Irvin', 'Tony', 'Linz', 'Manoj', 'Rochel', 'Jabir', 'Kishore',
        'Vijayan', 'Henry', 'Linton', 'Alok', 'Aldrin', 'Jonathan', 'Gregory', 'Zorav', 'Edwin', 'Thomas', 'Gilbert', 'Preston',
        'Harold','zacheriah', 'Zac', 'Sebastian', 'Jithin', 'Imran', 'Rohit', 'Vibin', 'Gokul', 'Janu', 'John', 'Prince', 'Raji',
        'Sunny', 'Micheal', 'Samuel', 'Stephen', 'Baron', 'Vishal', 'Noel', 'Reuben', 'Isaiah', 'Mark', 'Rajeev', 'Nivin', 'Ronnie',
        'Yash', 'Kiran', 'Tracy', 'Sherwin', 'Wilfred', 'Santhosh', 'Eric', 'Albert', 'Cyril', 'Eli', 'Renjit', 'Harvin', 'Anish',
        'Mose', 'Jashan', 'Cristian', 'Dev', 'Trevor', 'Kenny', 'Elwin', 'Nicky', 'Jerry', 'Roni', 'Lancy', 'Benjamin', 'Caleb',
        'Jonas', 'Job', 'Ramesh', 'Benson', 'Justin', 'Malvin', 'Anoop', 'Mohan', 'Ajay', 'Alen', 'Harrison', 'Dillan', 'Mervin',
        'Nevin', 'Dinesh', 'Aravind', 'Stanly', 'Rocky', 'Bonaventure', 'Paul', 'Victor', 'Siju', 'Joffin', 'Robin', 'Lelvin',
        'Mathew', 'Suni', 'Xavier', 'Stefen', 'Hari', 'Jeevan', 'Shane', 'Olivier', 'Kris', 'Dominic', 'Zubin', 'Sherin', 'Milan',
        'Keeran', 'Alex', 'William', 'Ishaan', 'Harris', 'Russell', 'Zach', 'Alben', 'Noah', 'Bobby', 'Siby', 'Joshua', 'Elvin',
        'Zachary', 'Sylvester', 'Rey', 'Vince', 'Ephraim', 'Binu', 'Jarvis', 'Biju', 'Ferdinand', 'Joseph', 'Pravin', 'Mithun',
        'Roy', 'Roshan', 'Jojy', 'Sidharth', 'Vikash', 'Nelson', 'Jayson', 'Jacob', 'Jorge', 'Vino', 'Samson', 'Benedict', 'Rohan',
        'Michael', 'Neeraj', 'Aswin', 'Wilson', 'Lazarus', 'Clyde', 'Gerald', 'Vimal', 'Ajesh', 'Basil', 'Glen', 'Vincent', 'Vyas',
        'Alphonse', 'Shan', 'Lancelot', 'Davis', 'Matthew', 'Isaac', 'reji','Leo','babu','bobby','boby','vinod','ashvil','roshan',
        'jibin','jebin' 'zubin','georgekutty','shaji','jai','benny','saji','biju','markose','nixon','rixon','rinto','robin','libin',
        'linto','jerry','tom','tomson','joy','prince','rajan','Alexander','sajin','sachin','jomon','johnny','nelvin','melbin','Shijo','arthur','martin',
        'sam','ajay','abel','faein',
        'fein','basil','tovino','antonio','albin','vivin','vibin','sharon','akhil','stelins','stebin','jude','vinay','ashin','stejin','jojo',
        'jobin']
    # Religion Percentages
    religion_distribution = {
        'male': {'hindu': 40, 'muslim': 40, 'christian': 20},
        'female': {'hindu': 40, 'muslim': 40, 'christian': 20}
    }

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Helper function to generate names based on count and type
    def generate_religious_names(count, firstnames, surnames, gender):
        for _ in range(count):
            first_name = random.choice(firstnames)
            surname = random.choice(surnames)
            if preferences.get('name_type') == 'first':
                names.append((first_name, gender))
            else:
                names.append((f"{first_name} {surname}", gender))

    # Divide counts based on gender
    male_count = n // 2
    female_count = n - male_count

    # Generate male names
    generate_religious_names(
        int(male_count * religion_distribution['male']['hindu'] / 100), 
        malyali_male_firstname_hindu, 
        malyali_male_surname_hindu, 
        "Male"
    )
    generate_religious_names(
        int(male_count * religion_distribution['male']['muslim'] / 100), 
        malyali_male_firstname_muslim, 
        malyali_male_surname_muslim, 
        "Male"
    )
    generate_religious_names(
        int(male_count * religion_distribution['male']['christian'] / 100), 
        malyali_male_firstname_christian, 
        malyali_surname_christian, 
        "Male"
    )

    # Generate female names
    generate_religious_names(
        int(female_count * religion_distribution['female']['hindu'] / 100), 
        malyali_female_firstname_hindu, 
        malyali_female_surname_hindu, 
        "Female"
    )
    generate_religious_names(
        int(female_count * religion_distribution['female']['muslim'] / 100), 
        malyali_female_firstname_muslim, 
        malyali_female_surname_muslim, 
        "Female"
    )
    generate_religious_names(
        int(female_count * religion_distribution['female']['christian'] / 100), 
        malyali_female_firstname_christian, 
        malyali_surname_christian, 
        "Female"
    )

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_kerala_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df
