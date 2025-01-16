import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
# The init function that sets user preferences
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

def generate_assam_names(n, user_preference=None, seed=None):
    # Male and Female First Names
    male_assam_firstname = ["Abhijeet", "Akashdeep", "Anirban", "Arup", "Biswajit", "Barun", "Bhaskar", "Banikanta", "Bhabesh",
    "Bidyut", "Bhupen", "Bhargav", "Bodhi", "Bhanuprasad", "Chandan", "Chitragupt", "Charan", "Chinmoy",
    "Dinesh", "Devendra", "Debojit", "Dipankar", "Dipesh", "Debasish", "Dhrubajyoti", "Dhiraj", "Durgesh",
    "Gouranga", "Gunadhar", "Gopal", "Gokul", "Gautam", "Hemanta", "Harihar", "Hiren", "Hemendra", "Harish",
    "Jagadish", "Jatin", "Joydeep", "Jhantu", "Jayanta", "Jaydev", "Jugal", "Kanak", "Kanhaiya", "Kishore",
    "Kirtan", "Krishnan", "Kunal", "Laxminarayan", "Loknath", "Laltu", "Manoj", "Manindra", 
    "Mahendra", "Maitreya", "Madhab", "Milan", "Mukul", "Neel", "Nabin", "Nirmal", "Narayan", "Nayan",
    "Partha", "Pankaj", "Pradeep", "Prakash", "Parthiban", "Pranjal", "Pritam", "Rakesh", "Ranjan",
    "Rajib", "Raghav", "Ratan", "Rudra", "Rajendra", "Rajiv", "Ratul", "Sandeep", "Suman", "Shyam", "Sankar",
    "Subhajit", "Shital", "Sourav", "Subrata", "Satyendra", "Someshwar", "Swapan", "Sanjeeb", "Tarun", "Tapan",
    "Upendra", "Umesh", "Aakash", "Aayush", "Anirvan", "Ayushman", "Ankit", "Arindam", "Biswanath", 
    "Barendra", "Bibhav", "Baskar", "Bhupendra", "Bhudev", "Bishwajit", "Chayan", "Chiranjeet", "Chirantan",
    "Chayanit", "Devashish", "Dineshwar", "Dhrubajit", "Debashree", "Dipak", "Debashis", "Dhananjay", "Durjay",
    "Gaurav", "Gobinda", "Gokulnath", "Gunaraj", "Hemen", "Hemant", "Haridas", "Harinath", "Hirish", "Hridayesh",
    "Jayaprakash", "Jayanth", "Jahangir", "Jagannath", "Jitendra", "Kamal", "Keshav", "Krishnakanta", "Keshavendra",
    "Kripananda", "Lakhinath", "Lakshman", "Lokenath", "Manabendra", "Maniram", "Manish", "Mohan", "Madhukanta",
    "Mithun", "Mukund", "Mizan", "Mritunjay", "Monoj", "Niranjan", "Nabadwip", "Nikhil", "Nakul", "Nayanesh", "Nilay",
    "Parthasarathi", "Purnanand", "Pranav", "Paritosh", "Proshanto", "Ratanjyoti", "Rajmohan", "Rajeshwar",
    "Rajwinder", "Rajkumar", "Rudrajesh", "Raghunath", "Ranju", "Raghavendra", "Rajdip", "Rajnarayan", "Sandip",
    "Subhodip", "Shovan", "Subir", "Shreyas", "Sanatan", "Sumantran", "Suraj", "Shyaminder", "Sankhadeep",
    "Shantanu", "Sudhir", "Utkal", "Aabhijit", "Aadhvay", "Aanjan", "Abhijoth", "Abhivan", "Adhiraj", "Adwitya",
    "Alesh", "Anikhil", "Arnabendra", "Arundev", "Aritraj", "Asitendra", "Ashokendra", "Astik", "Avran", "Badrinath",
    "Balaraj", "Banomali", "Banjan", "Banindra", "Bibhush", "Bijayendra", "Bikramjit", "Bideshwar", "Bishmendra",
    "Bhairabendra", "Bhavendra", "Bhupendrith", "Bhimsen", "Chhatresh", "Chitreshwar", "Charish", "Chandranil",
    "Chandraveer", "Chayanik","Dakshesh", "Dastan", "Debanand", "Debiprasad", "Dhirendra",
    "Dipendu", "Dipanjan", "Dwipen", "Dwijesh", "Durjayit", "Dhurvendra", "Gajendrajit", "Gauribhadra", "Gopalendu",
    "Gokulprakash", "Gurucharan", "Girinath", "Girishankar", "Gourinath", "Hemdev", "Hiteshranjan", "Hemparth",
    "Hiralal", "Hritikesh", "Harigopal", "Haribalan", "Hemnath", "Indrajit", "Indranil", "Jashwin", "Jagatprakash",
    "Jatinraj", "Jayeshwar", "Jhoolan", "Jnanendra", "Jashodar", "Kishmak", "Kripalendra", "Krishnachandra", "Kshithij",
    "Kunalprasad", "Lakshan", "Lokeshwar", "Laxminarayana", "Madhanesh", "Madhavendra", "Manindrajit", "Minank",
    "Mananith", "Mandarak", "Mukulendra", "Nakulprasad", "Nivash", "Nirendra", "Nitindev", "Paramananda", "Partheswar",
    "Pranadev", "Rajendrajit", "Raghvendra", "Aabir", "Aadhiresh", "Aantvik", "Aarvendra", "Abhayendra", "Abhijait",
    "Abhivrat", "Akhileshwar", "Alokendra", "Anayak", "Anandvijay", "Arijit", "Arvindranath", "Aswath",
    "Atharvendra", "Ayodhyapati", "Baidurya", "Balakumar", "Banandip", "Banmali", "Barindra", "Bimalendu", "Bhagatram",
    "Bhanuprakash", "Bhaveshwar", "Bhavikendra", "Bhishmendra", "Bhupenraj", "Chandanraj", "Charadrik",
    "Chitranjan", "Chirantanesh", "Chiranjeev", "Chittaranjan", "Chitranil", "Daksheshwar", "Damodar", "Dandeshwar",
    "Darpan", "Debajit", "Debaprasad", "Dineshwaran", "Dipankarjit", "Diptashish", "Dwarika", "Dwijendranath",
    "Durgeshwaran", "Dhanpati", "Devinderjit", "Dineshar", "Dhruvendra", "Dhimanesh", "Garvendra", "Ganeshwar",
    "Gauravendra", "Gobindaprasad", "Gokulpradip", "Gyanendra", "Girishwar", "Gourindra", "Hiral", "Hiteshwari",
    "Hirenjoy", "Harendra", "Harivansh", "Hrishikesh", "Harvendra", "Indranath", "Indresh", "Jayanthesh", "Jagannathesh",
    "Janardan", "Jugalendra", "Jitendranath", "Kanailal", "Kamaleswar", "Keshab", "Kishorlal", "Kripachandra",
    "Krithikesh", "Kshitinanda", "Kshamesh", "Kunjal", "Madhabnath", "Mahendranath", "Madhvendra", "Manikanta",
    "Manishek", "Manojh", "Madhavpran", "Mukeshwar", "Manindrajeet", "Nandishwar", "Niranjal",
    "Pranit", "Prashanth", "Pradyumna", "Pravendra", "Prakrit", "Raghvendra", "Rajendranath", "Rajkiran", "Ravindra",
    "Rishabhkumar", "Rajendrajeet", "Saidheesh", "Saraswati", "Sandeepvarma", "Sayanik", "Siddhartha", "Santanu",
    "Sukanta", "Sudhakar", "Shakti", "Shalendra", "Sahasra", "Subhansh", "Sourin", "Sreekanth", "Sumanish",
    "Tithiraj", "Tanmay", "Tejesh", "Udyan", "Ujjwal", "Vishwanath"]
    
    female_assam_firstname = ["Ananya", "Aaratrika", "Aishani", "Aloka", "Alpana", "Anamika", "Anindita", "Aparajita",
    "Arpita", "Arundhati", "Asmita", "Avantika", "Bandita", "Barnali", "Barsha", "Bijoya",
    "Bipasha", "Bithika", "Chandana", "Charulata", "Chhanda", "Chhaya", "Debjani", "Debika",
    "Deepanjali", "Deepa", "Devika", "Diya", "Dolon", "Dwipti", "Ela", "Eshita", "Gauri",
    "Haimanti", "Ila", "Indrani", "Ishani", "Jaya", "Jayati", "Jhuma", "Joya", "Kalyani",
    "Kamalika", "Karabi", "Kasturi", "Keka", "Keya", "Khushi", "Koel", "Konika", "Krishna",
    "Kusum", "Laboni", "Latika", "Leena", "Lopamudra", "Madhabi", "Madhumita", "Mahuya",
    "Malabika", "Malati", "Malini", "Mandira", "Manisha", "Manjula", "Mausumi", "Mayuri",
    "Meghna", "Meenal", "Meenakshi", "Milika", "Mithila", "Mitali", "Mohona", "Moushumi",
    "Mukta", "Nabanita", "Nandita", "Nandini", "Neepa", "Neha", "Nikita", "Nila", "Nipa",
    "Nirupama", "Nisha", "Nita", "Nivedita", "Pallabi", "Parineeta", "Paromita", "Parul",
    "Payal", "Payel", "Piyali", "Poonam", "Poulomi", "Pragya", "Prakriti", "Pramila",
    "Pranati", "Pratima", "Priya", "Priyanka", "Proma", "Puja", "Purnima", "Rachana",
    "Raima", "Rajashree", "Raka", "Rakhi", "Ranjana", "Ratna", "Rekha", "Reshmi", "Rewati",
    "Ria", "Rimi", "Rina", "Rini", "Rituparna", "Roshni", "Ruchira", "Rupali", "Sangita",
    "Sanjana", "Sarmila", "Shalini", "Shampa", "Sharmila", "Shibani", "Shikha", "Shilpa",
    "Shreya", "Shruti", "Simran", "Smita", "Sneha", "Sohini", "Soma", "Sonali", "Sujata",
    "Sukanya", "Sulagna", "Sutapa", "Tanima", "Tapati", "Tanuja", "Aadrita", "Aarohi",
    "Abha", "Achala", "Adrija", "Adrika", "Ahana", "Aishwarya", "Akriti", "Alina", "Amita",
    "Amrita", "Amruta", "Amulya", "Anindini", "Anjali", "Annapurna", "Antara",
    "Aparna", "Archana", "Arunima", "Ashmita", "Atreyi", "Ayantika", "Banashree", "Bandana",
    "Banhi", "Barnita", "Basanti", "Bela", "Bhakti", "Bhaswati", "Bhavya", "Bina", "Binita",
    "Bishakha", "Brahmi", "Chandrima", "Charvi", "Chaya", "Chhavi", "Chitralekha", "Damini",
    "Darshini", "Deeksha", "Deepshikha", "Deeti", "Dhrishti", "Dhyani", "Diksha", "Dipannita",
    "Dishari", "Drishti", "Dwipali", "Dyuti", "Ekta", "Esha", "Etasha", "Falguni", "Gargee",
    "Gitali", "Gitashree", "Gopa", "Gopika", "Grishma", "Gunjan", "Hemanti", "Hemlata",
    "Hrishita", "Ilaaka", "Ishita", "Jhanavi", "Jharna", "Jyoti", "Kabita", "Kadambini",
    "Kamini", "Kanaklata", "Kanan", "Kanishka", "Kanti", "Karishma", "Kavya", "Keerti",
    "Komal", "Kumudini", "Lajja", "Lalita", "Lata", "Madhubala", "Madhuri", "Manasi",
    "Manika", "Minati", "Mirnalini", "Mohini", "Moumita", "Mousami", "Mridula", "Namrata",
    "Nanita", "Nayantara", "Neelima", "Nilanjana", "Nilima", "Nirosha", "Nitya", "Oindrila",
    "Pallavi", "Panchami", "Paramita", "Phalguni", "Piya", "Poorna", "Prabha", "Pragyashree",
    "Prajna", "Pranali", "Prarthana", "Pratibha", "Preeti", "Priyadarshini", "Purba",
    "Rachita", "Radhika", "Ragini", "Rajani", "Rajasi", "Rakhee", "Reeti", "Renuka", "Richa",
    "Riddhi", "Rishita", "Riti", "Rohini", "Rukmini", "Rupsha", "Rupa", "Sabita", "Aditi",
    "Alaka", "Amala", "Amba", "Ambika", "Ashima", "Bhagirathi", "Bhanumati", "Bharati",
    "Bhavani", "Bijaya", "Bimala", "Damayanti", "Deepmala", "Dhanalakshmi", "Dhrubaa",
    "Dipa", "Dipali", "Doyel", "Durga", "Gita", "Hemalata", "Hira", "Indira", "Jayanti",
    "Jayashree", "Kamala", "Kashmira", "Khuku", "Kokila", "Kumkum", "Labanya", "Leela",
    "Lilavati", "Lochana", "Madhavi", "Malaya", "Mrinalini", "Nabaneeta", "Neela", "Neerja",
    "Neeta", "Nirmala", "Padmini", "Parvati", "Phoolmoni", "Premalata", "Priyambada",
    "Pushpa", "Radha", "Rajkumari", "Rita", "Ritu", "Roopa", "Sadhana", "Sandhya", "Sanjukta",
    "Saraswati", "Sarita", "Sarojini", "Saudamini", "Seema", "Shakuntala", "Shanti", "Shefali",
    "Shila", "Shobha", "Shova", "Shraddha", "Shreelata", "Shreemati", "Shreemoyee", "Shubhra",
    "Snehalata", "Sudeshna", "Sumati", "Sumitra", "Sushila", "Swapna", "Urmila", "Alpona",
    "Anima", "Annapoorna", "Anuradha", "Aparupa", "Arati", "Asharani", "Atasi", "Bhadra",
    "Bhavna", "Binapani", "Bindu", "Brinda", "Charubala", "Dipanjali", "Dipika", "Durgamoni",
    "Giribala", "Girija", "Hena", "Jagadamba", "Jyotsna", "Ketaki", "Kshama", "Lalana",
    "Madhura", "Manorama", "Manoshi", "Mukti", "Nanda", "Neeraja", "Nidhi", "Padmabati",
    "Parbati", "Shanta", "Tapasi", "Tarulata", "Tilottama", "Vaidehi", "Vandana", "Vasanti",
    "Vibha", "Vidya", "Vimala", "Vrinda", "Yamini", "Yashoda"]
    
    # Surnames common in Assam
    assam_surname = ['Kalita', 'Thakuria', 'Bhuyan', 'Borah', 'Sarmah', 'Laskar', 'Pathak', 'Maheshwari', 'Gayan', 'Boro',
                  'Pujari', 'Bharali', 'Sikdar', 'Talukdar', 'Pradhani', 'Baroowa', 'Barpatra', 'Chaliha', 'Deka', 'Barman',
                  'Bora', 'Parashar', 'Sinha', 'Morang', 'Mahanta', 'Doley', 'Chakravarty', 'Bhattacharya', 'Phukan',
                  'Bishwas', 'Saikia', 'Baruah', 'Borthakur', 'Boruah', 'Dihingia', 'Kataki', 'Pegu', 'Dutta', 'Mazumdar',
                  'Maharana', 'Bhattacharjee', 'Hazarika', 'Sarania', 'Sharma', 'Tamuli', 'Kakati', 'Khound', 'Nath',
                  'Goswami', 'Kumar', 'Konwar', 'Gogoi', 'Upadhyaya', 'Bhagawati', 'Saikiya', 'Barpatra Gohain', 'Choudhury',
                  'Das', 'Medhi', 'Rajkhowa', 'Khanikar', 'Bezbaruah', 'Bordoloi', 'Mishra', 'Purkayastha', 'Dasgupta', 'Barua', 'Sarma', 'Singh']

    # Initialize user preferences (default to 'full' name type if not passed)
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(male_assam_firstname)
        last_name_male = random.choice(assam_surname)
        
        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        names.append((name_male, "Male"))
    for i in range(n // 2):
        # Female Name Generation
        first_name_female = random.choice(female_assam_firstname)
        last_name_female = random.choice(assam_surname)
        
        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female  # Full name

        # Append female name with gender information
        # Append male name with gender information
        
        names.append((name_female, "Female"))

    
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Ensure file writing happens
    file_path = 'generated_assam_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')
    
    print(f"Names have been written to '{file_path}' successfully.")
    return df

