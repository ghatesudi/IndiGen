import random
import pandas as pd
import os

# Function to initialize preferences from user input (defaults to 'full' name type if not passed)
# The init function that sets user preferences
def init(user_preference=None):
    if user_preference is None:
        return {'name_type': 'full'}  # Default to full name
    return user_preference

def generate_goa_names(n, user_preference=None):
    # Goa Hindu Male First Names
    goa_hindu_male_firstnames = [
        "Aaditya", "Abhay", "Abhishek", "Achyut", "Adarsh", "Advait", "Ajesh", "Ajit",
        "Akash", "Akshay", "Amar", "Amogh", "Anand", "Anay", "Anirudh", "Ankit", "Anshul",
        "Arjun", "Arnav", "Ashok", "Ashwin", "Atul", "Avinash", "Ayush", "Balaji", "Balkrishna",
        "Bhaskar", "Bhavesh", "Chetan", "Chintan", "Darshan", "Dayanand", "Deepak", "Dev", "Devendra",
        "Dhruv", "Dinesh", "Eknath", "Eshwar", "Gajanan", "Ganesh", "Gaurav", "Gopal", "Govind",
        "Gururaj", "Harish", "Harsha", "Hemant", "Hemanth", "Hriday", "Hrishikesh", "Indrajit", "Ishaan",
        "Ishwar", "Jagannath", "Jagdish", "Jaidev", "Jairam", "Jatin", "Jay", "Jayesh", "Jeevan", "Kailas",
        "Kalyan", "Kamal", "Karthik", "Kaviraj", "Kishore", "Krishna", "Kunal", "Laxman", "Lokesh", "Madhav",
        "Mahesh", "Manoj", "Mayur", "Milind", "Mohan", "Mukesh", "Murali", "Nagesh", "Nandan", "Narendra",
        "Naresh", "Navin", "Nikhil", "Nilesh", "Nishant", "Omkar", "Padmanabh", "Parth", "Prabhakar", "Pradeep",
        "Prakash", "Pranav", "Prashant", "Pratap", "Prem", "Purushottam", "Pushkar", "Rahul", "Rajesh", "Rajendra",
        "Rakesh", "Ramesh", "Ramkrishna", "Ranganath", "Ranjit", "Ravi", "Ravindra", "Rishabh", "Rohit", "Rudra",
        "Sachin", "Sagar", "Sandeep", "Sanjay", "Santosh", "Sarvesh", "Satish", "Sharad", "Sharv", "Shekhar",
        "Shivanand", "Shreepad", "Shridhar", "Shrinivas", "Siddharth", "Soham", "Somesh", "Subodh", "Sudarshan",
        "Sudesh", "Sukhdev", "Sunil", "Suraj", "Suresh", "Swapnil", "Tanmay", "Tejas", "Uday", "Umakant", "Umesh",
        "Upendra", "Vaibhav", "Vaman", "Vasant", "Vasudev", "Vedant", "Veeresh", "Vijay", "Vinay", "Vinayak", "Vipul",
        "Vishal", "Vishesh", "Vishnu", "Vivek", "Yashwant", "Yatin", "Yeshwanth", "Aditya", "Amrit", "Anil", "Anshuman",
        "Ayaan", "Bhanu", "Chandrakant", "Chaitanya", "Damodar", "Dattaram", "Devanand", "Girish", "Gunakar", "Hanumanth",
        "Harendra", "Jayant", "Keshav", "Lakshmikant", "Madhukar", "Manjunath", "Narayan", "Nirmal", "Omprakash", "Pankaj",
        "Rajkumar", "Ramachandra", "Shashank", "Sudhakar", "Trivikram", "Ujjwal", "Vallabh", "Venkatesh", "Vidhyadhar",
        "Vignesh", "Vishwajeet", "Yoganand", "Yugesh"
    ]
    # Goa Hindu surnames
    goa_hindu_surnames = [
        "Bhat", "Borkar", "Desai", "Gaonkar", "Gawas", "Hegde", "Kamat", "Kudtarkar",
        "Kunte", "Madgaonkar", "Naik", "Pai", "Prabhu", "Rane", "Rao", "Sawant", "Shenoy",
        "Shet", "Vernekar", "Bhandary"
    ]
    # Goa Hindu Female First Names
    goa_hindu_female_firstnames = [
        "Aditi", "Akshata", "Amruta", "Anagha", "Anjali", "Aparna", "Aruna", "Asmita",
        "Bhavani", "Bindiya", "Charita", "Chitra", "Damini", "Deepa", "Devika", "Dhanashree",
        "Diksha", "Disha", "Divya", "Durga", "Pavitra", "Prachi", "Prerana", "Priyal", "Raaga",
        "Raksha", "Renuka", "Riddhi", "Rupali", "Samiksha", "Sanika", "Sharini", "Shivali",
        "Srishti", "Suhasini", "Sumitra", "Sunita", "Surekha", "Suvarna", "Swati", "Aanya",
        "Aarna", "Aashika", "Advika", "Aira", "Anika", "Anvitha", "Arshi", "Avantika", "Ayesha",
        "Bhavana", "Bhumi", "Charvi", "Chhaya", "Darshana", "Deepthi", "Devina", "Diya", "Ekta",
        "Esha", "Eshwari", "Gauri", "Gayatri", "Geeta", "Girija", "Hansika", "Harika", "Harini",
        "Haritha", "Harsha", "Harshada", "Hasini", "Hema", "Hemal", "Hemangi", "Hemavathi", "Himani",
        "Hiral", "Hita", "Hridaya", "Hridya", "Hrudaya", "Indira", "Inika", "Ira", "Isha", "Ishani",
        "Ishita", "Iva", "Jagruti", "Janhavi", "Jaya", "Jayashree", "Jiya", "Jyoti", "Kalpana",
        "Kamakshi", "Kamini", "Kanchana", "Karuna", "Kavini", "Kavisha", "Kavita", "Kavya", "Keya",
        "Keyuri", "Krisha", "Kumari", "Lalita", "Lavanya", "Laxmi", "Laya", "Leela", "Mahi", "Mahika",
        "Mira", "Neelima", "Neha", "Niharika", "Nisha", "Nupur", "Ojaswi", "Pari", "Pratiksha", "Prisha",
        "Radha", "Rajeshwari", "Ranjana", "Rekha", "Revati", "Rina", "Riya", "Roopa", "Rukmini", "Saavi",
        "Sadhana", "Sailee", "Sakshi", "Sangeeta", "Saraswati", "Shanta", "Sharvani", "Sheetal", "Shilpa",
        "Shreya", "Shruti", "Sia", "Siya", "Smita", "Sneha", "Snehal", "Tanisha", "Tanvi", "Tara", "Tejaswini",
        "Trupti", "Uma", "Urmila", "Urvi", "Usha", "Vaidehi", "Vaishnavi", "Vandana", "Vandita", "Vanshika",
        "Varsha", "Vedika", "Veena", "Vidya", "Vinita", "Vrinda", "Yami", "Yamini", "Yashoda", "Yojana",
        "Lakshmi", "Parvati", "Sita", "Devi", "Meenakshi", "Annapurna", "Mahalakshmi", "Chamundeshwari",
        "Shivani", "Mahadevi", "Ambika", "Janaki", "Padmavati", "Nandini", "Anusuya", "Shakti", "Ananta",
        "Kalyani", "Tarini", "Shyama", "Indrani", "Sundari", "Bhairavi", "Kaveri", "Tulasi", "Mohini",
        "Mrinalini", "Amba", "Jagadamba", "Manjula", "Savitri", "Padma", "Ganga", "Sulochana"
    ]
    # Goa Cristian Male First Names
    goa_christian_male_names = [
        "Aaron", "Abel", "Abraham", "Adam", "Adrian", "Alan", "Albert", "Alex", "Alexander", "Alvin",
        "Alwyn", "Amos", "Andrew", "Anthony", "Arthur", "Aston", "Augustine", "Austin", "Avitus", "Baptist",
        "Barry", "Ben", "Bendict", "Benedict", "Benjamin", "Benny", "Bernard", "Bill", "Blaren", "Brendan",
        "Brian", "Bruce", "Bryan", "Caleb", "Calvin", "Carlos", "Charles", "Christian", "Christopher", "Clarence",
        "Cleevan", "Clifford", "Colin", "Cristopher", "Curtis", "Cyril", "Damien", "Daniel", "Darren", "David",
        "Dennis", "Deon", "Desmond", "Dominic", "Donald", "Dylan", "Edmund", "Edward", "Edwin", "Eilson", "Eli",
        "Elias", "Elijah", "Elisha", "Emmanuel", "Eric", "Ethan", "Evan", "Ezra", "Fabian", "Felix", "Flexon",
        "Francis", "Franklin", "Frenith", "Gabriel", "Gavin", "George", "Gerard", "Gideon", "Gilbert", "Glen",
        "Glenson", "Gordon", "Gratian", "Gravil", "Gregory", "Guy", "Harold", "Harry", "Heevan", "Henry", "Hugo",
        "Ian", "Ignatius", "Isaac", "Israel", "Ivan", "Jack", "Jacob", "James", "Jason", "Jeffrey", "Jerald",
        "Jeremiah", "Jerome", "Jerry", "Jesse", "Joackim", "Job", "Joe", "Joel", "John", "Johnathan", "Jonah",
        "Jonathan", "Joseph", "Joshua", "Josiah", "Joston", "Joyson", "Jude", "Justin", "Kenneth", "Kevin", "Kiran",
        "Lancy", "Lanville", "Lawrence", "Lazarus", "Leander", "Lenson", "Leo", "Leonard", "Leorand", "Levi", "Louis",
        "Loy", "Lucas", "Luke", "Maceth", "Marcel", "Mark", "Martin", "Mason", "Matthew", "Maxim", "Meldan", "Melric",
        "Micah", "Michael", "Moses", "Nathan", "Nathaniel", "Nelson", "Nicholas", "Nickson", "Nischal", "Noah", "Noel",
        "Oliver", "Olson", "Oscar", "Oswald", "Owen", "Pascal", "Patrick", "Paul", "Peter", "Philip", "Quincy", "Randolf",
        "Raphael", "Raymond", "Remo", "Renson", "Reuben", "Richard", "Robert", "Robin", "Roger", "Roland", "Ronald", "Roshan",
        "Royston", "Ruzar", "Ryan", "Salvadore", "Samuel", "Saul", "Sebastian", "Seth", "Sharon", "Sharwin", "Shawn", "Shruthan",
        "Simon", "Solomon", "Stanley", "Stephen", "Stewen", "Terence", "Terrance", "Theodore", "Thomas", "Timothy", "Tyron",
        "Valerian", "Victor", "Vincent", "Vivian", "Walter", "Warren", "Wilfred", "William", "Xavier", "Zacharias", "Zachary",
        "Zion"
    ]
    # Goa Cristian surnames
    goa_christian_surnames = [
        "Alberto", "Alvares", "Andrade", "Baptista", "Barboza", "Cardozo", "Carvalho", "Coelho",
        "Colaco", "Correa", "Costa", "Coutinho", "Crasta", "D'Cruz", "D'Lima", "D'Mello", "D'Silva",
        "De Souza", "Dias", "Faria", "Fernandes", "Furtado", "Gonsalves", "Lopez", "Mascarenhas",
        "Mendonca", "Menezes", "Miranda", "Monteiro", "Morais", "Nazareth", "Noronha", "Pais", "Pereira",
        "Pinto", "Quadros", "Rebello", "Rodrigues", "Rosario", "Sequeira", "Serrao", "Siqueira", "Saldanha",
        "Silva", "Soares", "Saldanha", "Vaz", "Xavier", "Abraham", "Alexander", "Antony", "Andrews",
        "Benjamin", "Chacko", "Daniel", "David", "D'Souza", "Fernandes", "George", "Gomes", "Gonsalves",
        "Isaac", "Jacob", "James", "John", "Joseph", "Kuriakose", "Lazar", "Lobo", "Mathew", "Mathias",
        "Menezes", "Michael", "Monteiro", "Morais", "Paul", "Pereira", "Peter", "Philip", "Pinto", "Raphael",
        "Rodrigues", "Samuel", "Sebastian", "Simon", "Stephen", "Thomas", "Timothy", "Varghese", "Victor",
        "Xavier", "Zachariah", "Zacharias", "Cherian", "D'Cruz", "D'Lima", "Noronha", "Tauro"
    ]
    # Goa  Cristian Female First Names
    goa_christian_female_names = [
        "Abigail", "Agatha", "Agnes", "Agnes", "Albeena", "Albina", "Alice", "Alice", "Alina",
        "Alysia", "Amanda", "Amelia", "Andrea", "Angel", "Angela", "Angelina", "Anita", "Anitha",
        "Ann", "Ann", "Anna", "Annette", "Asha", "Ashel", "Ashley", "Audrey", "Augustine", "Barbara",
        "Beatrice", "Beatrice", "Benedicta", "Bernadette", "Beryl", "Bethany", "Blossom", "Brenda",
        "Bridget", "Candice", "Carmel", "Carmelita", "Carmina", "Carmine", "Caroline", "Cassandra",
        "Catherine", "Catherine", "Cecilia", "Cecilia", "Celestine", "Celia", "Charity", "Cheryl",
        "Christiana", "Christina", "Christy", "Clara", "Clara", "Clara", "Clarissa", "Claudia",
        "Clementina", "Constance", "Cornelia", "Cosima", "Cristine", "Crystal", "Daphne", "Darlene",
        "Deborah", "Delia", "Demetria", "Diana", "Dina", "Dona", "Dorinda", "Dorothy", "Edna", "Eileen",
        "Elaine", "Eleanor", "Eleanor", "Eleanor", "Eliana", "Eliza", "Elizabeth", "Elizabeth", "Elsa",
        "Emeline", "Emma", "Esther", "Esther", "Eugene", "Eugenia", "Eve", "Evelyn", "Faustina", "Felcy",
        "Felicia", "Fiona", "Flan", "Flaviana", "Florence", "Frances", "Frizzel", "Gabriella", "Genevieve",
        "Genevive", "Georgia", "Georgina", "Gertrude", "Gilda", "Glenda", "Gloria", "Gloria", "Grace",
        "Gracy", "Gretchen", "Gwyneth", "Hannah", "Harriet", "Hazel", "Helen", "Helen", "Helen", "Hemal",
        "Henika", "Hilda", "Irena", "Irene", "Irene", "Irene", "Irene", "Isabel", "Isabella", "Ivanna", "Ivy",
        "Jacintha", "Jacintha", "Jacqueline", "Janet", "Janice", "Jemima", "Jenika", "Jennifer", "Jesicca",
        "Jesmitha", "Jessica", "Jessy", "Jiliet", "Joanna", "Johanna", "Josephine", "Josephine", "Jovita",
        "Joy", "Juanita", "Judith", "Julia", "Julia", "Juliana", "Juliana", "Justina", "Karen", "Karina",
        "Katherina", "Katherine", "Kimberly", "Kristina", "Lara", "Laura", "Leah", "Leena", "Lenora", "Leona",
        "Leonora", "Lilian", "Lillian", "Lilly", "Linda", "Lisa", "Lisbeth", "Lishma", "Lorraine", "Louella",
        "Louisa", "Lucy", "Lucy", "Lydia", "Magdalena", "Magdalene", "Magdaline", "Marceline", "Marcy",
        "Margaret", "Margaret", "Marguerite", "Maria", "Maria", "Marita", "Martha", "Martha", "Martina", "Mary",
        "Mary", "Mary", "Maryline", "Matilda", "Matilda", "Maureen", "Meena", "Megan", "Melita", "Mercy",
        "Michelle", "Miriam", "Miriam", "Monica", "Monisha", "Myrtle", "Nancy", "Naomi", "Natalie", "Natasha",
        "Neena", "Neola", "Nerissa", "Nicole", "Nicolina", "Nikitha", "Nina", "Noelle", "Nora", "Noreen",
        "Octivia", "Odilia", "Olisha", "Olivia", "Olivia", "Olympia", "Ophelia", "Oriel", "Pamela", "Patricia",
        "Patricia", "Patricia-Anne", "Paula", "Pauline", "Pauline", "Pearl", "Philomena", "Polly", "Precilla",
        "Precita", "Preemal", "Priscilla", "Rachel", "Rafaela", "Raveena", "Raylene", "Rebecca", "Reema", "Regina",
        "Regina", "Rhea", "Rishal", "Rita", "Rita", "Riya", "Rosalina", "Rosalind", "Rosanne", "Rose", "Rosy",
        "Roveena", "Ruby", "Ruth", "Sabrina", "Saloni", "Samantha", "Sana", "Sandra", "Sarah", "Sarah", "Sharel",
        "Sharlene", "Sheba", "Shirley", "Shirley", "Simone", "Steffy", "Stella", "Susannah", "Sylvia", "Teresa",
        "Theodora", "Theresa", "Tresa", "Valencia", "Venessa", "Veronica", "Veronica", "Vinolia", "Viola", "Viola",
        "Voilet", "Zelda"
    ]
    # Initialize user preferences
    preferences = init(user_preference)

    # Create a list to store names and their genders
    names = []

    # Generate names
    for i in range(n // 2):  # Generate half male and half female names
        # Male Name Generation
        if random.choice(["Hindu", "Christian"]) == "Hindu":
            first_name_male = random.choice(goa_hindu_male_firstnames)
            last_name_male = random.choice(goa_hindu_surnames)
        else:
            # Christian first name with Christian surname
            first_name_male = random.choice(goa_christian_male_names)
            last_name_male = random.choice(goa_christian_surnames)

        if preferences.get('name_type') == 'first':
            name_male = first_name_male  # Only first name
        else:
            name_male = first_name_male + " " + last_name_male  # Full name

        # Female Name Generation
        if random.choice(["Hindu", "Christian"]) == "Hindu":
            first_name_female = random.choice(goa_hindu_female_firstnames)
            last_name_female = random.choice(goa_hindu_surnames)
        else:
            # Christian first name with Christian surname
            first_name_female = random.choice(goa_christian_female_names)
            last_name_female = random.choice(goa_christian_surnames)


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
    file_path = 'generated_goa_names.csv'
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new data.")
    else:
        print(f"Creating a new file '{file_path}'.")

    df.to_csv(file_path, index=False, encoding='utf-8')

    print(f"Names have been written to '{file_path}' successfully.")
    return df

