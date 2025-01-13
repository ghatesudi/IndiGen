import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

# Bihar Male and Female First Names and Surnames
def generate_tribal_names(n, user_preference=None):

    #Bodo_tribal _names
    bodo_male_names = [
        "Ajoy", "Alok", "Amrit", "Angmoi", "Baishnu", "Balin", "Bamon", "Basu", 
        "Belir", "Benai", "Biswa", "Bhaku", "Bikram", "Binesh", "Bodhi", "Brahma", 
        "Chandram", "Chanmoy", "Chasing", "Chintho", "Chiti", "Chirag", "Daho", 
        "Dhiren", "Dinesh", "Dinjoy", "Dwijen", "Gokul", "Ganesh", "Gobin", "Gokoi", 
        "Ghora", "Gokol", "Hemin", "Hiran", "Hemto", "Himan", "Jiten", "Jagai", 
        "Jimal", "Jhumon", "Khamjang", "Khoshio", "Kamal", "Karan", "Kotin", "Kundan", 
        "Lahon", "Loken", "Lutfu", "Luit", "Manindra", "Mangal", "Minto", "Monoj", 
        "Mungsir", "Mojoy", "Munim", "Nabin", "Nayan", "Niranjan", "Nitai", "Narayan", 
        "Pandit", "Pintu", "Preshit", "Phul", "Partho", "Rajesh", "Rajkumar", "Rajdeep", 
        "Ranjit", "Ramesh", "Ratan", "Roshni", "Rituraj", "Sagar", "Sanjoy", "Suman", 
        "Suraj", "Sukal", "Shankar", "Santi", "Subho", "Tuhin", "Thong", "Thabil", 
        "Trinayan", "Tapan", "Urmoi", "Upendra", "Utpal", "Yadab", "Yadav", "Yash", 
        "Zitho", "Zumar", "Zhimoi"
    ]

    bodo_female_names = [
        "Aini", "Alina", "Amuli", "Anima", "Ashika", "Bini", "Bina", "Bobo", 
        "Bipasha", "Bisnu", "Binal", "Bonita", "Barmoi", "Chameli", "Chintana", 
        "Chandini", "Churni", "Chimong", "Chura", "Doli", "Dasi", "Dewmi", "Daroni", 
        "Dibrina", "Dipti", "Durga", "Gimi", "Gita", "Gungun", "Gobha", "Gini", 
        "Gauri", "Hemi", "Himai", "Hoshni", "Jangkhun", "Joti", "Jhumon", "Jiban", 
        "Kanki", "Kherai", "Kholi", "Kamli", "Kunti", "Kusal", "Lami", "Lasa", 
        "Lisi", "Limi", "Loma", "Luham", "Lota", "Libi", "Luita", "Manisa", "Mintu", 
        "Mimo", "Malai", "Meher", "Mangkhi", "Manju", "Minu", "Moni", "Mungni", 
        "Murmi", "Nidhi", "Nayan", "Nilu", "Nipa", "Namita", "Pumi", "Pina", 
        "Phuli", "Priya", "Rina", "Roli", "Rekha", "Rima", "Rupi", "Raki", "Rumi", 
        "Santia", "Shanti", "Shila", "Sushma", "Sumi", "Surai", "Subita", "Tali", 
        "Thirni", "Tinu", "Urmi", "Usha", "Vena", "Vimala", "Wona", "Wangi", 
        "Wari", "Zini"
    ]
    bodo_surnames = [
        "Adna", "Akhuli", "Arem", "Atik", "Barha", "Baruni", "Barik", "Baski", 
        "Belu", "Bhunia", "Bidyadhar", "Bindo", "Bolia", "Bonda", "Dadi", "Dhamra", 
        "Dalu", "Dandia", "Darhi", "Dhyana", "Dholia", "Dhani", "Gadhi", "Ganti", 
        "Goria", "Gudi", "Hina", "Hirata", "Holia", "Horo", "Jadum", "Jagha", "Jali", 
        "Jhara", "Kamua", "Kadiya", "Kando", "Karia", "Kanua", "Koiya", "Kundu", 
        "Kande", "Kar", "Kendi", "Kuri", "Kharika", "Khani", "Khunia", "Khede", "Lada", 
        "Lari", "Lita", "Luma", "Malia", "Madi", "Madiya", "Maru", "Mondia", "Morha", 
        "Murmu", "Matha", "Nadi", "Nani", "Nima", "Niro", "Pani", "Patra", "Pati", 
        "Pasi", "Rati", "Ramo", "Rora", "Raju", "Roda", "Sari", "Sunti", "Suni", 
        "Sita", "Tadi", "Teli", "Teliya", "Tora", "Tula", "Tara", "Wadi", "Wado", 
        "Wanu", "Wari", "Watti", "Wariha", "Walia", "Hima", "Hera", "Homa", "Kira", 
        "Kera", "Raja", "Rasu", "Sangha", "Tiki"
    ]   
    #Todo_tribal _names
    todo_male_names = [
        "Akar", "Alok", "Anand", "Arvin", "Balan", "Baran", "Bala", "Banu", "Bimal", 
        "Chandra", "Chini", "Dhruv", "Devraj", "Dinesh", "Gajan", "Gokul", "Gopal", 
        "Ganesh", "Hari", "Hemant", "Keshav", "Kiran", "Krishnan", "Kunal", "Laxman", 
        "Manoj", "Mithun", "Mohan", "Nandu", "Narayan", "Nikhil", "Rajesh", "Ramesh", 
        "Rajkumar", "Ravi", "Raghav", "Ranjan", "Ritesh", "Rajiv", "Ratan", "Samir", 
        "Sandeep", "Suraj", "Shankar", "Shyam", "Vikash", "Vinay", "Vijay", "Vikas", 
        "Yogesh", "Uday", "Vinod", "Akhil", "Chandran", "Gokhay", "Kesavan", "Lalit", 
        "Manik", "Mohit", "Rithvik", "Subash", "Tanuj", "Trinayan", "Umesh", "Aniket", 
        "Yash", "Bhaskar", "Aaryan", "Akash", "Sanjeev", "Vikram", "Mahesh", "Lakshman", 
        "Harihar", "Rajendra", "Sundar", "Suman", "Madan", "Ganapati", "Ramanan", "Arjun", 
        "Magesh", "Rishabh", "Ajeet", "Arun", "Kamaraj", "Subramanian", "Venkatesh", 
        "Bhupender", "Rameswar", "Manoj Kumar", "Vinayak", "Surendra", "Ajit", "Rajan", 
        "Arvind", "Mohanlal", "Raghuraj", "Mahendra"
    ]
    todo_female_names = [
        "Aditi", "Alka", "Amita", "Anju", "Anjali", "Anita", "Asha", "Bina", "Bhuvana", 
        "Chandra", "Charulata", "Chandini", "Darshana", "Divya", "Gita", "Gauri", "Gayatri", 
        "Hema", "Hina", "Indira", "Jyoti", "Kalyani", "Kamala", "Kamini", "Kiran", "Kusum", 
        "Lata", "Leela", "Manju", "Meera", "Meenal", "Monika", "Naina", "Nidhi", "Nupur", 
        "Pooja", "Priya", "Radhika", "Rani", "Rekha", "Rima", "Rupal", "Sadhana", "Sakshi", 
        "Shanti", "Shikha", "Shruti", "Sita", "Sunita", "Swati", "Suman", "Subha", "Tanu", 
        "Tara", "Trisha", "Uma", "Urmila", "Vandana", "Varsha", "Vidya", "Vimala", "Yashoda", 
        "Anu", "Amba", "Chitra", "Chetana", "Ganga", "Kusuma", "Lila", "Manisha", "Nandini", 
        "Nilima", "Preeti", "Ranjana", "Rupa", "Ruchi", "Sangeeta", "Sneha", "Shubha", "Sushila", 
        "Sunitha", "Sujata", "Tanuja", "Tripti", "Urmi", "Vanita", "Yamini", "Priyanka", "Sushmita", 
        "Vaidehi", "Rukmini", "Anusha", "Sarita", "Geeta", "Rajkumari"
    ]
    todo_surnames = [
        "Adiyan", "Alvan", "Ambar", "Anban", "Atman", "Azhagan", "Baidya", "Bhima", "Bhura", 
        "Chalu", "Chellam", "Chevvan", "Dhanan", "Elangai", "Elavan", "Gnanam", "Haran", "Ilam", 
        "Jagan", "Jeyaraj", "Kallai", "Kalai", "Kamaraj", "Kandhan", "Karuppa", "Kavi", "Kayan", 
        "Kumban", "Kura", "Lakshan", "Malar", "Manik", "Muthu", "Moorthy", "Nadar", "Nadana", 
        "Perumal", "Rajan", "Ramaiya", "Ramu", "Santhan", "Saravanan", "Sivaram", "Sivaraj", 
        "Sundar", "Thangamani", "Tharshan", "Thirumalai", "Thivakaran", "Thozhan", "Velu", 
        "Venkataraman", "Vidhya", "Vimalan", "Venkatesan", "Karthik", "Thanvan", "Pugalan", 
        "Raghavan", "Senthil", "Sathyamoorthy", "Selvan", "Sekar", "Ramkumar", "Thayan", "Nayan", 
        "Rathi", "Ashok", "Arul", "Avan", "Charan", "Chinnasamy", "Ezhumalai", "Gokul", "Govindan", 
        "Kannai", "Karunanidhi", "Linga", "Mani", "Niranjan", "Rajkumar", "Ramalingam", "Sankaran", 
        "Suriyan", "Vaasu", "Varadarajan", "Vidhyakumar", "Viran", "Yogan", "Akilan", "Anil", 
        "Arunachalam", "Gajendran", "Thinesh", "Vithiyan", "Rajendran", "Kannan", "Maran"
    ]
    #Koya_tribal _names
    koya_male_names = [
        "Adiv", "Ajeet", "Akshay", "Alok", "Amar", "Anil", "Ashok", "Basu", "Bhanu", 
        "Bheem", "Babu", "Dinesh", "Dalpat", "Devendra", "Dharma", "Girish", "Ganesh", 
        "Gopal", "Gokul", "Hari", "Hemanth", "Jagan", "Jitendra", "Jagdish", "Kiran", 
        "Kamal", "Kanti", "Keshav", "Kalyan", "Laxman", "Manoj", "Mukesh", "Nandu", 
        "Narayan", "Naresh", "Nikhil", "Pankaj", "Pritam", "Prakash", "Prem", "Rajesh", 
        "Ravi", "Ramesh", "Rajendra", "Rajiv", "Raghav", "Santosh", "Sudhir", "Suresh", 
        "Suraj", "Shankar", "Shyam", "Vikash", "Vinay", "Vijay", "Virender", "Yogesh", 
        "Vikas", "Yash", "Ankur", "Arjun", "Bhaskar", "Chandra", "Chintu", "Deepak", 
        "Girvan", "Hemant", "Jit", "Mangal", "Rishab", "Roshan", "Raghunath", "Samar", 
        "Shailendra", "Shubham", "Thakur", "Uday", "Vishal", "Venkatesh", "Jagat", "Kunal", 
        "Pradeep", "Kundan", "Madhav", "Ranjan", "Vayun", "Kamran", "Sanjay", "Sushil", 
        "Shikhar", "Aashish", "Satish", "Dushyant", "Manish", "Neel"
    ]
    koya_female_names = [
        "Aarti", "Amrita", "Anjali", "Anita", "Aparna", "Bindu", "Bina", "Chhaya", 
        "Charulata", "Damini", "Deepa", "Devi", "Divya", "Geeta", "Gauri", "Ganga", 
        "Hema", "Indira", "Jyoti", "Kamala", "Kamini", "Kiran", "Kusum", "Leela", 
        "Lata", "Manju", "Meera", "Minati", "Meenal", "Naina", "Nidhi", "Neelam", 
        "Nupur", "Pooja", "Priti", "Priya", "Radhika", "Rina", "Rekha", "Renuka", 
        "Rupal", "Sadhana", "Sakshi", "Shanti", "Shikha", "Shruti", "Sita", "Sunita", 
        "Surabhi", "Swati", "Swapna", "Suman", "Tanu", "Tara", "Trisha", "Uma", 
        "Urmila", "Vandana", "Varsha", "Vasudha", "Vidya", "Vimala", "Yashoda", 
        "Asha", "Anu", "Amba", "Bhuvana", "Binita", "Chitra", "Chetana", "Kalyani", 
        "Kusuma", "Lila", "Manisha", "Nandini", "Nilima", "Preeti", "Ranjana", "Rupa", 
        "Ruchi", "Sangeeta", "Sneha", "Shubha", "Sushila", "Sunitha", "Sujata", "Tanuja", 
        "Tripti", "Urmi", "Vanita", "Yamini", "Priyanka", "Sushmita", "Vaidehi", 
        "Rukmini", "Anusha"
    ]
    koya_surnames = [
        "Achari", "Adavi", "Alaka", "Anji", "Atchari", "Badi", "Barla", "Bolla", 
        "Bonthu", "Chamarti", "Chendru", "Chintak", "Chellama", "Chinta", "Dandapani", 
        "Dandu", "Dhanvadi", "Dhara", "Dosi", "Gajji", "Ganta", "Gari", "Gunda", 
        "Goli", "Jakkara", "Jamai", "Jallama", "Jani", "Joga", "Kadi", "Kakala", 
        "Kambe", "Kanthar", "Kanchan", "Konda", "Kondi", "Kothi", "Lala", "Lakshma", 
        "Linga", "Marla", "Mandla", "Masi", "Malla", "Mantha", "Meli", "Motti", "Muru", 
        "Nagavala", "Nari", "Nandhi", "Nelli", "Niran", "Nitta", "Padi", "Panta", 
        "Paturi", "Pochi", "Rami", "Raju", "Rani", "Rema", "Raja", "Rokka", "Sambi", 
        "Samma", "Sani", "Sati", "Satti", "Thakka", "Thati", "Thiru", "Tiru", "Vamshi", 
        "Vanu", "Vaddi", "Veta", "Vepa", "Vinta", "Veka", "Vodi", "Vidi", "Yella", 
        "Yadu", "Yellaiah", "Yama", "Yodh", "Zora", "Zenda", "Zori", "Bada", "Basu", 
        "Bhima", "Bhatti", "Bidri", "Bandi", "Balram", "Bhavya", "Barri", "Bandari"
    ]
    #Gond_tribal _names
    gond_male_names = [
        "Aditya", "Amar", "Anil", "Arjun", "Balaram", "Bhanu", "Chandra", "Dhanraj", 
        "Ekalavya", "Ganesh", "Gopal", "Govind", "Harish", "Ishwar", "Jagdish", "Jitendra", 
        "Kailash", "Karan", "Keshav", "Krishna", "Lakhan", "Lokesh", "Mahendra", "Manoj", 
        "Mukesh", "Nagesh", "Narayan", "Navin", "Omkar", "Padmanabh", "Paramesh", "Pradeep", 
        "Prakash", "Prem", "Raghunath", "Rajendra", "Ramakant", "Ravi", "Sachin", "Sagar", 
        "Sandeep", "Satish", "Shankar", "Shiv", "Shyam", "Somesh", "Subhash", "Sudhir", 
        "Suraj", "Tarun", "Trilok", "Uday", "Umesh", "Vasant", "Veer", "Vikram", "Vishal", 
        "Vishnu", "Yash", "Yogesh", "Ankit", "Balaji", "Chintu", "Devaraj", "Durgesh", 
        "Ganpat", "Hemant", "Indrajit", "Jaidev", "Jayanth", "Kailesh", "Kamlesh", "Kartik", 
        "Madhav", "Manish", "Mohan", "Naresh", "Narendra", "Navdeep", "Omprakash", "Prahlad", 
        "Rajesh", "Rajnath", "Ramprasad", "Ramesh", "Satyendra", "Satyam", "Shailesh", "Shridhar", 
        "Sudarshan", "Sukesh", "Suresh", "Trilochan", "Vijay", "Virendra", "Yadvendra", "Yashwant", 
        "Yogendra", "Ajay", "Arvind"
    ]
    gond_female_names = [
        "Aruni", "Baruni", "Chitkala", "Dhuni", "Esha", "Gangi", "Indraja", "Jivita", 
        "Kanaka", "Kiran", "Komali", "Leelavati", "Madhuri", "Mallika", "Megha", "Nalini", 
        "Neeraja", "Pavitra", "Rajini", "Sharini", "Ahalya", "Bhavini", "Daya", "Geeta", 
        "Indira", "Jyoti", "Kanta", "Lata", "Manjula", "Padma", "Parvati", "Radha", "Rani", 
        "Sita", "Sundari", "Uma", "Vimala", "Yashoda", "Sumitra", "Suvarna", "Bhuvi", "Chitra", 
        "Dulhami", "Ganji", "Ghanti", "Jiviya", "Kuyili", "Langri", "Mandari", "Marai", 
        "Mudila", "Namu", "Phulvati", "Rajani", "Sangini", "Savita", "Somila", "Tarini", 
        "Tungini", "Viraja", "Amba", "Ankita", "Anusuya", "Bhakti", "Chandrika", "Dayamayi", 
        "Eshwari", "Gaurika", "Harini", "Ishani", "Kamini", "Lakshmi", "Manini", "Moksha", 
        "Narmada", "Panchali", "Sarvani", "Shanvika", "Subhadra", "Tripti", "Aloka", "Bhavya", 
        "Charini", "Deepa", "Eila", "Gati", "Hamsini", "Ila", "Jvala", "Kalika", "Lali", "Manavi", 
        "Nila", "Ojaswini", "Padmavati", "Rajata", "Sohini", "Tushara", "Vasundhara", "Yamini"
    ]
    gond_surnames = [
        "Maravi", "Uike", "Dhurve", "Tekam", "Markam", "Netam", "Pawar", "Meshram", 
        "Korram", "Batti", "Siddam", "Tumram", "Wadde", "Chaudhari", "Salame", 
        "Kawle", "Madavi", "Kunjam", "Mude", "Tatte"
    ]   
    #Santhal_tribal _names
    santhal_male_names = [
        "Ajit", "Alok", "Amrit", "Anil", "Arjun", "Ashok", "Badal", "Balai", "Bandi", 
        "Bankim", "Banshidhar", "Barun", "Basant", "Bhagirath", "Bhanu", "Bikas", "Birendra", 
        "Bishnu", "Chandan", "Chandresh", "Damodar", "Dhananjay", "Dharmendra", "Dibakar", 
        "Dipankar", "Durga", "Ganesh", "Gautam", "Gopal", "Govind", "Harendra", "Hari", "Hemant", 
        "Indrajit", "Ishwar", "Jagdish", "Jiban", "Jitendra", "Kalyan", "Kamal", "Kanchan", 
        "Kedar", "Khagen", "Krishna", "Kumar", "Laxman", "Mahendra", "Manoj", "Manohar", "Mohan", 
        "Mukesh", "Naresh", "Narayan", "Narendra", "Nirmal", "Niranjan", "Omprakash", "Pankaj", 
        "Paritosh", "Prabhat", "Pradeep", "Prakash", "Prasanta", "Pratap", "Prem", "Rajendra", 
        "Rajesh", "Ramesh", "Ravi", "Sachin", "Samar", "Samir", "Sanjay", "Santosh", "Saroj", 
        "Satish", "Shankar", "Shantanu", "Sharad", "Shashi", "Shyam", "Somnath", "Srikant", 
        "Subhash", "Sudarshan", "Suman", "Sunil", "Surendra", "Suresh", "Tarun", "Trilok", "Uday", 
        "Umesh", "Utpal", "Vijay", "Vikram", "Vinay", "Vishal", "Vivek", "Yash"
    ]
    santhal_female_names = [
        "Aarti", "Alpana", "Amrita", "Anima", "Anita", "Anjali", "Aparna", "Arpita", 
        "Bani", "Basanti", "Bela", "Bimala", "Champa", "Chhaya", "Damini", "Deepa", 
        "Debashree", "Devi", "Dipa", "Durga", "Ganga", "Gauri", "Gayatri", "Geeta", 
        "Hema", "Indira", "Ishani", "Jaya", "Jyoti", "Kalyani", "Kamala", "Kanchana", 
        "Kanta", "Karuna", "Kaveri", "Kavita", "Khusi", "Komal", "Kusum", "Lakshmi", 
        "Lalita", "Leela", "Madhavi", "Madhuri", "Malati", "Mandira", "Manjula", "Maya", 
        "Meena", "Minati", "Mira", "Mithila", "Mukta", "Nalini", "Namita", "Nandini", 
        "Nayana", "Neelam", "Nilima", "Nirmala", "Padma", "Parbati", "Piyali", "Pooja", 
        "Pratima", "Priya", "Purnima", "Pushpa", "Radha", "Rajashree", "Rajni", "Rama", 
        "Ranjana", "Rekha", "Renuka", "Rina", "Ritu", "Roopa", "Ruma", "Sabita", "Sadhana", 
        "Sangita", "Sarala", "Saraswati", "Sarita", "Savitri", "Seema", "Shanti", "Sharmila", 
        "Shikha", "Shila", "Shreya", "Smita", "Sneha", "Sohini", "Sona", "Sujata", "Sunita", 
        "Suruchi", "Sushmita"
    ]
    santhal_surnames = [
        "Murmu", "Soren", "Tudu", "Hembrom", "Kisku", "Marandi", "Baskey", "Besra", 
        "Champa", "Panna", "Hansdak", "Saren", "Bedea", "Corea", "Tudu-Baski", "Majhi", 
        "Chore", "Manjhi", "Sohor", "Hasa"
    ]
    #Bhils_tribal _names
    bhils_male_names = [
        "Ajay", "Amar", "Anil", "Arjun", "Ashok", "Badri", "Baldev", "Bansi", 
        "Bhairav", "Bhanu", "Chand", "Chatur", "Dhanraj", "Dharmendra", "Dilip", 
        "Eklavya", "Ganesh", "Girdhar", "Govind", "Harish", "Hemant", "Indrajit", 
        "Ishwar", "Jagdish", "Jitendra", "Kailash", "Kalyan", "Kamlesh", "Kanha", 
        "Kantilal", "Kartik", "Khuman", "Kishan", "Krishna", "Lakhan", "Laxman", 
        "Lokesh", "Madhav", "Mahendra", "Manoj", "Matiram", "Mohan", "Mukesh", "Nagesh", 
        "Naresh", "Narayan", "Navin", "Omprakash", "Padmanabh", "Parashuram", "Prakash", 
        "Pratap", "Prem", "Raghunath", "Rajendra", "Rajesh", "Ramesh", "Ravi", "Sachin", 
        "Sagar", "Sandeep", "Satish", "Shankar", "Shyam", "Somnath", "Sukhdev", "Sukhlal", 
        "Sundar", "Suraj", "Suresh", "Tarun", "Trilok", "Tulsi", "Uday", "Umesh", "Vijay", 
        "Vikram", "Vishal", "Vishnu", "Yogesh", "Amba", "Anoop", "Banshi", "Bhairu", 
        "Bharat", "Chokha", "Dalpat", "Deva", "Durga", "Gopal", "Jatan", "Lali", "Madho", 
        "Motilal", "Naru", "Raju", "Sona", "Thakur", "Tokra", "Veer"
    ]
    bhils_female_names = [
        "Aarti", "Alka", "Anjana", "Anita", "Anjali", "Anu", "Aparna", "Arpita", 
        "Banu", "Bela", "Bhuri", "Champa", "Chhaya", "Damini", "Deepa", "Devi", 
        "Dhanni", "Ganga", "Gauri", "Gayatri", "Geeta", "Hema", "Indira", "Ishani", 
        "Jaya", "Jyoti", "Kamala", "Kanak", "Kanta", "Kaveri", "Kavita", "Kiran", 
        "Kusum", "Lalita", "Leela", "Madhuri", "Malati", "Mandira", "Manisha", "Meena", 
        "Megha", "Mukta", "Nalini", "Namita", "Nandini", "Neelam", "Padma", "Pooja", 
        "Pratima", "Priya", "Pushpa", "Radha", "Rajni", "Rani", "Rekha", "Renuka", 
        "Rina", "Roopa", "Sabita", "Sadhana", "Sangita", "Saraswati", "Sarita", "Savita", 
        "Seema", "Shanti", "Sharmila", "Shikha", "Shila", "Shobha", "Shraddha", "Sita", 
        "Smita", "Sneha", "Sohini", "Sona", "Sonam", "Sudha", "Sujata", "Sundari", 
        "Sunita", "Surbhi", "Sushila", "Swapna", "Tara", "Tripti", "Uma", "Usha", 
        "Vandana", "Vasanti", "Vidya", "Vimla", "Vinita", "Yamini", "Yashoda", "Champi", 
        "Choti", "Dharmi", "Manjula", "Tulsi"
    ]
    bhils_surnames = [
        "Ahirwar", "Alawa", "Banvasi", "Bansiya", "Baria", "Baradi", "Barve", "Bhagat",
        "Bhansali", "Bhil", "Bhoria", "Borkheda", "Chavda", "Chaurasia", "Dama", "Dangi",
        "Deewan", "Dhanvani", "Gamit", "Gharu", "Gohil", "Gajra", "Gajjar", "Gadaria", 
        "Ghuge", "Gograni", "Gond", "Goswami", "Hadi", "Halap", "Hiralal", "Hoda", "Jadav", 
        "Jadhav", "Jariwala", "Jirawala", "Kadiya", "Kambod", "Kanbi", "Karadi", "Koli", 
        "Kumbhkar", "Lala", "Lamani", "Lohana", "Lohar", "Mandloi", "Maru", "Mewada", "Moli", 
        "Morkheda", "Nadiya", "Nayak", "Padhar", "Patil", "Prajapati", "Rajgarhia", "Rajput", 
        "Rana", "Rawal", "Sadar", "Saharia", "Saini", "Sanadiya", "Sandaliya", "Sindhi", 
        "Solanki", "Soni", "Thakur", "Thokan", "Thuniyal", "Tiwari", "Vankhede", "Vaishya", 
        "Vahora", "Vadhela", "Vankar", "Varma", "Yadav", "Kirodimal", "Koli", "Kolhi", "Bhawsar", 
        "Patwari", "Sarvani", "Poonia", "Purohit", "Suthar", "Vasa", "Chauhan", "Bhamra", "Dadia", 
        "Sawant", "Chaturvedi", "Vadgama", "Raval", "Jamal", "Rathi"
    ]
    #Munda_tribal _names
    munda_male_names = [
        "Ajay", "Amar", "Anil", "Arjun", "Ashok", "Badal", "Balram", "Banshi", "Bhairav",
        "Bhanu", "Chand", "Chandan", "Damodar", "Dhanesh", "Dharmu", "Dilip", "Eklavya", "Ganesh",
        "Gopal", "Govind", "Harendra", "Harish", "Hemant", "Indrajit", "Ishwar", "Jagdish", "Jagat",
        "Jitendra", "Kailash", "Kamlesh", "Kanhai", "Kartik", "Keshav", "Khudiram", "Krishna", 
        "Laxman", "Lokesh", "Madhav", "Mahendra", "Manoj", "Mohan", "Mukesh", "Naresh", "Narayan", 
        "Navin", "Omprakash", "Padmanabh", "Paritosh", "Prabhat", "Pradeep", "Prakash", "Pratap", 
        "Prem", "Raghunath", "Rajendra", "Rajesh", "Ramesh", "Ravi", "Sachin", "Sagar", "Sandeep", 
        "Satish", "Shankar", "Shyam", "Somesh", "Subhash", "Sudarshan", "Suman", "Suresh", "Surendra", 
        "Tarun", "Trilok", "Uday", "Umesh", "Vasant", "Veeru", "Vikram", "Vishal", "Vishnu", "Yashwant", 
        "Yogesh", "Amba", "Anoop", "Birsu", "Chotu", "Dalpat", "Dayaram", "Devram", "Eshwar", "Girdhar", 
        "Jatan", "Lalram", "Madho", "Mangal", "Nandu", "Pawan", "Raju", "Sattu", "Tokra", "Veer"
    ]
    munda_female_names = [
        "Aarti", "Alka", "Amba", "Amita", "Anjali", "Anita", "Aparna", "Arpita", "Bani", "Bela", 
        "Bhuri", "Champa", "Chhaya", "Damini", "Deepa", "Devi", "Dhanni", "Ganga", "Gauri", "Gayatri", 
        "Geeta", "Hema", "Indira", "Ishani", "Jaya", "Jyoti", "Kalyani", "Kamala", "Kanak", "Kanta", 
        "Karuna", "Kavita", "Khusi", "Kiran", "Kusum", "Lalita", "Leela", "Madhavi", "Malati", "Mandira", 
        "Manjula", "Maya", "Meena", "Minati", "Mira", "Mukta", "Nalini", "Namita", "Nandini", "Neelam", 
        "Padma", "Pooja", "Prabha", "Pratima", "Premvati", "Priya", "Pushpa", "Radha", "Rajni", "Rama", 
        "Rekha", "Renuka", "Rina", "Roopa", "Ruma", "Sabita", "Sadhana", "Sangita", "Sarita", "Savita", 
        "Seema", "Shanti", "Sharmila", "Shikha", "Shila", "Shobha", "Shraddha", "Sita", "Smita", "Sneha", 
        "Sohini", "Sujata", "Sundari", "Sunita", "Sushila", "Swapna", "Tara", "Tripti", "Uma", "Usha", 
        "Vandana", "Vasanti", "Vidya", "Vimla", "Vinita", "Yamini", "Yashoda", "Champi", "Choti", "Tulsi"
    ]
    munda_surnames = [
        "Bedia", "Binda", "Hembrom", "Kindo", "Kujur", "Tudu", "Soren", "Murmu", "Minz", "Lakra", 
        "Khalkho", "Bhagat", "Barla", "Toppo", "Kerketta", "Marandi", "Kisku", "Gagrai", "Lakra", 
        "Manjhi", "Manki", "Rora", "Horo", "Hembrom", "Digra", "Majhi", "Bhatra", "Mundu", "Lamba", 
        "Kispotta", "Rajak", "Bhagat", "Minz", "Hansda", "Giddu", "Bhagat", "Giri", "Sohra", "Murmu", 
        "Rengma", "Tana", "Nag", "Sardar", "Kachhap", "Pahan", "Oram", "Ekka", "Bishi", "Gonthi", 
        "Nagesh", "Tirkey", "Bara", "Pansari", "Bhokta", "Jila", "Matri", "Chirkiri", "Dhan", "Toppo", 
        "Gossai", "Dom", "Jagga", "Hansda", "Lakro", "Munda", "Kumar", "Hori", "Hira", "Sanko", "Mardini", 
        "Pariat", "Hembom", "Bhatta", "Murmu", "Mundi", "Dhurwa", "Chandra", "Mahato", "Budi", "Bhagat", 
        "Kisku", "Gohil", "Raje", "Chand", "Khiladi", "Damor", "Bhenga", "Mangal", "Akhri", "Mishra", "Barla", 
        "Koska", "Khurri", "Rika", "Majhi", "Chhatar", "Lakra", "Kudra", "Ekka", "Lari"
    ]
    #Khasi_tribal _names
    khasi_male_names = [
        "Ading", "Aibor", "Amarlal", "Bansen", "Bante", "Bareng", "Bensheng", "Bokep", "Borsing", 
        "Borshen", "Cheni", "Chingkhat", "Chitlang", "Chureng", "Darnum", "Darme", "Dimpi", "Dorbin", 
        "Dorli", "Dorbar", "Dorsing", "Durbin", "Eldor", "Elkes", "Endro", "Erlang", "Gashan", "Gento", 
        "Haming", "Honseng", "Hopseng", "Iewtang", "Iengkong", "Ingrem", "Jambor", "Jala", "Jinthar", 
        "Jyntah", "Kaichang", "Karam", "Keishing", "Khyriem", "Khristang", "Kharjar", "Khuslang", "Kynjing", 
        "Langdoh", "Laitlang", "Lasa", "Lason", "Latja", "Lian", "Lying", "Masiang", "Mawphlang", "Mica", 
        "Monkam", "Muanpui", "Nabil", "Nengsynd", "Niang", "Ngat", "Norong", "Nongtraw", "Nongthlong", 
        "Phut", "Pynskhem", "Pyrkhat", "Pyngrope", "Pynsnem", "Ranjit", "Ristang", "Rangkynshi", "Rangthang", 
        "Reikman", "Rengto", "Rojak", "Rynjah", "Samla", "Sangma", "Sangramsing", "Saphong", "Satiang", 
        "Sdip", "Sing", "Singhania", "Singtim", "Syntung", "Talang", "Thangkhiew", "Tharoe", "Thawai", 
        "Thokre", "Thokmai", "Thyrniang", "Ujoth", "Ulang", "Unim", "Usor", "Wangshem"
    ]
    khasi_female_names = [
        "Aibon", "Ailer", "Alanna", "Amkri", "Ansika", "Ara", "Balu", "Barlin", "Bemali", "Biah", 
        "Bilai", "Bina", "Bishka", "Chemi", "Chitka", "Chyngka", "Dorina", "Dorshan", "Deni", "Dia", 
        "Diem", "Duwa", "Eldrina", "Elina", "Emang", "Erna", "Gana", "Gengri", "Giyang", "Hansi", 
        "Hira", "Hongsia", "Ingmar", "Istar", "Jebhira", "Jyntia", "Kamblang", "Kauli", "Khali", 
        "Kholie", "Khamlang", "Khyriem", "Kyntang", "Laishri", "Laiti", "Lajri", "Latiang", "Langhning", 
        "Lante", "Leichong", "Lila", "Mamon", "Mawryngkew", "Meham", "Merina", "Muthi", "Naba", 
        "Namara", "Nari", "Nao", "Ndarang", "Nongni", "Nongskhem", "Phetme", "Pynshop", "Pyndeh", 
        "Radhika", "Raibha", "Rani", "Ranjana", "Raksana", "Rewa", "Rwiang", "Sadan", "Sangma", 
        "Sarita", "Shali", "Shylla", "Syngkha", "Talina", "Tangwai", "Terpili", "Thangrai", "Thymmai", 
        "Thynba", "Tiran", "Tiam", "Tomsang", "Uma", "Usha", "Vibha", "Viu", "Wanshi", "Wansyngkham", 
        "Wahba", "Wai", "Warami", "Wenglong", "Wersing", "Wyernglang"
    ]
    khasi_surnames = [
        "Ading", "Blah", "Bindo", "Dkhar", "Hadem", "Hynñiewta", "Kharkongor", "Kharshiing", 
        "Kyiang", "Lyngdoh", "Mawlong", "Momin", "Nongbri", "Nongkynrih", "Rymbai", "Syiem", 
        "Syiemlieh", "Tynsong", "Wankhar", "Wahlang", "Warjri", "Wahlang", "Pde", "Pariat", 
        "Myrboh", "Mawphlang", "Mawsem", "Marbaniang", "Laitphlang", "Laitnoh", "Suting", "Shadap", 
        "Suwal", "Kyndiah", "Lyngdoh", "Mawkhlien", "Mawphlang", "Mynsong", "Mawrie", "Khongmen", 
        "Khongsit", "Khongchab", "Mowtung", "Suh", "Phawa", "Tyiap", "Wahngar", "Tysim", "Rymbai", 
        "Nongkrem", "Kharbuli", "Pynsong", "Kharshiing", "Mawkhar", "Rymmei", "Marbaniang", "Pde", 
        "Kharche", "Hlemlang", "Shnong", "Wanswot", "Iawbiang", "Kharkei", "Hynñiewneng", "Kynjoh", 
        "Iawlang", "Hano", "Mohrang", "Mawlong", "Laloo", "Laliang", "Chyrmang", "Nonglat", "Pidiang", 
        "Wahlieh", "Shun", "Hyrno", "Wensy", "Purbah", "Wahlang", "Nyngkong", "Mawthoh", "Sumer", 
        "Tiso", "Rabha", "Aids", "Bihari", "Tynsong", "Harian", "Kihim", "Wanshorm", "Phyngshang", 
        "Buirong", "Mawnar", "Kynsem", "Neng", "Myrboh", "Kynjoh", "Mawlai", "Latang"
    ]
    #Naga_tribal _names
    naga_male_names = [
        "Abo", "Akho", "Alu", "Anga", "Angh", "Ato", "Baishun", "Bai", "Bang", "Bano", "Banshan", 
        "Baokh", "Bembem", "Chingmai", "Chinglung", "Chitu", "Chinghao", "Chongkho", "Dazhi", "Daho", 
        "Delong", "Gasing", "Gokh", "Gada", "Gaikh", "Gimon", "Haiba", "Haokho", "Hekho", "Heka", "Herhu", 
        "Imlang", "Iro", "Inru", "Jato", "Jambung", "Jamir", "Jethro", "Kasa", "Khao", "Khamung", "Khema", 
        "Kimo", "Khaia", "Kongkum", "Konyak", "Kotho", "Lhota", "Liba", "Likhom", "Luko", "Lichung", 
        "Longsuh", "Lungshim", "Makem", "Mareng", "Mangram", "Mothang", "Mhet", "Mungmong", "Mongze", 
        "Neipang", "Nono", "Neng", "Noku", "Nokha", "Nyem", "Orem", "Phai", "Phrang", "Phiang", "Pohu", 
        "Rungka", "Rengti", "Rhetang", "Ritho", "Seve", "Sezing", "Sinat", "Sakhong", "Semshi", "Seki", 
        "Tasha", "Tekho", "Thungho", "Thotso", "Thungjem", "Tongrei", "Tokho", "Tsang", "Umang", "Unzo", 
        "Vichu", "Vong", "Wemben", "Wongtu", "Wekhro", "Zhoho", "Zhimomi", "Zholie"
    ]
    naga_female_names = [
        "Abiu", "Aji", "Akhu", "Akini", "Alima", "Alung", "Amulu", "Angni", "Angmo", "Ao", "Bakhen", 
        "Baiho", "Basu", "Banu", "Bechamo", "Belen", "Bera", "Bilai", "Chamhu", "Changli", "Changnuk", 
        "Chato", "Chingki", "Chongli", "Dene", "Demo", "Dinesh", "Duho", "Emong", "Enu", "Estina", "Fakho", 
        "Fikir", "Gani", "Gele", "Gomi", "Hamon", "Hapta", "Hekho", "Henrietta", "Heni", "Honhe", "Ibo", 
        "Iza", "Izo", "Jemi", "Jemkhum", "Jena", "Jenti", "Jukhu", "Kachi", "Kaiyo", "Kheno", "Kheme", 
        "Khang", "Khonu", "Lako", "Lania", "Lachi", "Lendshe", "Lenyang", "Leva", "Lipa", "Lila", "Limo", 
        "Lingi", "Lomo", "Liana", "Mapei", "Makumi", "Merli", "Mongmong", "Mukhu", "Muli", "Moina", "Neju", 
        "Nomi", "Ningho", "Nyamo", "Penlo", "Phoi", "Pranli", "Rukmi", "Renu", "Rani", "Rinali", "Samho", 
        "Singri", "Singhi", "Sitli", "Sumi", "Taki", "Teji", "Tohmi", "Zili", "Zeling", "Zhahto", "Zhemi", 
        "Zindoh", "Zutho"
    ]
    naga_surnames = [
        "Angami", "Ao", "Chakhesang", "Changkikong", "Chang", "Chishi", "Dzüvü", "Hoshi", "Imsong", "Kikon",
        "Khamo", "Konyak", "Konyak", "Lhouvum", "Lotha", "Longkumer", "Longkumer", "Makhrei", "Malu", "Mema",
        "Meru", "Mihu", "Motsu", "Mungro", "Nagi", "Naga", "Nienu", "Niumai", "Ngullie", "Nyekho", "Pongen",
        "Pomi", "Rangtok", "Rengma", "Rony", "Sema", "Sangtam", "Sathu", "Sema", "Som", "Tangkhul", "Tangkhul",
        "Tikhir", "Tili", "Tolu", "Vatung", "Yimchungru", "Yaden", "Yangme", "Zeliang", "Zhimo", "Zatnu",
        "Zhimomi", "Kipgen", "Hram", "Fiu", "Wati", "Tungdim", "Ahoto", "Yimkhiung", "Munglong", "Thinu",
        "Wathu", "Dumi", "Rengma", "Kori", "Nyathong", "Tshung", "Anai", "Vathen", "Khathoi", "Monung", "Hriye",
        "Sing", "Sano", "Kitovi", "Miki", "Mhong", "Changki", "Zevi", "Lomi", "Salomi", "Munli", "Netse", "Tali",
        "Richa", "Hothon", "Tsiang", "Yimkhiung", "Suman", "Temjen", "Mero", "Yata", "Dingkho", "Jang", "Khonsha",
        "Kiyang", "Yang", "Kezang", "Kalang"
    ]

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names for all tribes with surname matching
    def generate_names(tribal_male_names, tribal_female_names, tribal_surnames):
        for i in range(n // 2):  # Generate half male and half female names
            # Male Name Generation
            first_name_male = random.choice(tribal_male_names)
            last_name_male = random.choice(tribal_surnames)
            name_male = first_name_male + " " + last_name_male  # Full name

            # Female Name Generation
            first_name_female = random.choice(tribal_female_names)
            last_name_female = random.choice(tribal_surnames)
            name_female = first_name_female + " " + last_name_female  # Full name

            # Append names with gender information
            names.append((name_male, "Male"))
            names.append((name_female, "Female"))

    # Apply this function to each tribe
    generate_names(bodo_male_names, bodo_female_names, bodo_surnames)
    generate_names(todo_male_names, todo_female_names, todo_surnames)
    generate_names(koya_male_names, koya_female_names, koya_surnames)
    generate_names(gond_male_names, gond_female_names, gond_surnames)
    generate_names(santhal_male_names, santhal_female_names, santhal_surnames)
    generate_names(bhils_male_names, bhils_female_names, bhils_surnames)
    generate_names(munda_male_names, munda_female_names, munda_surnames)
    generate_names(khasi_male_names, khasi_female_names, khasi_surnames)
    generate_names(naga_male_names, naga_female_names, naga_surnames)

    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_tribal_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df