import random
import pandas as pd
import os


# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

#  Female First Names and Surnames
def generate_female_names(n, user_preference=None):

    # Kerala Female First Names
    female_firstname_hindu =  [ "Abha", "Akanksha", "Anandi", "Aradhana", "Archana", "Arpana", "Arpitha", "Astha", 
    "Bhagavanti", "Bhagvanti", "Bindhu", "Chakori", "Chandni", "Chandra", "Chandramukhi", 
    "Charu", "Chaya", "Deepa", "Deepika", "Dhanwanti", "Disha", "Divya", "Gaura", "Gauri", 
    "Geetika", "Gunjan", "Hansi", "Heera", "Jyotnsa", "Kajal", "Kali", "Kalika", 
    "Kalpana", "Kamala", "Kamana", "Kangan", "Kanta", "Kanya", "Kasturi", "Kavita", 
    "Kesari", "Kishori", "Komal", "Kusum", "Lajja", "Lalita", "Madhuri", "Mahak", "Mahima", 
    "Mala", "Mandodari", "Maneesha", "Manorama", "Manushi", "Mayuri", "Megha", "Meghana", 
    "Mohini", "Mukta", "Namrata", "Neelima", "Neera", "Neeru", "Neeta", "Niharika", 
    "Nirmala", "Nisha", "Nupur", "Pallavi", "Payal", "Pooja", "Poonam", "Poornima", 
    "Prabhavati", "Pragathi", "Prakash", "Prakrithi", "Priya", "Pushpa", "Rajkumari", 
    "Raka", "Ratna", "Ratnadevi", "Ritu", "Ruchira", "Sandhya", "Santhoshi", 
    "Sanwati", "Sarita", "Saroja", "Sashi", "Saundarya", "Savita", "Seeta", "Shagun", 
    "Shakun", "Shantidevi", "Sharmili", "Shyama", "Sugandha", "Sujatha", "Sukumari", 
    "Suman", "Sumathi", "Sunanya", "Swarna", "Sweta", "Tara", "Tarika", 
    "Usha", "Vandana", "Varsha", "Vasanthi", "Veena", "Vijaya", "Vineeta", "Yamini","Jyothi",
    "Shakuntala", "Maina", "Naga", "Salabha", "Kokil", "Mangala", "Saubhagya", "Shantha", "Suguņa",
    "Mamata", "Shobhana", "Priyamvada", "Suhasini", "Subhasini", "Sulochana", "Susheela", "Madhuri",
    "Shalini", "Sharada", "Usha", "Laxmi", "Thellamma", "Shyamă", "Shyamala", "Parvathi", "Saraswathi", "Sitha",
    "Savitha", "Savithri", "Gayathri", "Girija", "Shailaja", "Swarņamma", "Thangamma", "Suvarna", "Sonali", "Hiranya",
    "Kanchana", "Kanakavalli", "Kanagi", "Hamalata", "Ratnamma", "Maragadavally", "Muthulakshmi", "Thulasi", "Latha",
    "Lathika", "Vally", "Lavangika", "Saroja", "Kusuma", "Mallika", "Pushpa", "Mallika",
    "Ganga", "Jamuna", "Saraswati", "Kaveri", "Godavari", "Thunga", "Narmada", "Kaphini", "Gomathi",
    "Vasana", "Sugandha", "Saurabha", "Chandanavally", "Kasturi", "Surabhi", "Manjari", "Asvathi", "Kartika", "Rohini",
    "Swathi", "Rewathi", "Chandraprabha", "Chothi", "Tirunal", "Avittham", "Veena", "Dhwani", "Geetha",
    "Sangeetha", "Chitra", "Chitrarupa", "Chitrar", "Chitralekha", "Indumathi", "Menaka",
     "Jyotsna", "Rashmi", "Deepti", "Prabha", "Kanti", "Shashikala", "Abhilasha", "Aditi", 
     "Alochana", "Amala", "Amarava", "Amba", "Ambalika", "Ambara", "Ambika", "Ameesha", "Amogha", "Amrita", 
    "Anagha", "Anamika", "Anandi", "Ananta", "Anantalaxmi", "Ananya", "Anargha", "Anasuya", "Anavadya", 
    "Anchal", "Aneeta", "Angana", "Anila", "Anima", "Anindita", "Anjali", "Anjana", "Ankita", "Annapurna", 
    "Antara", "Anubha", "Anuja", "Anukampa", "Anukriti", "Anumiti", "Anupama", "Anuprabha", "Anupriya", 
    "Anuradha", "Anurekha", "Anushna", "Anusuya", "Anvita", "Anviti", "Aparajita", "Aparna", "Apeksha", 
    "Apurti", "Aradhana", "Arasi", "Arati", "Archana", "Archita", "Arpana", "Arpita", "Aruna", "Arundati", 
    "Arunima", "Arushi", "Asha", "Ashlesha", "Asita", "Asmita", "Astha", "Atreyi", "Badala", "Bela", 
    "Bhagavati", "Bhakti", "Bhamini", "Bhanu", "Bhanuja", "Bhanumati", "Bharati", "Bhavana", "Bhavya", 
    "Bhawani", "Bijali", "Bijli", "Bindiya", "Bulbul", "Chakori", "Chanchala", "Chandana", "Chandrakala", 
    "Chandralekha", "Chandramukhi", "Chandrani", "Chandraprabha", "Chandravati", "Chandravati Tiwari", 
    "Chandrika", "Charchita", "Charu", "Charulochana", "Chetana", "Chhabili", "Dakshayani", 
    "Damayanti", "Damini", "Daya", "Deeksha", "Deepali", "Deepanjali", "Deepika", "Deepti", "Deshna", 
    "Devaki", "Devakirti", "Devapriya", "Devashri", "Devasmita", "Devayani", "Devi", "Devika", "Dharana", 
    "Dharini", "Dhatri", "Disha", "Diva", "Divya", "Draupadi", "Duhita", "Durga", "Ekta", "Gagana", "Gajra", 
    "Gargi", "Garima", "Gaurangi", "Gauri", "Gaveshana", "Gayatri", "Geeta", "Geetanjali", "Geetika", 
    "Girija", "Godhavari", "Gopika", "Greeshma", "Guncha", "Gunjan", "Haimawati", "Hansa", "Hansi", "Hansika", 
    "Havisha", "Hemani", "Ichchha", "Iksa", "Ikshana", "Ikshita", "Ila", "Indira", "Indirani", "Indrani", 
    "Indu", "Indumati", "Ipsa", "Ipsita", "Ira", "Janaki", "Jeevana", "Jhelam", "Juhi", "Juthika", "Kadambari", 
    "Kajal", "Kalika", "Kalindi", "Kamala", "Kamini", "Kankan", "Kanta", "Kasturi", "Kaushalya", "Ketaki", 
    "Kirana", "Krittika", "Kshama", "Kumkum", "Kumud", "Kumudini", "Kunti", "Kusum", "Lahari", "Lajja", 
    "Lalita", "Lata", "Latika", "Laxmi", "Lopamudra", "Maanvi", "Madalasa", "Madhavi", "Madubala", "Mahamaya", 
    "Mahasweta", "Mahaswetha", "Maithili", "Maitreyi", "Mala", "Malathi", "Malavika", "Mallika", "Mandakini", 
    "Mandavi", "Mandodari", "Maneesha", "Mangala", "Maniprabha", "Manisha", "Manjari", "Manjira", "Manjoosha", 
    "Manju", "Manjula", "Manjushri", "Manorama", "Mansa", "Mansi", "Maya", "Mayuri", "Medha", "Medini", "Meena", 
    "Meenakshi", "Megha", "Meghana", "Mekhala", "Menaka", "Mita", "Mitali", "Modini", "Mohini", "Moksha", 
    "Mona", "Mridula", "Mrigakshi", "Mrinal", "Mrinalini", "Mudita", "Mugdha", "Mukta", "Mukti", "Muskan", 
    "Namita", "Namrata", "Nanda", "Nandini", "Nandita", "Narayani", "Naveena", "Nayana", "Neeharika", "Neelam", 
    "Neelima", "Neena", "Neera", "Neerada", "Neeraja", "Neeta", "Neha", "Nidhi", "Nimisha", "Niranjana", 
    "Nirjhari", "Nirjharini", "Nirmala", "Nirupama", "Nisha", "Nishchala", "Nishitha", "Nishtha", "Nitya", 
    "Niyati", "Noopur", "Nootan", "Nupur", "Padma", "Padmaja", "Padmavati", "Padmini", "Pakhi", "Palak", 
    "Pallavi", "Pankhuri", "Parakh", "Parameshvari", "Parameshwari", "Parikalpana", "Parikha", "Parikrama", 
    "Parimal", "Parul", "Parvati", "Pataka", "Paulomi", "Pavana", "Pavitra", "Payal", "Phankudi", "Pipeelika", 
    "Poojita", "Poorna", "Poornima", "Poorvi", "Poosha", "Prabha", "Prabhavati", "Prachi", "Prachura", 
    "Pragati", "Pragya", "Prakriti", "Pramila", "Pramodini", "Pramudita", "Pranati", "Praneeta", "Pranvi", 
    "Prarthita", "Prashamsha", "Prasiddhi", "Prateeksha", "Prateeti", "Prathiksha", "Pratibha", "Pratigya", 
    "Pratima", "Pratishtha", "Preeti", "Prerana", "Preyasi", "Prithvi", "Priya", "Priyadarshini", "Priyamvada", 
    "Priyanka", "Pulak", "Puloma", "Puneeta", "Pushipta", "Pushpa", "Pushpanjali", "Rachana", "Radha", "Ragini", 
    "Rajani", "Rajanigandha", "Rajkumari", "Rajni", "Rajyalaxmi", "Rajyashri", "Raka", "Rakhi", "Raksha", 
    "Rakshita", "Rama", "Ramana", "Ramba", "Ramya", "Rani", "Rasana", "Rashmika", "Rasmi", "Rati", 
    "Ratna", "Ratnavali", "Ratnottama", "Reena", "Rekha", "Renu", "Renuka", "Revati", "Rewati", "Riddhi", 
    "Ridhi", "Ritambhara", "Ritu", "Rituja", "Robini", "Roma", "Romila", "Roopa", "Roopali", "Roopashri", 
    "Roopasi", "Roopmati", "Rooprekha", "Roshani", "Ruchi", "Ruchira", "Rukma", "Rukmini", "Rukumani", "Rupa", 
    "Rupali", "Rupasi", "Sagarika", "Salila", "Sameera", "Sangita", "Sapna", "Sarbhati", "Sargam", "Satyabhama", 
    "Satyavati", "Satyawati", "Satywati", "Savitri", "Shachi", "Shagun", "Shaila", "Shailaja", "Shaival", "Shaivya", 
    "Shaiya", "Shakun", "Shakuntala", "Shalabha", "Shalini", "Shalvi", "Shampa", "Shanta", "Shanti", "Sharada", 
    "Sharmishta", "Sharwari", "Shashi", "Shashikala", "Shefali", "Shikha", "Shilpa", "Shivani", "Shobha", 
    "Shoma", "Shradha", "Shraddha", "Shravani", "Shravya", "Shrestha", "Shubhi", "Shubhra", "Shubham", "Siddhi", 
    "Simran", "Sindhu", "Sitara", "Smita", "Sneha", "Sonal", "Sonalika", "Sreeja", "Srilata", "Suman", "Sumati", 
    "Sumanja", "Sumita", "Sumitra", "Sushila", "Sushmita", "Sushruta", "Swati", "Swetlana", "Tanaya", 
    "Tanirika", "Tanuja", "Tanushree", "Tara", "Tithira", "Trishala", "Tripti", "Trisha", "Triveni", "Tulika", 
    "Uma", "Urmi", "Urmila", "Vasudha", "Vasundhara", "Veda", "Vedika", "Vidhya", "Vijaya", 
    "Vijayalakshmi", "Vilasini", "Vishakha", "Vishali", "Vishnupriya", "Yamini", "Yamuna", "Yashoda", "Yashika", 
    "Yogita", "Yukti",'Vidya', 'Kanaka', 'Yashoda', 'Charutha', 'Shruthi', 'Damini', 'Neeraja', 'Sumathi', 'Shubha', 'Pooja', 'Jyothi', 'Sadhvi', 'Avani',
        'Tejaswini', 'Ujjwala', 'Renuka', 'Aruna', 'Darika', 'Bhavini', 'Varsha', 'Gajani', 'Meena', 'Sajini', 'Tharini',
        'Vinaya', 'Dhanya', 'Navya', 'Bhavani', 'Thara', 'Jeevitha', 'Meenal', 'Preethi', 'Rama', 'Mohana', 'Ammu', 'Jagruti', 'Bhavana',
        'Lakshmi', 'Bhavya', 'Mithra', 'Amritha', 'Ishwari', 'Karthika', 'Arya', 'Gita', 'Chandralekha', 'Daksha', 'Manjula', 'Lakshmipriya',
        'Haritha', 'Alaka', 'Sadhana', 'Sarika', 'Nandhini', 'Sharmila', 'Devi', 'Sangeetha', 'Sharanya', 'Malathi', 'Rohini', 'Manjari',
        'Poornima', 'Pavani', 'Gokila', 'Maya', 'Suman', 'Nithila', 'Vennila', 'Gajini', 'Vidhitha', 'Prasanna', 'Anupama', 'Meera', 'Radha',
        'Aishwarya', 'Chithra', 'Kushala', 'Sangeeta', 'Charushila', 'Madhavi', 'Sushila', 'Krishna', 'Shanthi', 'Eshitha', 'Manasi', 'Sushmita',
        'Hamsini', 'Sujatha', 'Durga', 'Aiswarya', 'Chandrika', 'Anjana', 'Gajalakshmi', 'Gauri', 'Sindu', 'Anisha', 'Ragini',
        'Arundhathi', 'Lalitha', 'Sruthi', 'Sushma', 'Disha', 'Kalyanika', 'Bhavitha', 'Vishwajeet', 'Yogitha', 'Rajeswari','Madhubala',
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
        'Deepti', 'Shilpa', 'Kalpana', 'Shrini', 'Riya', 'Vijaya', 'Sreelekshmi', 'Anagha', 'Nayana', 'Swara', 'Saranya',
        'Pushpavathy', 'Tilakavathy', 'Padmavathy', 'Suryavathy', 'Kalavathy', 'Amruthavalli','Maragathavalli', 'Kanagavalli',
         'Pushpavalli', 'Chandanavalli', 'Swarnavalli', 'Shanthakutti','Sharadakutti', 'Aneethakutti', 'Madhumatimathi', 'Indumathi',
         'Chandramathi', 'Shashikala','Chandrakala', 'Chandralekha', 'Chitralekha', 'Jayashri', 'Bhagyashri', 'Ratnashri', 'Anushri',
          'Manjushri', 'Gayathridevi', 'Shridevi', 'Savithridevi', 'Renukadevi', 'Ramadevi', 'Vijayalaxmilaxmi', 'Subbalaxmi', 'Mahalaxmi',
        'Rajyalaxmi', 'Muthulaxmi', 'Remabai', 'Kundanabai', 'Kanakabai', 'Sugathakumari', 'Anithakumari', 'Shashikumari', 'Santhakumari',
         'Padmakumari', 'Vasanthakumari', 'Manjularani', 'Shashirani', 'Shreelatha', 'Chandanalatha', 'Kanagalatha', 'Indubala', 'Shashibala'
        ]
    
    female_surname_hindu =  ['Vishnu', 'Kannan', 'Yadav', 'Shubhi', 'Nagarajan', 'Venkatesan', 'Vijayan', 'Chakyar', 'Harish', 'Govindan', 'Saxena',
                             'Tiwari', 'Sreenivasan', 'Anand', 'Pooja', 'Chitra', 'Gupta', 'Haridas', 'Dixit', 'Sathish', 'Mukherjee', 'Asha', 'Vishali',
                             'Ravindran', 'Shobha', 'Sonal', 'Deepika', 'Nair', 'Kamala', 'Ramachandran', 'Menon', 'Radhika', 'Harikrishnan', 'Radha', 'Anjali',
                             'Anoop', 'Chatterjee', 'Sushila', 'Sood', 'Bhide', 'Aravind', 'Neha', 'Sahu', 'Kothari', 'Rajeshwari', 'Vandana', 'Narayana',
                             'Bharath', 'Sen', 'Soman', 'Kachroo', 'Savitri', 'Thakur', 'Vayalil', 'Rajagopal', 'Reddy', 'Raj', 'Sangeeta', 'Swathi', 'Sahai',
                             'Indira', 'Patel', 'Agarwal', 'Sankaran', 'Sadhukhan', 'Bindiya', 'Venu', 'Priya', 'Subhadra', 'Pandey', 'Rathi', 'Eapen',
                             'Rathnakumar', 'Nirmal', 'Kavitha', 'Parvati', 'Kailas', 'Hemanth', 'Puri', 'Shinde', 'Chandran', 'Madhavi', 'Gopalakrishnan',
                             'Pillai', 'Vasudevan', 'Durga', 'Rukmini', 'Sita', 'Kalpana', 'Kurian', 'Ramesh', 'Balakrishnan', 'Gopal', 'Bansal', 'Raghavan',
                             'Balan', 'Warrier', 'Ravi', 'Khandelwal', 'Sastri', 'Rajendran', 'Venkiteswaran', 'Krishna', 'Suresh', 'Sushmita', 'Suman',
                             'Ramaswamy', 'Madhavan', 'Gokul', 'Trivedi', 'Sandeep', 'Joshi', 'Aarti', 'Shanil', 'Nadapran', 'Rajesh', 'Ritika', 'Shukla',
                             'Ghosh', 'Vijayalaxmi', 'Anil', 'Prathapan', 'Rekha', 'Sivadas', 'Prasanna', 'Vaidya', 'Gopinathan', 'Madhusoodhanan',
                             'Bhairavi', 'Chandrika', 'Sunil', 'Sreejith', 'Ramani', 'Murali', 'Bhattacharya', 'Panchal', 'Jayan', 'Rathnakaran', 'Krishnan',
                             'Sharma', 'Padmini', 'Shastri', 'Srinivasan', 'Rai', 'Vaidyar', 'Sankar', 'Choudhury', 'Bhardwaj', 'Shalini', 'Sundaram', 'Hariharan',
                             'Ramanan', 'Namboothiri', 'Rajeev', 'Sarojini', 'Vishwanathan', 'Dey', 'Gowda', 'Lalita', 'Pradeep', 'Nambudiripad', 'Bhaskar', 'Simran',
                             'Murthy', 'Shaan', 'Lakshmanan', 'Neelam', 'Narayani', 'Gandhi', 'Sridhar', 'Jha', 'Kochuparambil', 'Rama', 'Kollath', 'Shaji', 'Sundar',
                             'Vikram', 'Ajayan', 'Iyer', 'Lal', 'Bharadwaj', 'Vasundhara', 'Nellikkal', 'Nambiar', 'Bedi', 'Nivedita', 'Lakshmi', 'Desai',
                             'Meenakshi', 'Kanak', 'Ganesh', 'Varsha', 'Choudhary', 'Deepak', 'Ankita', 'Kurup', 'Mishra', 'Kashyap', 'Jaya', 'Thampi',
                             'Prakash', 'Raghu', 'Kumar', 'Rao', 'Chidambaram', 'Bhagwat', 'Chakraborty', 'Suryanarayan']
    

    
    #Muslim names
    female_firstname_muslim= [
        'Nawra', 'Farzana', 'Bint', 'Rafiya', 'Sumaya', 'Sofia', 'Reem', 'Shahira', 'Tabassum', 'Kainat', 'Shirin', 'Rimsha', 'Abeer', 
        'Suman', 'Lubna', 'Hasna', 'Raiza', 'Sumiya', 'Naila', 'Arifa', 'Esha', 'Fatma', 'Zubairah', 'Zehra', 'Sarai', 'Lailah', 'Shahida', 
        'Jameela', 'Zohra', 'Jasmine', 'Marwa', 'Maliha', 'Jabira', 'Najma', 'Aabida', 'Aisha', 'Ishraq', 'Maheen', 'Shazia', 'Sibah', 'Misha', 
        'Haneen', 'Arwa', 'Aysha', 'Areeba', 'Rida', 'Laila', 'Hawra', 'Shamima', 'Iqra', 'Fareeha', 'Shaista', 'Aila', 'Sundus', 'Nabila', 
        'Bilqis', 'Shaila', 'Raghda', 'Raniya', 'Simi', 'Zaynab', 'Rabiya', 'Fiza', 'Rabia', 'Amal', 'Sakina', 'Zahira', 'Shania', 'Sahar', 
        'Uzma', 'Gulsher', 'Ameera', 'Liya', 'Mariam', 'Muneera', 'Noor', 'Tasneem', 'Hamida', 'Ruqiah', 'Nashwa', 'Anjum', 'Anum', 'Madiha', 
        'Dina', 'Jumana', 'Ummul', 'Shaheena', 'Wafa', 'Nida', 'Raheel', 'Eman', 'Zainab', 'Poonam', 'Basma', 'Feroze', 'Fairooza', 'Sumaiya', 
        'Kamilah', 'Mirah', 'Kausar', 'Sobia', 'Fariha', 'Inas', 'Ruqayya', 'Mekka', 'Asma', 'Shanaz', 'Alima', 'Suma', 'Khatijah', 'Khadeeja', 
        'Sara', 'Ghazala', 'Nigha', 'Haya', 'Fathima', 'Mariya', 'Badriya', 'Haseena', 'Inaya', 'Sumaira', 'Rania', 'Afsana', 'Maisha', 
        'Nafisa', 'Tariqa', 'Jamila', 'Sima', 'Zara', 'Hafsa', 'Shayma', 'Aziza', 'Warda', 'Ghina', 'Abla', 'Ayesha', 'Farah', 'Zoya', 
        'Raheela', 'Tahira', 'Lana', 'Sadaf', 'Basmah', 'Kawthar', 'Aafiya', 'Ghadir', 'Dalal', 'Shaheen', 'Leena', 'Raheema', 'Afra', 'Rasha', 
        'Huda', 'Aleena', 'Anisa', 'Hina', 'Maha', 'Sajida', 'Jazmin', 'Rashida', 'Sanaa', 'Kamar', 'Syeda', 'Fatimah', 'Fatima', 'Maimuna', 
        'Fareeda', 'Ainul', 'Hanan', 'Muna', 'Asiya', 'Sana', 'Sufiya', 'Gulzar', 'Maheerah', 'Shireen', 'Zeenat', 'Rehama', 'Khadija', 
        'Ameerah', 'Meher', 'Nisreen', 'Sadia', 'Shatha', 'Khalida', 'Shanaya', 'Rima', 'Azra', 'Bushra', 'Alia', 'Raihana', 'Yasmin', 
        'Siti', 'Aminah', 'Lina', 'Asfiya', 'Samira', 'Bibi', 'Durrah', 'Hafeeza', 'Suhaila', 'Mehreen', 'Alya', 'Nehar', 'Saira', 'Dania', 
        'Shifa', 'Zubaida', 'Haniya', 'Zahra', 'Nisa', 'Muzna']


    female_surname_muslim= [
        "Abdullah", "Ali", "Khalid", "Ibrahim", "Muneer", "Said", "Shihab", "Rashid", "Nasir", "Zahid",
        "Amin", "Fahad", "Zubair", "Ameer", "Farooq", "Hassan", "Yusuf", "Riyad", "Rauf", "Feroze",
        "Alavi", "Kutty", "Kunjalikutty", "Muneer", "Pookoya", "Shihabudheen", "Madhavath", "Abdulkareem",
        "Thangal", "Fazal", "Vallikkunnu", "Mannan", "Muthalali", "Musliyar", "Nadapuram", "Chalappuram",
        "Koroth", "Palliyath", "Meethal", "Chekkan", "Syeda", "Zahra", "Hidaya", "Ashrafiya", "Rukayya",
        "Salahuddin", "Fatimah", "Al-Hassan", "Al-Khansa", "Shahida"]

    #christian names
    female_firstname_christian = [
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
        'susan','liyan','lena','sonia','steffy','anu','anusha','anju',
        'anjusha','ajitha','shiny','febina','feby','jinsha','raechel','pearly','kochutheresa','kochurani',
        'kochumaria','kunjumol','kunjumariyam','mariyamma','anet','divya','deola','divina','rosy','rosamma','rose','soumya','Benna',
        'binu','jinu','rhea','riya','Janet','jessy','jaissy','mercy','stella','anna','celin','diana','jeni','jeny','moncy','lisha','jinsa',
        'abi','abilin','mini','lovely','jane','anisha','alisha','aneesha','nimmy','nimisha','mimi','jasna','merlin','jesslin','rosemary',
        'annmaria','annmary','alinta',
        'Ananya', 'Angelina', 'Alina', 'Sharanya', 'Simone', 'Irene', 'Lena', 'Sonia', 'Tina', 'Lilian', 
    'Benedicta', 'Margaret', 'Gabriella', 'Theresa', 'Gertrude', 'Ruth', 'Tessy', 'Selina', 'Regina', 
    'Sharmila', 'Sylvia', 'Cynthia', 'Reba', 'Sereena', 'Luzia', 'Anushka', 'Mariya', 'Solomon', 'Alfiya', 
    'Ashwini', 'Sheena', 'Beatrice', 'Alessandra', 'Dolly', 'Tharika', 'Rosaline', 'Bernadette', 'Evelyn', 
    'Charity', 'Christina', 'Sharine', 'Sabina', 'Monika', 'Susie', 'Saira', 'Nellie', 'Patricia', 'Sushila', 
    'Claudia', 'Miriam', 'Selma', 'Edith', 'Martha', 'Kavitha', 'Carolina', 'Sarita', 'Vishali', 'Sonali', 
    'Tanisha', 'Sangeetha', 'Jerin', 'Clementine', 'Yasmin', 'Farida', 'Sofiya', 'Dulcie', 'Angeline', 
    'Maya', 'Judy', 'Josephine', 'Aruna', 'Sofi', 'Fatima', 'Saraswati', 'Betty', 'Princy', 'Veena', 
    'Fabiola', 'Felicia', 'Parvathy', 'Patricia', 'Lakshmi', 'Aileen', 'Madhavi', 'Reshma', 'Gilda', 
    'Ursula', 'Philomena', 'Carmela', 'Pinky', 'Ritha', 'Giselle', 'Chitra', 'Ragini', 'Joanna', 'Sasha', 
    'Zita', 'Chantal', 'Krishna', 'Lathika', 'Prema', 'Anita', 'Sophia', 'Joya', 'Jerusha', 'Tania', 
    'Ophelia', 'Daisy', 'Sophie', 'Clementina', 'Diana', 'Bessy', 'Michele', 'Angel', 'Sophie', 'Rochelle',
    'Priscilla', 'Sanchita', 'Esther', 'Theresa', 'Clarissa', 'Edna', 'Rachael', 'Hilda', 'Beulah', 'Dorothy',
    'Patty', 'Leena', 'Rahel', 'Chandrika', 'Elina', 'Meera', 'Amala', 'Nisha', 'Siri', 'Vimala', 'Estelle']


    female_surname_christian= [
        'Thomasina', 'Philip','Rebecca', 'Salome','Bernice','Ellen', 'Peter',
        'David',  'Ruth', 'John',  'Freda', 'Thomas', 'Ouseph', 'Avittom', 'Jacob', 'Elizabeth', 
        'Kurian',  'Catherine', 'Judith', 'Chali', 'Carmela', 'Martha', 'Jameson', 'Punnathoor', 'Huldah', 'Helen', 'Phoebe', 
        'Elisabeth', 'Matthew',  'George', 'Edavanakkad', 'Davis', 'Joseph', 'Ester', 
        'Hannah', 'Mariyam', 'Bethel', 'Victoria', 'Tabitha', 'Abraham', 'Kallely', 'Clara', 
        'Charlotte', 'Karakatt', 'Sophia', 'Joanna', 'Pallath', 'Mazhavil', 'Annunziata', 'Miriam', 'Edward', 'Paul',  'Sarah', 
        'James', 'Puthoor', 'Moolayil', 'Perera', 'Iype', 'Eve', 'Valanjickal', 'Jude', 'Varkey', 'Sally', 'Julia', 'Damaris', 'Esther', 
        'Annie', 'Puthenveettil', 'Panayil', 'Varghese', 'Josephine', 'Magdalene', 'Lydia',  
        'William', 'Benedict', 'Susannah', 'Samuel','Abraham', 'Alex', 'Alexander', 'Almeida', 'Andrews', 'Antony', 'Benjamin', 
    'Chacko', 'Chandy', 'Cherian', 'Fernandes', 'Francis', 'George', 'Jacob', 
    'James', 'Joseph', 'Kuriakose', 'Mathew', 'Paul', 'Philip', 'Thomas', 
    'Varghese', 'Abraham', 'Kochamma', 'Mathews', 'Silva', 'D’Souza', 
    'Menezes', 'Sequeira', 'Gonsalves', 'Mascarenhas', 'Pereira', 'Pinto', 
    'Noronha', 'Lobo', 'Rodrigues', 'Carvalho', 'Dias', 'D’Cruz', 'John', 
    'Mark', 'Luke', 'Noel', 'Angel', 'Grace', 'Mercy', 'Hannah', 'Rebecca', 
    'Ruth', 'Tabitha', 'Anna', 'Miriam', 'Leah', 'Martha', 'Salome', 'Phoebe', 
    'Clara', 'Victoria', 'Charlotte', 'Sophia', 'Amala', 'Jaya', 'Catherine', 
    'Theresa', 'Veronica', 'Rosalyn', 'Lourdes', 'Mariamma', 'Elisabeth', 
    'Christina', 'Daphne', 'Seline', 'Marina', 'Ann', 'Maria', 'Alice', 
    'Carmel', 'Lucy', 'Juliet', 'Agnes', 'Serena', 'Patricia', 'Gloria', 
    'Bernadette', 'Angelina', 'Joanna', 'Paulina', 'Antonia', 'Audrey', 
    'Evangelina', 'Natasha', 'Monica', 'Regina', 'Grace', 'Helena', 'Felicia', 
    'Irene', 'Jennifer', 'Jessica', 'Margaret', 'Beatrice', 'Evangeline', 
    'Diana', 'Mabel', 'Rosaline', 'Selina'
        ]

     # Define religion percentages
    religion_percentages = {'hindu': 70, 'muslim': 20, 'christian': 10}

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names
    names = []

    # Generate names based on religion percentages
    for _ in range(n):
        # Determine religion based on percentage
        random_percentage = random.randint(1, 100)
        if random_percentage <= religion_percentages['hindu']:
            first_name = random.choice(female_firstname_hindu)
            last_name = random.choice(female_surname_hindu)
        elif random_percentage <= religion_percentages['hindu'] + religion_percentages['muslim']:
            first_name = random.choice(female_firstname_muslim)
            last_name = random.choice(female_surname_muslim)
        else:
            first_name = random.choice(female_firstname_christian)
            last_name = random.choice(female_surname_christian).capitalize()

        # Generate the full or first name based on user preferences
        if preferences.get('name_type') == 'first':
            name = first_name  # Only first name
        else:
            name = first_name + " " + last_name  # Full name

        # Append the name to the list
        names.append(name)

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name"])

    # Write to CSV file
    file_path = 'generated_female_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df                           
