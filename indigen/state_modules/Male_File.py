import random
import pandas as pd  # Ensure you have pandas installed
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
# The init function that sets user preferences
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

def generate_male_names(n, user_preference):
    # Define suffixes and their specific prefixes
    suffix_to_prefixes = {"vihāri": [
            "Rām", "Krisn", "Mukut", "Rās", "Rasik", "Brij", "Syam", "Awadh", 
            "Atal", "Kunj", "Vipin", "Anand", "Banke", "Mukund", "Lāl", 
            "Vaikunth", "Gagan", "Golok"],
      
            "shyam" : ["Sundar", "Lal", "Vihari", "Shankar", "Narayan", "Manohar"],
    "govinda" : ["Ballabh", "Prasad", "Chand", "Ram", "Natha", "Narayan"],
     "shankara" : ["Dev", "Lal", "Datt", "Sharan", "Prasad", "Singh", "Narayan", "Das", "Dayal", "Anand"],
    "keshava" : ["Ananda", "Datta", "Deva"],
    
    "Hari" : ["Mohan", "Ballabh", "Narayan",  "Chandra", "Indra","Datt", "Kirti", "Charan", 
             "Sharan", "Bhajan", "Govind"],
    "vihara" : ["Ram", "Krisn", "Mukut", "Ras", "Rasik", "Brij", "Syam", "Awadh", "Atal", "Kunj", "Vipin", "Anand", "Banke", "Mukund", "Lal", "Vaikunth",           "Gagan", "Golok"],

    "dayal" : ["Ram", "Deen", "Shiv", "Bhagwat", "Prabhu", "Har", "Shankar", "Gur", "Rameshwar", "Raghuvar"],

    "kant" : ["Rama", "Uma", "Vişnu", "Krishn", "Shri", "Ravi", "Shiv", "Shruti", "Shashi Nishi", "Chandra", "Rajani", "Laxmi", "Surya", "Nidhi", "Dev", "Kamala",   "Sudhi", "Padm", "Nalini", "Dharani", "Manohar"],

    "charan" : ["Shiv", "Ram", "Durga", "Kali", "Devi", "Radha", "Hari", "Syama", "Ambika", "Kalika", "Uma", "Bhagawati"],

    "sharan" : ["Hari", "Ram", "Shiv", "Raghuveer", "Shambhu", "Saraswati", "Ganga", "Maithili"],

    "pal" : ["Ram", "Shiv", "Raj", "Mahendra", "Som", "Satya", "Richh", "Netra", "Ajay", "Tej", "Sukh", "Dharam", "Jay", "Yash", "Shri", "Ved", "Karan"],

    "nath" : ["Onkar", "Ram", "Som", "Kashi", "Vishva", "Jagat", "Jas", "Hari", "RudraKrishna", "Devendra", "Govind", "Jay", "Mahendra", "Narendra", "Kehari", "Gorakh", "Chhabi", "Pran", "Shambhu", "Keshari", "badri", "Kedar", "Pushkar", "Gopi", "Deena", "Bhola", "Triloki", "Uma", "Niranjan", "Janaki", "Maheshvar", "Prem", "Raj", "Shri", "Gokul", "Dvarika", "Amar", "Raghu", "Indra", "Prithvi", "Manmath", "Narendra", "Kailash", "Jitendra", "Gauri", "Rati", "Dharmendra"],

    "pati" : ["Rama", "Uma", "Radha", "Laxmi", "Shri", "Kamala", "Padma", "Rati", "Tara", "Raghu", "Kailas", "Ratan", "Vidya", "Kula", "Sīta", "Pashu"],

    "ballabh" : ["Radha", "Shri", "Kanti", "Kirti", "Vasant", "Jay", "Brij", "Nanda", "Hari", "Netri", "Prem", "Kul", "Hira", "Buddhi", "Anand", "Govind", "Vişnu", "Gopi", "Janaki", "Uma", "Laxmi", "Rama", "Vidya", "Ganga", "Shruti"],

    "svarup" : ["Ram", "Vishnu", "Dharam", "Shiv Har", "Dev", "BhagvanMadan", "Satya", "Mukund", "Vishva"],

    "datt" : ["Ram", "Rudra", "Krishn", "Hari", "Chandra", "Charu", "Shankar", "Bhairav", "Padma", "Durga", "Devi", "Dev", "Laxmi", "Kedar", "Badri", "Visnu", "Ganga", "Yamuna", "Narayan", "Prayag", "Mathura", "Indr", "Jay", "Shri", "Ambika", "Amba", "Dharam", "Gopal", "Bala", "Bhola", "Ishwari", "Keshav", "Gusain", "Manoj"],

    "nandan" : ["Maruti", "Devaki", "Shyam", "Shiv", "Yoshoda", "Dev", "Kul", "Raghu"],

    "ananda" : ["Krişņa", "Shiva", "Rama", "Nitya", "Brahma", "Daya", "HridayaBhava", "Sada", "Jaya", "Viveka", "Kula", "Vishveshvara", "Mahesha", "Parama", "Raghava", "Kewala", "Achyuta", "Deva", "Akhila", "Guna", "Vasava", "Dharma", "Jiva", "Ghana", "Purņa", "Sampurņa", "Sachchid", "Shridhara", "Parameshvara", "Nigama", "Keshava", "asha", "Bhaskara", "Satchida"],

    "mani" : ["Kul", "Din", "Chandra", "Ratn", "Hira", "Lal", "Chuda", "Veer", "Indr", "Chinta", "Raj", "Lok", "Neel", "Pushkar", "Paras", "Nag"],

    "dhar" : ["Shri", "Leela", "Murali", "Chandra", "Chakra", "Laxmi", "Rewa", "JațaGada", "Shashi", "Dharini", "Vanshi", "Ganga", "Yasho", "Giri", "Mahi", "Vidya"],

    "prakash" : ["Ram", "Shiv", "Ravi", "Chandra", "Hari", "Brahma", "Sürya"],

    "veer" : ["Raghu", "Bal", "Dharam", "Yajan", "Karam", "Achintya", "Ran", "Kul"],

    "prasad" : ["Ram", "Shiv", "Har", "Durga", "Devi", "jwala", "Shanti", "Kanti", "Chandi", "Ganga", "Jamună", "Ambika", "Jagadambika", "Sharada", "Ayodhya", "Mathura", "Gaya", "Bhagwati", "Jitendra", "Maithili"],
    
    "akar" : ["Diva", "Sudha", "Chandra", "Prabha", "Kusuma", "Ratna", "Guna"],

    "vrat" : ["Satya", "Priya", "Deva"],

    "kar" : ["Diva", "Sudha", "Bhas", "Din", "Madhu", "Karuna"],

    "mitra" : ["Agni", "Vasu", "Pranay", "Vishva"],

    "shekhar" : ["Chandra", "Vidhu", "Shiv", "Indu", "Som", "Kul"],

    "bhushan" : ["Kul", "Vidhu", "Chandra", "Shashi", "Naga"],

    "das" : ["Ram", "Shiv", "Durga", "Devi", "Garib", "Chandi", "Tulsi", "Dharam", "Charan", "Kumar", "Mohan", "Banarasi", "Mathura", "Gur", "Mahi", "Hari"],

    "deen" : ["Bhagwan", "Mata", "Ram", "Shiv"],

    "kishor" : ["Ram", "Nand", "Brij", "Jugal", "Giriraj", "Raj", "Syam", "Hari", "Shri", "Kaushal"],

    "ambar" : ["Peeta", "Neela", "Dig"],

    "raj" : ["Dev", "Desh", "Bal", "Hem", "Lekh", "Dhan", "Tilak", "Shiv", "Hans", "Mool"],

    "bhanu" : ["Chandra", "Suraj", "Briş"],

    "nidhi" : ["Gun", "Sudha", "Shri", "Prem", "Karuna"],

    "lal" : ["Ram", "Shiv", "Amrit", "Girdhari", "Krishan", "Shyam", "Mohan", "Madan", "Sohan", "Govardhan", "Vihari", "Murari", "Kishori", "Rasik", "Banwari", "Muphat", "Maņik", "Munna", "Bahori", "Moti", "Hira", "Ratan", "Brij", "Mewa", "Misri", "Hori", "Dori"],

    "amshu" : ["Sheeta", "Sudha", "Shubhra", "Hima"],

    "Ranjan": ["Rajeev", "Som", "Sheetanshu", "Ritu", "Chitta", "Rama", "Sharada", "Sudhanshu", "Vidhu", "Rajesh", "Rati", "Shruti"],

    "ram" : ["Shiva", "Hari", "Jay", "Tulsi", "Tuka", "Tīka", "Tulá", "Nand", "Moti", "Maya", "Mani", "Sīta", "Dhani", "vem", "Hansa", "Raja", "Data", "Bhaiyya", "Kali", "Manasa"],

    "kumar" : ["Shiv", "Ram", "Krisn", "Asvini", "Shravan", "Raj", "Maharaj", "Ravi", "Viranchi", "Shashi", "Anjani", "Manoj", "Hemant", "Vasant", "Suniti", "Prem", "Vijay", "Kaushal"],

    "krishna" : ["Ram", "Bal", "Hari", "Radha", "Shri", "Jay", "Gopal", "Lal", "Maharaj", "Kewal", "Venkata", "Apurv", "Anand"],

    "gopal" : ["Ram", "Madan", "Venu", "Krisna", "Hari"],

    "shankar" : ["Shiv", "Ram", "Laxmi", "Mool", "Gauri", "Durga", "Uma", "Ravi", "Uday", "Daya", "Ratn", "Kripa", "Jay", "Hari", "Prem", "Bhawani", "Rama", "Jata", "Bhola", "Girija", "Devi", "Vijay", "Abhay", "Anand", "Vişnu", "Bhim"],

    "narayan" : ["Ram", "Shiv", "Hari", "Vibhuti", "Shyam", "Shankar", "Vishva", "Vikram", "Satya", "Surya", "Anant", "Kesari", "Brij", "Jagat", "Madan", "Jay", "Trilok", "Uday", "Udit", "Veerendra", "Yagya", "Sarvagya", "Vineet", "Yogendra", "Surendra"],

    "mohan" : ["Madan", "Yogendra", "Ram", "Chandra", "Narendra", "Krisn", "Vidhu", "Hari", "Radhe", "Vişnu", "Man", "Brij", "Jag", "Vishva"],

    "raman" : ["Radha", "Tulsi", "Devaki", "Janaki", "Rama", "Rewati"],

    "isha" : ["Pushpa", "Roopa", "Dina", "Rama", "Sura", "Deva", "Hari", "Brija", "Kamala", "Bhupa", "Nara", "Rajani", "Raja", "Maha", "Ratna", "Naga", "Gaņa", "Mithila", "Awadha", "Gopa", "Dina", "Hita", "Loka", "Uma", "Neela", "Akhila", "Yoga", "Durga", "Deepa", "Chandra", "Bhava", "Raka", "Bhuvana", "Taraka", "Nikhila", "Vag"],

    "indra" : ["Deva", "Sura", "Dharma", "Veera", "Satya", "Ravi", "Nara", "Hari", "Maha", "Upa", "Raghava", "Kaushala", "Brija", "Jaya", "Shaila", "Jita", "Veera", "Bhupa", "Gyana", "Raja", "Gaja", "Naga", "Manava", "Pushpa"],

    "deva" : ["Ram", "Shiv", "Krisn", "Hari", "Har", "Vijaya", "Jay", "Nar", "Shankar", "Mohan", "Bhim", "Arjun", "Harsh", "Shyam", "Vam", "Brahm", "Gur", "Satya", "Narendra", "Bhu", "Shri", "Sukh", "Hars", "Shuk"],

    "shiva" : ["Sada", "Samba", "Parama"],

    "ishvara" : ["Ram", "Vishva", "Yagya", "Chandra", "Muni", "Vag", "Raja", "Hari", "Parama", "Yoga", "Soma", "Kama", "Kamala"],

    "Chandra": ["Krisna", "Ram", "Shiv", "Padm", "Laxmi", "Harish", "Hari", "Govind", "Lokesh", "Mohan", "Naween", "Madan", "Dinesh", "Ramesh", "Girish", "Gyan", "Hem", "Sharat", "Subhash", "Jagdish", "Pooran", "Jay", "Jiwan", "Shri", "Satish", "Indr", "Lal", "Moti", "Vidhi", "Deep", "Som", "Charu"],

    "indu" : ["Shiva", "Mukula", "Nava", "Poorna", "Shubha", "Bala", "Vimala", "Bharata"]
                          }
    
    
    #Preffix to Suffix
    prefix_to_suffixes = {
        "Vishnu": ["Datt", "Kant", "Mitra", "Shankar", "Vardhan", "Pad", "Sarup"],
        "Hari":["Haran","Vamsh"],
        "Raghu" : ["Nath", "Pati", "Veer", "Nandan", "Raj", "Var"],
    "Shiva" : ["Kumar", "Datt", "Anand", "Charan", "Sharan", "Shekhar", "Kant", "Sundar", 
            "Dev", "Narayan", "Prasad", "Ram", "Nandan", "Nath", "Pujan", "Raj", "Mangal", 
            "Jeevan", "Deen", "Balak", "Chand", "Singh", "Lal"],
    "Rudra" : ["Datt", "Dev", "Mani", "Nath"],
    "Indra" : ["Datt", "Mani", "Chandra", "Dev", "Jeet", "Mohan", "Kumar", "Nath", "Prakash"],
    "Deva" : ["Datt", "Vrat", "Poojan", "Nandan", "Ashish", "Indra (Devendra)"],
    "Bhagwan" : ["Deen", "Dass", "Duit", "Sarup", "Ballabh", "Singh"],
    "Shri" : ["Dhar", "Prakash", "Chand", "Kant", "Ram", "Pati", "Pal", "Nath", "Vats", "Gopal"],
    "Durga" : ["Datt", "Prasad", "Charan", "Sharan", "Das", "Lal", "Ish", "Shankar"],
    "Bhawani" : ["Datt", "Lal", "Singh", "Prasad", "Shankar"],
    "Bhagwati" : ["Prasad", "Charan", "Sharan"],
    "Lakshmi" : ["Kant", "Shankar", "Narayan", "Dhar", "Chand", "Datt"],
        "Saraswati" : ["Sharan", "Prasad", "Kumar"],

    "Rama" : ["Pati", "Kant", "Nath", "Ish", "Ranjan", "Shankar", "Raman"],

    "Revati" : ["Raman", "Nandan", "Prasad"],

    "Shri" : ["Pad", "Pal", "Chand", "Niwas", "Dhar", "Kant", "Vats", "Nath"],

    "Uma" : ["Pati", "Shankar", "Kant", "Nath", "Ish ", "Charan", "Maheshwar", 
             "Prasann", "Sharan", "Datt"],

    "Maithili" : ["Sharan", "Charan", "Prasad"],

    "Chandr" : ["Prakash", "Kant", "Shekhar", "Mauli", "Mohan", "Datt", "Mani", "Bhushan", 
                "Ballabh", "Dhar"],

    "Surya" : ["Kant", "Prakash", "Narayan", "Surajbhan"],

    "Shashi" : ["Kant", "Bhushan", "Shekhar", "Dhar"],

    "Som" : ["Chand", "Datt", "Dev", "Shekhar", "Pal", "endra", 
              "Ishwar (Someshwar)", "Nath", "Ranjan"],

    "Vidhu" : ["Mohan", "Shekhar", "Bhushan", "Kant"],

    "Raj" : ["Kumar", "Dev", "Shekhar", "Mohan", "Nath", "Gopal", "eshwar", 
             "endra", "Pal", "Bahadur", "Narayan", "Veer"],

    "Satya" : ["Narayan", "Bhushan", "Vrat", "Kam", "Svarup", "Prakash", "Dev", 
               "Anand", "Indra", "Murti", "Shankar"],

    "Prem" : ["Shankar", "Nath", "Chand", "Datt", "Prakash", "Lal", 
              "Narayan", "Kumar", "Sagar", "Anand", "Singh"],

    "Roop" : ["Chand", "Narayan", "Lal", "esh"],

    "Kanti" : ["Ballabh", "Lal", "Chand", "Chandra"],

    "Dharm" : ["Chand", "Dev", "Anand", "Svaroop", "Kirti", "Pal", "Raj", 
               "Singh", "Veer", "Indra"],

    "Vishva" : ["Deep", "Mitra", "Mohan", "Roop", "Bhushan", "Prakash", "Jeet"],

    "Jaya" : ["Anand", "Ram", "Krishna", "Dev", "Chand", "Shankar", "Bhagwan", 
    "Narayan", "Prakash", "Singh", "Datt"],

    "Kul" : ["Bhushan", "Deep", "Anand", "Rajiv", "Rakesh", "Mani", "Shresth"],

    "Brij" : ["Vihari", "Bhushan", "Mohan", "Nandan", "Narayan", "Lal", 
            "Indra", "Ballabh", "Ish "],

    "Veni" : ["Prasad", "Madhav", "Shankar", "Ram"],

    "Jag" : ["Mohan", "Ish", "Nath", "Jeet", 
              "Jagat Ram", "Jagadeeshwar Prasad"],

    "Guru" : ["Datt", "Dev", "Swamy", "Prasad", "Charan", "Sharan", "Das"],

    "Ratna" : ["Chand", "Mani", "Lal", "Akar", "Ish"],

    "Bala" : ["Krishna", "Chandra", "Datt", "Indu", 
              "Sundara", "Subramanya", "Govind"],

    "Vimal" : ["Chand", "Prasad", "Kumar", "Indu", "Prakash", "Kanti"],

    "Gyan" : ["Dev", "Chand", "Svaroop", "Indra", "Shankar"],

    "Veda" : ["Vrat", "Prakash", "Mitra"],
    "Maha" : ["Dev", "Raj", "Anand", "Indra", "Ish", "Ishwar"],

    "Sada" : ["Anand", "Shiv", "Sukh"],

    "Upa" : ["Manyu", "Indra", "Asana"],

    "Nir" : ["Upam", "Bhay", "Ranjan"],

    "Abhi" : ["Manyu", "Shek", "Lash"],

    "Pra" : ["Gati", "Kriti", "Teeti", "Hlad", "Tyoosh", "Sann", "Shant", "Mod"],

    "Vir" : ["Kram", "Krant", "Mal", "Nod", "Shal", "Las", "Shrut"],

    "Vidya" : ["Datt", "Char", "Niwas", "Charan", "Bhushan", "Dhar", "Datt", "Niwas", "Sagar"],

    "Kishori" : ["Lal", "Das", "Raman", "Ram"],
        
    "Ram" : ["Chandra", "Kumar", "Anand", "Sharan", "Charan", "Govind", "Dev", "Narayan", "Manohar", 
    "Datt", "Prakash", "Kishor", "Mohan", "Gopal", "Prasad", "Shankar", "Ratan", "Simran", 
    "Sevak", "Svarup", "Dayal", "Anuj", "Dhari", "Deen", "Gulam", "Ashray", "agya", "Pal", 
    "Awadh", "Vilas", "Karan", "Sukh", "Lochan", "Bahadur", "Mürti", "Naresh", "Avtar", 
    "Veer", "Nagina", "Kinkar", "Lubhaya", "Rasik", "Dular", "Ashish", "Darshan", "Sundar", 
    "Lal", "Ishwar (Rameshwar)", "Nath", "Sahay", "Niwas", "Bharose", "Ranjan", "Rasik", 
    "Lakhan", "Sumir", "Bahori", "Sahodar", "Niranjan", "Lala", "Prasann", "Sammukh", 
    "Akhil", "Janam", "Rakha", "Tahal", "Sagar", "Vriksh", "Dhan", "Rakshit", "Harsh", 
    "Balak", "Roop", "Bachan", "Bhajan", "Pukar", "Chela", "Mohit", "Lubhavan", "Khilavan", 
    "Sakal", "Sakha", "Jas", "Ramaiya", "Shobhit", "Pujan", "Darash", "Nachattar", "Badan", 
    "Jharokhe", "Sahaj", "Lingam", "Tilak", "Phal", "Vinay", "Kripal", "Pyare", "Dulare", 
    "Soorat", "Ji", "Lal"],
        "Krishna" : ["Kant", "Kumar", "Dev", "Mohan", "Gopal", "Murari", "Bihari"]
    }  
    
    # Define surnames
    male_surname = [
        'Kalita', 'Thakuria', 'Bhuyan', 'Borah', 'Sarmah', 'Laskar', 'Pathak', 'Maheshwari', 
        'Gayan', 'Boro', 'Pujari', 'Bharali', 'Sikdar', 'Talukdar', 'Pradhani', 'Baroowa', 
        'Barpatra', 'Chaliha', 'Deka', 'Barman', 'Bora', 'Parashar', 'Sinha', 'Morang', 
        'Mahanta', 'Doley', 'Chakravarty', 'Bhattacharya', 'Phukan', 'Bishwas', 'Saikia', 
        'Baruah', 'Borthakur'
    ]

    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    for _ in range(n):

        name_type = random.choice(["suffix", "prefix"])
        
        if name_type == "suffix":
            # Randomly select a suffix group
            suffix = random.choice(list(suffix_to_prefixes.keys()))
            # Randomly select a prefix from the chosen suffix group
            prefix = random.choice(suffix_to_prefixes[suffix])
            # Combine prefix and suffix
            male_first = prefix + suffix.lower()

        elif name_type == "prefix":
            # Randomly select a prefix group
            prefix = random.choice(list(prefix_to_suffixes.keys()))
            # Randomly select a suffix from the chosen prefix group
            suffix = random.choice(prefix_to_suffixes[prefix])
            # Combine prefix and suffix
            male_first = prefix + suffix.lower()

        # Randomly select a surname
        male_last = random.choice(male_surname)
        
        # Combine names based on user preference
        if preferences.get('name_type') == 'first':
            name_male = male_first  # Only first name
        else:
            name_male = male_first + " " + male_last  # Full name (first + surname)
        
        # Append the generated name to the list
        names.append((name_male, "Male"))
    
    # Create a DataFrame
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Write to CSV file
    file_path = 'generated_male_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df

