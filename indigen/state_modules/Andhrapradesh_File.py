import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
# The init function that sets user preferences
def init(user_preference=None):
        if user_preference is None:
            return {'name_type': 'full'}  # Default to full name
        return user_preference

# andhrapradesh Male First Names
def generate_andhrapradesh_names(n, user_preference=None):
    
    andhrapradesh_male_firstname= [
        "Aadhitya", "Aakash", "Aanjaneya", "Abhiram", "Achyuth", "Aditya", "Agastya", "Ajay", "Akash", "Akshay", 
        "Amarendra", "Amarnath", "Amogh", "Anand", "Ananth", "Anirudh", "Anjaneyulu", "Anudeep", 
        "Aravind", "Arjun", "Aryan", "Ashok", "Aswath", "Atreya", "Avinash", "Bala", "Balakrishna", "Balasubramanyam", 
        "Balavanth", "Balendra", "Balaram", "Bhadraksh", "Bhadri", "Bhagirath", "Bhanu", "Bhargav", "Bhaskar", 
        "Bheemesh", "Bhimesh", "Bhoopathi", "Chandrakanth", "Chandramouli", "Charan", "Chidambaram", "Chinnaiah", 
        "Chiranjeevi", "Dakshinamurthy", "Dhananjay", "Dharan", "Dharmendra", "Dharmesh", "Dinesh", "Divakar", 
        "Durgesh", "Dwaraka", "Ekambaram", "Elango", "Eshwar", "Ganapati", "Gangadhara", "Ganesha", "Gangaiah", 
        "Garuda", "Gaurav", "Gautham", "Giridhar", "Girish", "Govinda", "Guhan", "Hanuman", "Hari", "Haribabu", 
        "Harikrishna", "Harish", "Harsha", "Harshavardhan", "Hemachandra", "Hemal", "Hemanth", "Himanshu", "Indra", 
        "Ishwara", "Jagadeesh", "Jagannath", "Jagdish", "Janardhan", "Jayanth", "Jayaram", "Jayasimha", "Jitendra", 
        "Kalyan", "Kamal", "Kamalakar", "Kamalesh", "Kamesh", "Kanakaraju", "Kanthaiah", "Karunakar", 
        "Kasthuri", "Keshava", "Ketan", "Kiran", "Kishore", "Krishnamurthy", "Krishnamoorthy", "Krishnaiah", 
        "Krishnappa", "Kumaraswamy", "Lakshman", "Lakshmanaiah", "Lingaiah", "Lokesh", "Madhava", "Madhukar", 
        "Mahadevaiah", "Mahalingam", "Mahesh", "Mallikarjuna", "Manikanta", "Manoj", "Maruthi", "Mayura", "Meghnad", 
        "Mohan", "Mohanrao", "Mukunda", "Murali", "Murthy", "Nagabhushanam", "Nagarjuna", "Nagendra", "Nagendranath", 
        "Naresh", "Narahari", "Narasimha", "Narasimhaiah", "Narayana", "Narayanappa", "Narsimha", "Nataraja", 
        "Neelakantaiah", "Nishanth", "Padmanabha", "Pavan", "Perumal", "Phanindra", "Prabhakar", "Pradeep", 
        "Prakash", "Pramod", "Pranav", "Prashanth", "Pratap", "Praveen", "Premanand", "Radhakrishna", "Rajagopal", 
        "Rajarshi", "Rajasekar", "Rajendra", "Rajesh", "Rakesh", "Ramachandraiah", "Ramakrishnaiah", "Ramana", 
        "Ramanaiah", "Ramanuj", "Ramarao", "Ramesh", "Ranganath", "Ranjith", "Ravindra", "Ravi", "Ravindraiah", "Sai", 
        "Samudra", "Sanjeev", "Sanyasi", "Satish", "Satyamurthy", "Satyanarayana", "Seetharam", "Shankar", 
        "Shanmukhaiah", "Shekhar", "Shivaramakrishnaiah", "Shivashankar", "Siddhartha", "Siddhu", "Sikandar", 
        "Simhadri", "Sitaram", "Someswar", "Sreenivas", "Srinivasulu", "Sripathi", "Subbaiah", "Subbarao", 
        "Subrahmanya", "Sudarshan", "Sugreev", "Sukumar", "Sumanth", "Sundararajan", "Sundar", "Surendra", "Surya", 
        "Suryaprakash", "Swamy", "Tanishq", "Thirumal", "Uday", "Umesh", "Upendra", "Vamana", "Vamsi", 
        "Varun", "Vasu", "Vasudevaiah", "Venkanna", "Venkataramanappa", "Venkataramanaiah", "Venkatesaiah", 
        "Venkateswaraiah", "Venkayya", "Vidyasagar", "Vijayakumar", "Vinay", "Vishal", "Vishnu", 
        "Vishnuvardhan", "Viswamitra", "Vivek", "Vyas", "Yadagir", "Yajnesh", "Yamuna", "Yashwant", "Yogendra", 
        "Yoganandaiah", "Yogi", "Yudhistira", "Adiseshaiah", "Balakrishnaiah", "Bhanudas", "Chandrappa", 
        "Chandraiah", "Gangadharaiah", "Garudaiah", "Govindarajaiah", "Hanumanthaiah", "Harinath", 
        "Harihara", "Ilavarasan", "Jayadevaiah", "Jayasimhaiah", "Kaleswaraiah", "Krishnayya", "Lingamurthy", 
        "Madhunandhan", "Mahipal", "Manjunathaiah", "Marutirao", "Moorthy", "Nageswaraiah", "Narayanappaiah", 
        "Neelakanthaiah", "Padmanabaiah", "Raghavendraiah", "Raghunandan", "Rajeshwaraiah", "Ramakrishnayya", "Sanjay", 
        "Satyanand", "Shanmugham", "Shrinivas", "Somashekaraiah", "Srinath", "Sriram", "Sudhakar", "Surendranath", 
        "Tulasiram", "Varaprasad", "Vasundharaiah", "Veerabhadraiah", "Viswanadhaiah", "Yaswanth", "Yogaraj", 
        "Aanjaneyulu", "Abbayya", "Achutaiah", "Adinarayana", "Apparao", "Appanna", "Appayya", "Bhaskarappa", 
        "Bhadraiah", "Bhanuchander", "Bhargavaiah", "Bhaskaraiah", "Brahmaiah", "Chennakeshava", "Chintalapudi", 
        "Dattatreya", "Doddanna", "Edurappa", "Elumalai", "Gangappa", "Gangaraju", "Garapati", "Giridharayya", 
        "Govindayya", "Hanumantaiah", "Jagannathaiah", "Janakiramaiah", "Jayanarayan", "Jayaramayya", "Jogayya", 
        "Kadambaiah", "Kamalakarayya", "Kanakayya", "Kasina", "Kasinathaiah", "Kesavayya", "Kondalrao", "Kondaiah", 
        "Krishnamurthyiah", "Kurmaiah", "Lakshmi Narayana", "Lingamaiah", "Lokayya", "Madhavaiah", "Mallesh", 
        "Mallikarjunaiah", "Manikyam", "Mohanayya", "Muralidharayya", "Nagaraju", "Nagaswamy", "Nagendramma", 
        "Narayanaiah", "Narasimhulu", "Narsayya", "Nareshkumar", "Paramesh", "Paramatma", "Parandham", "Perumallu", 
        "Prabhakaraiah", "Pratapaiah", "Puttaiah", "Raghuveer", "Rajanna", "Rajaramayya", "Rajeswaraiah", "Raju", 
        "Ramaiah", "Ramanjaneyulu", "Ramayya", "Ramchandraiah", "Ramulamma", "Rangarao", "Ranganayakayya", 
        "Ravulapati", "Sadashivaiah", "Saibabaiah", "Sailu", "Sambayya", "Sampathkumar", "Sanjivayya", "Sankaraiah", 
        "Sastry", "Satyanarayanaiah", "Seetaramayya", "Seshu", "Shankaranna", "Shantakumaraiah", "Sharvayya", 
        "Sheshadri", "Siddiah", "Sitaiah", "Sivaramaiah", "Somasundaraiah", "Subrahmanyam", "Sudhakaranna", 
        "Sugunayya", "Sundararajaiah", "Surendramma", "Suryanarayanaiah", "Swami", "Tathachari", "Tirupataiah", 
        "Tirupathi", "Tulasiramayya", "Umapathi", "Upendraiah", "Vangaraiah", "Varadarajaiah", "Venkatesham", 
        "Venkateshulu", "Vijayayya", "Vignesh", "Vishnuvardhanayya", "Yadavaiah", "Yagnavalkya", "Yamunayya", 
        "Yerranna", "Adikesavulu", "Ammanna", "Annayya", "Annaraya", "Annavarapu", "Appalanaidu", "Aravindhaiah", 
        "Arjunanna", "Baburao", "Balanna", "Balaramaiah", "Bhimaiah", "Bhoopal", "Brahmanandaiah", "Chennakesavulu", 
        "Chidambarayya", "Devayya", "Dhananjayaiah", "Dheerajanna", "Durgaprasadaiah", "Eknathayya", "Elaparamathaiah", 
        "Gangarao", "Garikaiah", "Gopalaiah", "Govindaiah", "Gururajaiah", "Hampaiah", "Hariharaiah", "Harinathaiah", 
        "Iyyappa", "Jayaraman", "Jogiraju", "Kakani", "Kesavarao", "Kesavaiah", "Krishnarao", "Kumarayya", 
        "Lakshmanarao", "Lakshmipathi", "Lokanatham", "Malleswaraiah", "Manjunatha", "Mastanayya", "Maturi", 
        "Mohanaramaiah", "Naidu", "Namasivayaiah", "Narasappa", "Narasimhachari", "Narayanarao", "Narasingarao", 
        "Pattabhiramaiah", "Polanna", "Prakasarao", "Prataparao", "Prithvirajaiah", "Pullaiah", "Puttayya", 
        "Raghupathi", "Rajaiah", "Rajarathnaiah", "Rajendraiah", "Ramaswami", "Rangayya", "Ravikiran", "Rayalu", 
        "Sadashivayya", "Sainathaiah", "Seshappa", "Shankarappa", "Shantayya", "Shyamaramaiah", "Siddappaiah", 
        "Singanna", "Sitaramaiah", "Srinivasaiah", "Subanna", "Subramanyam", "Sudharshanayya", "Sugunarao", 
        "Sundaramma", "Suryaprakashaiah", "Swaminathayya", "Timmappa", "Tirupati", "Udayaramaiah", 
        "Umakanthaiah", "Vaddanapudi", "Vamanaiah", "Vanapalli", "Vasanthaiah", "Vasi", "Vemana", "Venkatakrishnayya", 
        "Venkateshwarlu", "Vibhutanna", "Vijayakumaraiah", "Vigneshvaraiah", "Visweswarayya", 
        "Yadagirayya", "Yagnaiah", "Yedukondalu", "Yellappa", "Yerriswamy", "Yugandharaiah", "Adinarayanaiah", 
        "Alluri", "Anjigutta", "Babayya", "Balaswamy", "Balaramudu", "Bhavanarayana", "Bhujangaiah", "Brahmachary", 
        "Chandrasekharayya", "Chelikam", "Chittemmaiah", "Devenderayya", "Doddachari", "Durgeshwaraiah", "Elanna", 
        "Gajendranath", "Gokulayya", "Gollapudi", "Gopalakrishnaiah", "Gundappaiah", "Harikrishnaiah", 
        "Ikkadaiah", "Jayanandaiah", "Jwalanna", "Kalyanaprasadaiah", "Kotayya", "Madirajaiah", "Moorthaiah", 
        "Phanindraiah", "Virupakshaiah"]


    # andhrapradesh Female First Names
    andhrapradesh_female_firstname =  ['Saipriya', 'Thrisha', 'Srinidhi', 'Sitara', 'Gowri', 'Dayamani', 'Sindhuri', 'Saadhana', 'Suhasini', 'Arpitha', 'Vanitha',
                                   'Venkatalakshmi', 'Bhagavathi', 'Dayanidhi', 'Shalini', 'Niharika', 'Mallika', 'Vaijayanthi', 'Anjali', 'Haripriya', 'Bhagya',
                                   'Aaryama', 'Saanvi', 'Amulya', 'Deevamma', 'Ananya', 'Tejaswi', 'Subbalakshmi', 'Kethaki', 'Neelima', 'Rama', 'Shruthi', 'Bhagyavathi',
                                   'Aishwarya', 'Kadambari', 'Amrutha', 'Manorama', 'Vasavi', 'Vinodha', 'Chaya', 'Adithi', 'Malleswari', 'Manasa', 'Pushpa', 'Shilpa',
                                   'Mohini', 'Saketha', 'Veena', 'Pavani', 'Ruthika', 'Achala', 'Sucharitha', 'Harini', 'Ishwarya', 'Bhudevi', 'Chandramma', 'Chitra',
                                   'Annadurga', 'Chandana', 'Chandravathi', 'Sharada', 'Vathsala', 'Hema', 'Deepamala', 'Mangala', 'Jagadamba', 'Ramani', 'Aruna',
                                   'Arundhathi', 'Taradevi', 'Veenavani', 'Reshmi', 'Bhanu', 'Saraswathi', 'Sunitha', 'Sumana', 'Shanta', 'Sitamma', 'Kaavya', 'Savithri',
                                   'Sarojini', 'Suseela', 'Raktha', 'Geetha', 'Jayanthi', 'Kasturi', 'Aparna', 'Sushmitha', 'Rukmini', 'Karunamayi', 'Preethi', 'Vishakha',
                                   'Manjula', 'Vanaja', 'Vidya', 'Vinodini', 'Kavitha', 'Kalyani', 'Parameswari', 'Kamalamma', 'Tripura', 'Vimala', 'Yagna', 'Urmila', 'Sumedha',
                                   'Rishitha', 'Prathyusha', 'Visalakshi', 'Meena', 'Uma', 'Usharani', 'Rajeswari', 'Sharmila', 'Gangamma', 'Jaya', 'Priyadarshini', 'Vatsala',
                                   'Santhoshi', 'Vinitha', 'Urvashi', 'Siri', 'Amba', 'Varsha', 'Tarakeshwari', 'Alivelu', 'Indira', 'Priya', 'Namitha', 'Hitha', 'Balamani',
                                   'Tharuni', 'Nandana', 'Eesha', 'Dhanya', 'Garikipati', 'Sahithi', 'Suguna', 'Vardhini', 'Hamsa', 'Sowjanya', 'Sneha', 'Narayani',
                                   'Chandralekha', 'Pranathi', 'Jyothika', 'Karuna', 'Saigeetha', 'Mallamma', 'Andalamma', 'Hemalatha', 'Premalatha', 'Deepika', 'Gouthami',
                                   'Sailaja', 'Venkayamma', 'Vidhya', 'Aadhya', 'Pratibha', 'Swarna', 'Lakshmidevi', 'Adhira', 'Kannamma', 'Soni', 'Hima', 'Pragna', 'Kanakadurga',
                                   'Nageswari', 'Charitha', 'Vinaya', 'Sindhu', 'Devi', 'Bhavana', 'Kunti', 'Kalpana', 'Nishitha', 'Devika', 'Rohini', 'Bala', 'Shyamalamma',
                                   'Radhika', 'Tanvi', 'Abhilasha', 'Eshwari', 'Janaki', 'Mamatha', 'Gowramma', 'Yamini', 'Vasudha', 'Sandhya', 'Yellamma',
                                   'Gagana', 'Shivani', 'Anagha', 'Vaishnavi', 'Rekha', 'Chinthamani', 'Sadhana', 'Adithya', 'Swapna', 'Vishnupriya', 'Harinakshi',
                                   'Padmavathi', 'Prathima', 'Yogitha', 'Alekhya', 'Soubhagya', 'Ahalya', 'Naga Lakshmi', 'Maheshwari', 'Annapoorna', 'Archana', 'Thulasi',
                                   'Mrinalini', 'Aliveni', 'Yogini', 'Nandhini', 'Sheela', 'Krishnaveni', 'Sravani', 'Roopa', 'Revathi', 'Aamani', 'Bhagirathi', 'Rani',
                                   'Subhadra', 'Sangeetha', 'Kamakshi', 'Durga', 'Vijayamma', 'Shashi', 'Pallavi', 'Mrudula', 'Kamalaja', 'Rajalakshmi', 'Shakuntala',
                                   'Shakunthala', 'Sitadevi', 'Yashoda', 'Anusha', 'Deepa', 'Naga Veni', 'Sharvani', 'Shashikala', 'Jwala', 'Akshitha', 'Usha', 'Sundari',
                                   'Shaila', 'Prakruthi', 'Sujatha', 'Bhavani', 'Navaneetha', 'Ratna', 'Ramadevi', 'Srilatha', 'Dhanalakshmi', 'Mangalagiri', 'Jagruthi',
                                   'Sarvani', 'Akshara', 'Yogalakshmi', 'Mandara', 'Bhoomika', 'Shubha', 'Vaidehi', 'Latha', 'Gangavathi', 'Sunanda', 'Neelambari',
                                   'Keerthana', 'Sindhura', 'Tharunika', 'Kameshwari', 'Kusuma', 'Sripriya', 'Jamuna', 'Pankajam', 'Suvarna', 'Nagalakshmi', 'Poornima',
                                   'Vallika', 'Girija', 'Vasundhara', 'Lavanya', 'Sithara', 'Chaitanya', 'Yashaswini', 'Bhavya', 'Sri Lakshmi', 'Neeraja', 'Mythrayee',
                                   'Aadarshini', 'Sowbhagya', 'Devamma', 'Priyamvada', 'Indumathi', 'Nirmala', 'Komala', 'Srilakshmi', 'Taruni', 'Shyamala', 'Rupa', 'Kanthi', 'Manjari', 'Ambika', 'Anitha', 'Lakshmi', 'Athira', 'Vijaya', 'Avani', 'Jyothi', 'Mahitha', 'Sridevi', 'Anasuya', 'Dhanavathi', 'Anuradha', 'Sudha', 'Malathi', 'Swarnalatha', 'Supriya', 'Madhavi', 'Navya', 'Chiranjeevi', 'Ramulamma', 'Priyanka', 'Sugunamma', 'Renuka', 'Bhagyamma', 'Archamma', 'Vasantha', 'Vasanthi', 'Kanaka', 'Manjusha', 'Ambuja', 'Devasena', 'Vandana', 'Bhuvaneshwari', 'Damayanti', 'Madhura', 'Smitha', 'Yashasvini', 'Meghana', 'Lalitha', 'Sripadmavathi', 'Vismaya', 'Vedavathi', 'Parvathi', 'Kanchana', 'Chamundeshwari', 'Sobhana', 'Vijayalakshmi', 'Parvati', 'Ushasri', 'Ravathi', 'Akhila', 'Radha', 'Vaibhavi', 'Srilaxmi', 'Ramamani', 'Aasha', 'Thilothama', 'Sumathi', 'Leelavathi', 'Menaka', 'Dharani', 'Ishani',
                                   'Vishalakshi', 'Sitamahalakshmi', 'Nalini', 'Vanamala', 'Saritha', 'Vasumathi', 'Surekha', 'Mahalakshmi', 'Sanjana', 'Srimathi', 'Sulochana', 'Haritha', 'Aslesha', 'Gayathri', 'Sumithra', 'Seetha', 'Padma', 'Venkamma', 'Vennela', 'Annapurna', 'Swathi', 'Jayasri', 'Srivani', 'Varalakshmi', 'Mythili', 'Hrudhya', 'Shambhavi', 'Ganga', 'Jayalakshmi', 'Vimaladevi', 'Nagamani', 'Pushpavathi', 'Parijatha', 'Gouri', 'Pavithra', 'Neelaveni', 'Kamala', 'Prabhavathi', 'Rajini', 'Kamalavathi', 'Shobha', 'Ishwari', 'Adilakshmi', 'Keerthi', 'Rajitha', 'Shanmukhi', 'Padmini']
    andhrapradesh_surname =  [
        "Aavula", "Adapa", "Addala", "Adusumilli", "Akula", "Alla", "Allam", "Amara", "Annam", "Annem", 
        "Annemreddy", "Anumolu", "Avirneni", "Bachu", "Badam", "Bandaru", "Barla", "Bathula", "Battula", 
        "Bayyapu", "Bellam", "Bellapu", "Bhairi", "Bhajana", "Bhamidipati", "Bhaskaruni", "Bhimavarapu", 
        "Boggarapu", "Bollineni", "Bommala", "Bommi", "Bonthu", "Borusu", "Boya", "Brahmamdam", "Chada", 
        "Challa", "Chamanthi", "Chappa", "Chekuri", "Chenchu", "Chilakala", "Chilukoti", "Chinthala", 
        "Chinthakindi", "Chittibabu", "Chittimalla", "Davuluri", "Deekonda", "Dega", "Devabhaktuni", 
        "Devaki", "Devarapalli", "Dhanekula", "Donepudi", "Dora", "Duggirala", "Dunna", "Edara", "Edulakanti", 
        "Ellam", "Emandi", "Emani", "Eranki", "Erram", "Erravalli", "Gadikota", "Gajula", "Galipalli", 
        "Galla", "Ganjam", "Gangaraju", "Garapati", "Garikapati", "Gautam", "Gella", "Ginjupalli", "Godugu", 
        "Gollapalli", "Gondi", "Gonuguntla", "Gottimukkala", "Guggilla", "Gunnam", "Gutti", "Hamsa", 
        "Indrakanti", "Ippili", "Jadav", "Jaganmohan", "Jaladi", "Jammi", "Jampala", "Javvadi", "Jeedigunta", 
        "Jillella", "Kadali", "Kadapa", "Kadari", "Kadavakollu", "Kaipa", "Kakani", "Kamani", "Kanamarlapudi", 
        "Kancharla", "Kandru", "Kandula", "Kanithi", "Kanumuri", "Kapilavai", "Karri", "Katragadda", 
        "Kavuri", "Kethineni", "Kodati", "Kolagatla", "Kolluru", "Komaragiri", "Kona", "Koneru", "Korivi", 
        "Kosaraju", "Kovuru", "Koyyada", "Kuncham", "Kurapati", "Kurra", "Kuruva", "Lanka", "Lankapati", 
        "Lankireddy", "Lavu", "Lingamgunta", "Lingala", "Machavaram", "Madala", "Madarapu", "Maddala", 
        "Maganti", "Mandapati", "Manda", "Manepalli", "Manikya", "Manyam", "Marada", "Mekala", "Mekapothula", 
        "Mekapati", "Merugu", "Mittapalli", "Mogali", "Mopidevi", "Motapothula", "Mudigonda", "Mudunuri", 
        "Mukkara", "Mullapudi", "Munagala", "Murikipudi", "Mutyalapati", "Naidu", "Nallamilli", "Namala", 
        "Nampally", "Nandyala", "Narahari", "Narava", "Narepalli", "Nedunuri", "Neelamraju", "Nemani", 
        "Neredla", "Nimmala", "Nori", "Nukala", "Onteddu", "Pagadala", "Paidipally", "Paleti", "Panthulu", 
        "Papannagari", "Papolu", "Parachuri", "Parvataneni", "Pasam", "Paturu", "Pedapudi", "Pedireddi", 
        "Peethala", "Pendyala", "Peram", "Pidathala", "Pingili", "Pitla", "Pochampally", "Podipireddy", 
        "Polimera", "Ponnala", "Porandla", "Pulipaka", "Pullabhotla", "Puppala", "Putchala", "Raavi", 
        "Ragipindi", "Ramanujam", "Rambhatla", "Ramesetti", "Ramisetty", "Rapolu", "Rathnam", "Reddem", 
        "Rentala", "Repalle", "Repaka", "Roga", "Rokkam", "Saagi", "Sadul", "Sajja", "Saladi", "Sambhu", 
        "Sampangirama", "Sammeta", "Saride", "Sasanka", "Seelam", "Senapati", "Somisetty", "Soppari", 
        "Tadipatri", "Tallapaka", "Talari", "Tatikonda", "Tenneti", "Terneni", "Thallam", "Tirumala", 
        "Totakura", "Tripuraneni", "Udatha", "Udayagiri", "Uppalapati", "Uraga", "Vajji", "Vallabhaneni", 
        "Vemuri", "Visweswara"]


    # Initialize user preferences (default to 'full' name type if not passed)
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        first_name_male = random.choice(andhrapradesh_male_firstname)
        last_name_male = random.choice(andhrapradesh_surname)
        
        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

                
        # Female Name Generation
        first_name_female = random.choice(andhrapradesh_female_firstname)
        last_name_female = random.choice(andhrapradesh_surname)
        
        if preferences.get('name_type') == 'first':
            name_female = first_name_female  # Only first name
        else:
            name_female = first_name_female + " " + last_name_female  # Full name

        # Append female name with gender information
        # Append male name with gender information
        names.append((name_male, "Male"))
        names.append((name_female, "Female"))

    
    df = pd.DataFrame(names, columns=["Name", "Gender"])

    # Ensure file writing happens
    file_path = 'generated_andhrapradesh_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')
    
    print(f"Names have been written to '{file_path}' successfully.")
    return df