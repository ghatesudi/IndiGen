import random
import csv
import os
import pandas as pd

# Initialize preferences from user input (simulated with a function for this example)
def init(user_preference):
    # Example: user_preference could be a dict that includes:
    # 'name_type': 'full' or 'first' (to decide whether full name or first name)
    
    # We'll use this preference in the generation process
    return user_preference

# Function to generate names based on the preference set by `init`
def generate_karnataka_names(n, user_preference):
    # Karnataka Male First Names
    male_karnataka_firstname = ['Chandra', 'Vishvakarman', 'Udaykumar', 'Narayana', 'Lalith', 'Shashidar', 'Shanmukha', 'Vinayak', 'Indranath',
 'Lalit', 'Vasudevendra', 'Anandesh', 'Satish', 'Devendra', 'Jai', 'Sajjan', 'Manjunatha', 'Anand', 'Venkatraman', 'Charuvendra', 'Ganesh',
  'Dhruv', 'Anil', 'Arun', 'Anantha', 'Durga', 'Vittal', 'Siddhartha', 'Nandish', 'Maheshwar', 'Gowramma', 'Magesh', 'Kashyap', 'Vidhyadhar',
  'Sadarshan', 'Dheeraj', 'Ashwin', 'Vithal', 'Surendra', 'Jayan', 'Darshan', 'Prashanth', 'Yashwant', 'Rupendra', 'Shivendra', 'Laxminarayana',
  'Tanishq', 'Atmaram', 'Gajanand', 'Harinarayan', 'Madhav', 'Jayanth', 'Nitin', 'Rishikesh', 'Samarth', 'Vaidyanathan', 'Harvinder', 'Krishnamoorthy',
  'Umakanth', 'Vishwanath', 'Narayan', 'Balaram', 'Sanjay', 'Amar', 'Naveen', 'Rudra', 'Jayachandra', 'Raviappa', 'Balaji', 'Ketan', 'Rajashekar', 
  'Bhanuprasad', 'Surajkumar', 'Nikhil', 'Rohan', 'Vishnu', 'Venkappa', 'Eshwar', 'Hemanth', 'Chintan', 'Giridhar', 'Shivakumar', 'Bhaskar', 'Indra', 
  'Madhusree', 'Shivan', 'Yogendra', 'Aakash', 'Praveen', 'Madhusudhan', 'Kumar', 'Ashok', 'Krishna', 'Vishweshwar', 'Chandru', 'Ajit', 'Vishnuprasad', 
  'Ilan', 'Tarun', 'Siddhant', 'Lokesh', 'Tejendra', 'Vishvesh', 'Ravi Teja', 'Dineshwaran', 'Sharath', 'Onkar', 'Muktanand', 'Ponnappa', 'Raghunath', 
  'Sreenivasa', 'Vidhath', 'Krishnan', 'Kalyan', 'Tejaswin', 'Ashish', 'Ganeshwar', 'Rajan', 'Yogesh', 'Vijaykumar', 'Chinmayananda', 'Deeraj', 'Uday', 
  'Ajaya', 'Pranesh', 'Kiran', 'Lingaraj', 'Nishanth', 'Nirmal', 'Sanjeev', 'Uttam', 'Raghu', 'Pranay', 'Vishal', 'Nagendra', 'Balakrishna', 'Lohit', 
  'Shrikanth', 'Rajesh', 'Manjunath', 'Mukesh', 'Raghupati', 'Gautam', 'Raman', 'Ajay', 'Kailash', 'Jayakumar', 'Kuppuswamy', 'Kandappa', 'Srinath', 
  'Surya', 'Aditya', 'Abhaya', 'Vasudevan', 'Ishwaran', 'Sanjiv', 'Vijayraj', 'Chandreshwar', 'Jagannath', 'Pranav', 'Nataraj', 'Chandrashekhar', 'Rathi', 
  'Shankar', 'Venkatachalapathy', 'Irfan', 'Kartik', 'Mahender', 'Harsha', 'Badri', 'Kiranraj', 'Narayanesh', 'Suresh', 'Sridhar', 'Sandeep', 'Venkatesh', 
  'Dhananjay', 'Sathish', 'Renju', 'Mithilesh', 'Vishwas', 'Vishwak', 'Krupesh', 'Sarthak', 'Sudarshan', 'Pavan', 'Deepak', 'Chandan', 'Shakthi', 'Tushar', 
  'Vatsal', 'Gajanana', 'Sriram', 'Tarak', 'Dhanvantari', 'Santosh', 'Santhanam', 'Vimlesh', 'Somanna', 'Upendra', 'Muthappa', 'Gagan', 'Rameshwar', 'Vasantha', 
  'Janardhan', 'Dhanraj', 'Laxman', 'Vikram', 'Barun', 'Vivek', 'Gundappa', 'Ankur', 'Arvind', 'Milan', 'Kuttappa', 'Sudhir', 'Rudresh', 'Jatin', 'Aaditya', 
  'Vivekanand', 'Chandrashekar', 'Raghuram', 'Jayakrishna', 'Niranjan', 'Devesh', 'Rameshchandra', 'Vijayanand', 'Harish', 'Kailas', 'Sujay', 'Pankaj', 'Karan', 
  'Chandrakant', 'Vishwajit', 'Shravan', 'Krishnananda', 'Lakshmanan', 'Chiranjeevi', 'Shashank', 'Dinesh', 'Rajvinder', 'Ganapati', 'Rajeev', 'Sureshchandra', 
  'Veerendra', 'Govind', 'Narayanappa', 'Vishwajeet', 'Goutham', 'Vamsi', 'Vinay', 'Chinmay', 'Anshuman', 'Mohit', 'Gopalakrishna', 'Mithun', 'Bhavesh', 'Prithvi',
   'Kartikeya', 'Vimal', 'Raghuveer', 'Rama', 'Ramachandra', 'Nandakumar', 'Sudhakar', 'Bhaskarappa', 'Nagaraj', 'Binaayak', 'Chetan', 'Avinash', 'Deekshit', 
   'Shubham', 'Anirudh', 'Raghavendra', 'Charan', 'Jitendra', 'Sushant', 'Gajendra', 'Narayanswamy', 'Sharad', 'Jayanthan', 'Sailesh', 'Ranganath', 'Rishi', 
   'Shivappa', 'Siddhanth', 'Dhanesh', 'Mahadev', 'Manju', 'Puranjay', 'Ujjwal', 'Harihar', 'Omprakash', 'Nakul', 'Sankalp', 'Yashwanth', 'Srinivas', 'Ratan', 
   'Mark', 'Narendra', 'Adish', 'Vasant', 'Ganeshappa', 'Ranjith', 'Madhavan', 'Shivani', 'Kanchan', 'Kapil', 'Karthikeya', 'Subramaniam', 'Prakashchandra', 
   'Madhusudan', 'Ritesh', 'Nitesh', 'Vikrant', 'Kunal', 'Satyam', 'Chidambar', 'Sashwat', 'Girish', 'Jayaprakash', 'Jagat', 'Lakshman', 'Omkar', 'Keshav', 
   'Rakesh', 'Vikramaditya', 'Kakshith', 'Devaprasad', 'Ramdas', 'Achyuta', 'Anuj', 'Sivaprasad', 'Mitesh', 'Shivansh', 'Karthik', 'Brahman', 'Raj', 'Sharan', 
   'Pradeep', 'Divakar', 'Manikanta', 'Bharath', 'Mohan', 'Yagnendra', 'Nishant', 'Kamal', 'Subramanya', 'Chandresh', 'Kiran Kumar', 'Pundarik', 'Ramesh', 
   'Shailendra', 'Bhavani', 'Abhinav', 'Mahendra', 'Rajiv', 'Devaraj', 'Akshay', 'Akarsh', 'Balu', 'Karnan', 'Narayanswami', 'Yogeshwar', 'Srinivasulu', 'Shubhranshu', 
   'Manikandan', 'Tejas', 'Vijay', 'Udayashankar', 'Shyam', 'Vedavath', 'Rajit', 'Rajendra', 'Soham', 'Srinivasan', 'Devakumar', 'Sampath', 'Mahadevan', 'Madhuri', 
   'Harindra', 'Santhosh', 'Bala', 'Shakti', 'Deependra', 'Jeetendra', 'Sandeepan', 'Sashank', 'Dilip', 'Rajaram', 'Brahma', 'Sharvesh', 'Amit', 'Mahesh', 'Indrajit', 
   'Jagadish', 'Maneesh', 'Umesh', 'Himanshu', 'Nandan', 'Saurabh', 'Haran', 'Gopalan', 'Akash', 'Shubho', 'Arjun', 'Naren', 'Shiva', 'Tharun', 'Tejaswi', 'Abhay', 
   'Aarav', 'Vasanth', 'Shrikant', 'Krishnakumar', 'Yadava', 'Hariprasad', 'Santoshi', 'Udayendra', 'Suryanarayan', 'Vasudeva', 'Iggappa', 'Rishabh', 'Vinod', 'Vasudev',
    'Gunaranjan', 'Nithin', 'Hariom', 'Pritam', 'Sreenivas', 'Trilok', 'Chandranath', 'Vignesh', 'Shreyansh', 'Thimmaiah', 'Manohar', 'Biddappa', 'Karthikeyan', 
    'Raghunandan', 'Kamalanath', 'Chaitanya', 'Keshavan', 'Srikanth', 'Jayaram', 'Krisnamoorthy', 'Pavankumar', 'Sunil', 'Kalpesh', 'Suraj', 'Jeevendra', 'Abhishek',
     'Varun', 'Venkat', 'Venkataraman', 'Daya', 'Ishwar', 'Raghav', 'Hidayath', 'Haritha', 'Trivikram', 'Kishore', 'Ravi', 'Bhanu', 'Rohit', 'Prem', 'Subhash', 
     'Manish', 'Siddharth', 'Vasanthan', 'Tirumal', 'Yogananda', 'Jeevan', 'Gopal', 'Yogiraj', 'Dineshwar', 'Chandramohan', 'Ravi Kumar', 'Rukmini', 'Jayendra', 
     'Murugan', 'Venkateswara', 'Balarama', 'Chandran', 'Raghavan', 'Yash', 'Indranil', 'Aalok', 'Rupesh', 'Kanishk', 'Shreevar', 'Tanmay', 'Vikas', 'Abhijit', 
     'Bhuvan', 'Ravindra', 'Heshan', 'Jagan', 'Kailasam', 'Prabhu', 'Sadanand', 'Agnivesh', 'Gangesh', 'Manoj', 'Dineshan', 'Shastri', 'Murali', 'Parth', 'Shankarappa', 
     'Vishwanathan', 'Durgesh', 'Hari', 'Suryakant', 'Suryanarayana', 'Shreshth', 'Pravin', 'Adarsh', 'Vishwesh', 'Devanand', 'Ananta', 'Ishaan', 'Ravikumar', 
     'Bhuvanesh', 'Vedant', 'Makarand', 'Appaiah', 'Ankit', 'Chirantan', 'Vasundhara', 'Radhakrishna', 'Devappa', 'Naveenkumar', 'Deveshwar', 'Prakash', 'Pramod', 
     'Aman', 'Harilal', 'Viraappa', 'Alok', 'Anant', 'Madhukar']

    # Karnataka Male Surnames
    male_karnataka_surname = ['Dongre', 'Amarnath', 'Samaga', 'Sakleshpura', 'Udupi', 'Thakur', 'Kannur', 'Bidari', 'Ganjigatti', 'Arya', 'Birur', 'Poojary','Kolli',
                          'Raghunandan', 'Bagalkote', 'Kadra', 'Aithal', 'Yajaman', 'Pandavapura', 'Javali','Prabhavathi', 'Koparde', 'Shreepathi', 'Sannakki',
                          'Kurundwad', 'Shirasangi', 'Mandya', 'Gudigere', 'Gubbi', 'Ganganalli', 'Garadi', 'Belgaum', 'Yellappa', 'Basavappa', 'Nayaka', 'Reddy',
                          'Chincholi', 'Shivalli', 'Tiwari', 'Chavadi', 'Wodeyar', 'Kshetra', 'Rudrappa', 'Nayak', 'Bagavi', 'Bannur', 'Kondajji', 'Hugar',
                          'Ganganavar', 'Neelakantan', 'Murthy', 'Tonse', 'Alapti', 'Badami', 'Satyapriya', 'Kundapur', 'Savanur', 'Narayanappa', 'Varalakshmi',
                          'Kota', 'Salagame', 'Bilgi', 'Naik', 'Shivamurthy', 'Kampli', 'Udupa', 'Talikoti', 'Lokesh', 'Nittur', 'Kasargod', 'Hegde', 'Doddaballapura',
                          'Tantry', 'Sakleshpur', 'Mirajkar', 'Koratagere', 'Vikas', 'Belur', 'Kulkarni', 'Ilkal', 'Vidhya', 'Mestri', 'Uppunda', 'Anvekar', 'Raj',
                          'Bilagi', 'Iyengar', 'Kadamba', 'Vaikunthe', 'Chennappa', 'Muthuswami', 'Vijay', 'Banhatti', 'Ramachandra', 'Singanal', 'Kodihalli', 'Dodderi',
                          'Udaya', 'Saralaya', 'Nadan', 'Harapanahalli', 'Karjagi', 'Narayan', 'Mulbagal', 'Tumkur', 'Sangolli', 'Thippanna', 'Gururaj', 'Sontakke',
                          'Shet', 'Kolhar', 'Madhwaraj', 'Sadhvi', 'Bhat', 'Banakar', 'Saligrama', 'Panju', 'Gajendran', 'Karigowda', 'Sindagi', 'Kaniyoor', 'Dharmadhikari',
                          'Poojari', 'Adiga', 'Koppal', 'Karadi', 'Chikodi', 'Giri', 'Ittigi', 'Dandavati', 'Huli', 'Soni', 'Kudligi', 'Viswanathan', 'Vernekar', 'Kadkol',
                          'Gowda', 'Ullal', 'Prabhakar', 'Katti', 'Rathnakara', 'Porandla', 'Gadiyar', 'Seshadri', 'Vittal', 'Sorab', 'Gava', 'Shanbhag', 'Boddapur',
                          'Arsikere', 'Sashidhar', 'Thimmaiah', 'Taralagatti', 'Acharya', 'Madappa', 'Chikkanayakana Halli', 'Kolar', 'Suli', 'Arunachala', 'Kalmath', 'Yallappa',
                          'Bailur', 'Kailasam', 'Gade', 'Aland', 'Gangashetti', 'Sangama', 'Jain', 'Narvekar', 'Jamakhandi', 'Vibhuti', 'Kottari', 'Yemme', 'Bellare',
                          'Chikkanayaka', 'Kalal', 'Yellamma', 'Kodgi', 'Athreya', 'Puttur','Rai', 'Peddana', 'Chikkamagaluru', 'Thackeray', 'Surendra', 'Narasimharajapur', 'Suman',
                          'Bommanahalli', 'Nambiar', 'Karnad', 'Mallya', 'Kalkundrikar', 'Bhadravathi', 'Gokak', 'Rudranath', 'Hosakote', 'Santhoor', 'Shravanabelagola', 'Mesta',
                          'Menasinakai', 'Shiralakoppa', 'Hiriyur', 'Angadi', 'Kalvade', 'Karigannur', 'Madappan', 'Singaram', 'Sagar', 'Shetty', 'Nagappa', 'Upadhyay', 'Gokarna',
                          'Chiniwar', 'Mudenur', 'Manjunath', 'Panambur', 'Patwardhan', 'Agadi', 'Salim', 'Venkataraman', 'Jajpur', 'Palliyeri', 'Yalvigi', 'Shyam', 'Channappa',
                          'Kushalappa', 'Kumar', 'Siddi', 'Nagashetti', 'Chandapur', 'Sunil', 'Vini', 'Kalasapura', 'Kini', 'Tirumakudal', 'Baliga', 'Upadhya', 'Doddamani',
                          'Honnappa', 'Uttur', 'Rao', 'Lakshmanan', 'Singana', 'Tippanna', 'Chikkaballapur', 'Mahale', 'Guledgudda', 'Sool', 'Kelgeri', 'Srinivas',
                          'Panikkar', 'Belavadi', 'Avati', 'Muddebihal', 'Tambe', 'Rajeshwari', 'Ninge', 'Sirdeshpande', 'Vaman', 'Siddhi', 'Shridhar', 'Bhoja', 'Moily',
                          'Kedilaya', 'Vijayalakshmi', 'Urmil', 'Pal', 'Kodagu', 'Pujari', 'Nandini', 'Tendulkar', 'Nalwadi', 'Dharwad', 'Yamuna', 'Verma', 'Shirahatti', 'Kamadenu',
                          'Vaidya', 'Somayaji', 'Kodandaram', 'Rajur', 'Yellur', 'Devappa', 'Gudi', 'Doddabettahalli', 'Gundappa', 'Uppar', 'Kurdu', 'Yogaraj', 'Hiremath',
                          'Channarayapatna', 'Achar', 'Laxmeshwar', 'Kurdi', 'Bhatkal', 'Kallur', 'Lakkappa', 'Suvarna', 'Santhosh', 'Vamshi', 'Dasappa', 'Ganiga', 'Kerur',
                          'Kadri', 'Talwar', 'Kadadi', 'Chunchanur', 'Tharwani', 'Hukkeri', 'Doni', 'Sudhakar', 'Baranwal', 'Maddur', 'Cheppudira',  'Vijayakumar', 'Savkur',
                          'Kelkar', 'Indi', 'Medappa', 'Marpalli', 'Pangal', 'Yerramalli', 'Malgudi', 'Bandaru', 'Deekshit', 'Patil', 'Yelur', 'Yeragar', 'Shirur', 'Kamath', 'Nandi',
                          'Sharma', 'Mahadevappa', 'Ramanagara', 'Ellur', 'Hosur', 'Inamdar', 'Halageri', 'Vasudev', 'Yenagi', 'Mehandi', 'Burli', 'Jadhav', 'Gadag', 'Yogananda',
                          'Deshpande','Upadhyaya', 'Hiremani', 'Ballari', 'Heggade', 'Korwar', 'Kodical', 'Alva', 'Aralikatti', 'Gulwadi', 'Kanavi','Melkote', 'Navalgund', 'Dattatreya',
                          'Gattimuddanahalli','Annappa', 'Karkala', 'Vaikuntam', 'Desai']

    # Karnataka Female First Names
    female_karnataka_firstname = [
         "Aarti", "Adithi", "Aditi", "Ahalya", "Aishwarya", "Akshara", "Akshata", "Akshatha", "Akshaya", "Akshitha",
    "Alakananda", "Alamelu", "Amrita", "Amrutha", "Amulya", "Anagha", "Ananya", "Anitha", "Anjali", "Annapoorna",
    "Ansuya", "Anu", "Anupama", "Anuradha", "Anusha", "Anushka", "Anushree", "Aparajitha", "Aparna", "Archana",
    "Arpita", "Arpitha", "Aruna", "Arundhati", "Asha", "Ashlesha", "Ashrita", "Ashwini", "Asmita", "Avani", "Avantika",
    "Bhadra", "Bhagirathi", "Bhagyashree", "Bhairavi", "Bharathi", "Bhargavi", "Bhavana", "Bhavani", "Bhavika",
    "Bhavya", "Bhoomika", "Brinda", "Cauvery", "Chaitra", "Champa", "Chandana", "Chandralekha", "Chandrika", "Charitha",
    "Chaya", "Chithra", "Chitra", "Daksha", "Dakshayani", "Damayanti", "Damini", "Darshana", "Deepa", "Deepashree",
    "Deepika", "Deepthi", "Deepti", "Devaki", "Devi", "Devika", "Dhanashree", "Dhanya", "Dhara", "Disha", "Divya",
    "Divyashree", "Drishti", "Durga", "Ektha", "Esha", "Eshwari", "Gagana", "Ganga", "Gauri", "Gayathri",
    "Geetha", "Geethanjali", "Girija", "Girijamma", "Gomathi", "Gowri", "Grishma", "Hamsa", "Harini", "Haripriya",
    "Harshitha", "Hema", "Hemalatha", "Hemashree", "Hemavathi", "Hitha", "Indira", "Indumathi", "Isha",
    "Ishitha", "Ishwari", "Ishwarya", "Jagadamba", "Jalaja", "Janaki", "Janani", "Janhavi", "Jayalakshmi", "Jayanthi",
    "Jayanti", "Jayashree", "Jayavathi", "Jyothi", "Jyothika", "Kalindi", "Kalpana", "Kamakshi", "Kamala", "Kamini",
    "Kanaka", "Kanika", "Karuna", "Kasturi", "Kaushalya", "Kaveri", "Kavitha", "Kavya", "Kavyashree", "Keerthana",
    "Keerthi", "Kiran", "Kiranmayi", "Komala", "Kripa", "Krithika", "Krupa", "Kumari", "Kumudha", "Kumudini", "Kusuma",
    "Lakshitha", "Lakshmi", "Lalitha", "Lasya", "Latha", "Lavanya", "Laxmi", "Leela", "Leelavathi", "Likhita", "Likhitha",
    "Lila", "Lokeshwari", "Maanasa", "Madhavi", "Madhu", "Madhura", "Mahadevi", "Mahalakshmi", "Maithreyi", "Maitreyi",
    "Malavika", "Malini", "Mallamma", "Mallika", "Mamatha", "Manasa", "Mandakini", "Manisha", "Manjari", "Manju",
    "Manjula", "Manonmani", "Mayuri", "Meena", "Meenakshi", "Meera", "Megha", "Meghana", "Menaka", "Mohana", "Mohini",
    "Moksha", "Monisha", "Mounika", "Mridula", "Mrinalini", "Mythili", "Mythri", "Nageshwari", "Nalini", "Namitha",
    "Nanda", "Nandini", "Nandita", "Nanditha", "Narmada", "Navya", "Nayana", "Neela", "Neelima", "Neeraja", "Nethravathi",
    "Netravati", "Nidhi", "Niranjana", "Nirupama", "Nishitha", "Nithya", "Padma", "Padmashree", "Padmavathi", "Pallavi",
    "Panchami", "Pankaja", "Parvathi", "Pavana", "Pavani", "Pavithra", "Pooja", "Poornima", "Pournami", "Prabha",
    "Prakruthi", "Pramila", "Pranathi", "Pranita", "Pranitha", "Prashanthi", "Prathibha", "Prathyusha", "Preethi", "Prerana",
    "Priya", "Priyanka", "Purnima", "Pushpa", "Pushpalatha", "Rachana", "Radha", "Radhe", "Radhika", "Rajani", "Rajeshwari",
    "Rajitha", "Raksha", "Ramaa", "Ramya", "Ranjana", "Ranjitha", "Rashmika", "Rathi", "Rathika", "Rathna", "Rekha",
    "Renuka", "Revathi", "Rishika", "Rishitha", "Rohini", "Roja", "Roopa", "Rukmini", "Rupa", "Rupali", "Sahana", "Sakethika",
    "Sakshi", "Samatha", "Samyuktha", "Sandhya", "Sangeetha", "Sangitha", "Sanika", "Sanjana", "Sapna", "Sarala", "Saraswathi",
    "Saraswati", "Sarika", "Saritha", "Sarvani", "Savitha", "Savithri", "Savitri", "Seema", "Seetha", "Shailaja", "Shalini",
    "Shankari", "Shanmukha", "Shantha", "Shanthala", "Shanthi", "Sharada", "Sharadhi", "Sharanya", "Sharavathi", "Sharmila",
    "Sharvani", "Shashi", "Shashikala", "Shashvathi", "Sheela", "Sheethal", "Shilaka", "Shilpa", "Shivani", "Shobha",
    "Shobhitha", "Shraddha", "Shree", "Shreedevi", "Shreeja", "Shreenidhi", "Shreenika", "Shreevalli", "Shreeya", "Shreya",
    "Shruthi", "Shubha", "Shubhalakshmi", "Shwetha", "Siddhi", "Sindhu", "Sirisha", "Sita", "Smita", "Sneha", "Snehal",
    "Snehalatha", "Sobha", "Soniya", "Soujanya", "Soumya", "Soundarya", "Sowmya", "Sridevi", "Srilakshmi", "Srilatha",
    "Srimathi", "Srishti", "Srividya", "Sruthi", "Sthuthi", "Subhadra", "Sudha", "Suguna", "Suhasini", "Sujatha", "Suma",
    "Sumana", "Sumangala", "Sunandha", "Sundari", "Sunitha", "Supriya", "Suraksha", "Susheela", "Sushila", "Sushma",
    "Sushmitha", "Suvarna", "Swathi", "Swetha", "Tanvi", "Tejaswini", "Tharini", "Tripura", "Triveni", "Uma", "Umashree",
    "Usha", "Usharani", "Ushas", "Vaibhavi", "Vaishnavi", "Vallari", "Vanaja", "Vani", "Vanitha", "Varalakshmi", "Varsha",
    "Vasanti", "Vasavi", "Vasudha", "Vasundhara", "Vatsala", "Veena", "Vidya", "Vidyashree", "Vijayalakshmi", "Vijayalaxmi",
    "Vimala", "Vinaya", "Vindhya", "Vinutha", "Vismaya", "Yamuna", "Yashaswini", "Yashica", "Yashitha", "Yashodha",
    "Yogitha", "Appi", "Dina", "Jeevitha", "Jaya", "Leena", "Suman", "Vijaya", "Aadya", "Abhaya", "Achala", "Adhira",
    "Alaka", "Amara", "Ambika", "Anasuya", "Charulatha", "Dhanalakshmi", "Iswarya", "Kanchana", "Kumud", "Kundana",
    "Malathi", "Madhuri", "Maya", "Narayani", "Pavitra", "Prabhavathi", "Pratibha", "Rajalakshmi", "Rama", "Shakuntala",
    "Shanti", "Sharini", "Swarna", "Tara", "Vishalakshi", "Yashoda", "Bhuvana", "Gita", "Indrani", "Kalyani", "Krishna",
    "Medhini", "Meenal", "Minakshi", "Nirmala", "Prabhati", "Rani", "Ruchi", "Sahaja", "Sangeeta", "Shanta", "Shantala",
    "Sumati", "Swarnaprabha", "Urmila", "Yashasvini", "Keshavi", "Nandana", "Nayantara", "Sadhana", "Sampada", "Shruti",
    "Simran", "Tanuja", "Tulasi", "Vandana", "Vishnupriya", "Yamika", "Aaradhya", "Gopika", "Indu", "Nisha", "Padmaja",
    "Rakhi", "Sahiti", "Sambhavi", "Alpana", "Anisha", "Bhuvani", "Chinmayi", "Chinmaye", "Dharini", "Hamsika", "Haritha",
    "Jeevika", "Kousalya", "Lathika", "Manya", "Mithra", "Nivetha", "Padmavati", "Pranjal", "Pravina", "Rashmi", "Renu",
    "Sagara", "Shanaya", "Shaveta", "Swarnalatha", "Vidhya", "Vishaka", "Vishalini", "Aarthi", "Akila", "Amritha",
    "Anvitha", "Bhuvaneshwari", "Darshini", "Deeksha", "Garima", "Gargi", "Geethika", "Hina", "Ira", "Kishori",
    "Madhulika", "Madhumita", "Nagarani", "Nivitha", "Poornachandra", "Pravathi", "Rachitha", "Radhya", "Ramitha",
    "Ranjani", "Ravi", "Sadhvi", "Sampoorna", "Sarasvathi", "Shubhangi", "Soma", "Swara", "Tanu", "Vimalini", "Vishwajeet",
    "Yashasvi", "Yogini", "Bhavitha", "Chinmayee"
    ]

     # Female Karnataka Surnames
    female_karnataka_surname = ['Upadhyay', 'Kundapur', 'Hiremath', 'Karigannur', 'Gudigere', 'Kudligi', 'Gudi', 'Savkur', 'Karjagi',
                             'Gangadhar', 'Shyam', 'Sirdeshpande', 'Belur', 'Poojari', 'Alva', 'Salim', 'Badami', 'Tumkur', 'Vernekar',
                             'Ellur', 'Kalmath', 'Salagame', 'Venkatesh', 'Kannur', 'Peddana', 'Medappa', 'Narasimharajapur', 'Kasargod',
                             'Vaidya', 'Sharma', 'Ganganalli', 'Gundappa', 'Ramachandra', 'Boddapur', 'Basavappa', 'Chennappa', 'Panambur',
                             'Suli', 'Tendulkar', 'Vaikunthe', 'Kolhar', 'Somayaji', 'Raghunandan', 'Shet', 'Mesta', 'Garadi', 'Koppal',
                             'Yenagi', 'Yogananda', 'Kolar', 'Santhosh', 'Karkala', 'Sivasubramanian', 'Arsikere', 'Bailur', 'Chincholi',
                             'Devappa', 'Karadi', 'Kallur', 'Shivamurthy', 'Cheppudira', 'Achar', 'Mandya', 'Javali', 'Thippanna', 'Mestri',]

    # Female suffixes for Karnataka
    female_karnataka_suffix = ["kumari", "amma", "devi","", "", "", "", "", ""]

    # Generate names using the male and female first names and suffixes
    names = []
    for _ in range(n // 2):
        male_first = random.choice(male_karnataka_firstname)
        male_last = random.choice(male_karnataka_surname)
        female_first = random.choice(female_karnataka_firstname)
        female_suffix = random.choice(female_karnataka_suffix)
        female_last = random.choice(female_karnataka_surname)

        # Combine names based on user preference
        if user_preference['name_type'] == 'first':
            name_male = male_first  # Only first name
            name_female = female_first 
        else:
            name_male = f'{male_first} {male_last}'
            name_female = female_first + female_suffix + ' '+ female_last

        # Add male and female names alternatively to maintain a 1:1 ratio
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))
        
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Ensure file writing happens
    file_path = 'generated_karnataka_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')
    
    print(f"Names have been written to '{file_path}' successfully.")
    return df

# Example usage
#user_preference = init({'name_type': 'full'})
#generated_names = generate_karnataka_names(100, user_preference)
#save_to_csv(generated_names, './generated_karnataka_names.csv')
