#Pisay ASAP! 

#Dictionary/Database of usernames and passwords
users = {
    "Villalon, Zea" : "123"}

#List of snacks with their prices
snacks = {
    "Mamon":34,
    "Magic Flakes":25,
    "Lumpia":25,
    "Cream-O":10,
    "Skyflakes Condensada": 10,
    "Nissin Wafer": 5,
    "Fita":15,
    "Marie":15,
    "Cassava Chips":50}

#List of drinks with their prices
drinks = {
    "Mogu Mogu":34,
    "Milo":25,
    "Chuckie":25,
    "Calamansi Juice":16,
    "Melon Shake": 99,
    "Mango Shake": 99,
    "Banana Shake":99,
    "Grape Shake":99,
    "Watermelon Shake": 99}

#List of meals with their prices
meals = {
    "Fried Chicken":70,
    "Chicken Tinola":70,
    "Sinigang na Isda":50,
    "Honey Garlic Pork":70,
    "Hungarian Sausage":35,
    "Pork Asado":70,
    "Hash Brown":50,
    "Tortang Talong":40,
    "Chicken Sisig":75}

#List of rices with their prices
rice = {
    "Half Rice":10,
    "Whole Rice":15,
    "No Rice":0}

#User-defined Function for signing up ☆ ZEA
def signUp():
    print("""
==========SIGN-UP PAGE☆==========""")   
    while True:
        #Function that asks for the user to enter their full name for their username
        username = input("""
Please enter your full name (Last name, First Name): """).title()
    
        #checks if username exists in the database
        if username in users:
            print("Username already exists! Please try again.")
        
        else:
            #Asks for the user to create their password
            password = input("Create password: ")
            #Pairs value(password) to key(username)
            users[username] = password
            print("Account created succesfully!")
            break
           


#User-defined function for logging in ☆ ZEA & ELJAI
def login():
    print("""
==========LOG-IN PAGE☆==========
""")
    user = input("Please enter your full name (Last name, First Name), or enter 'exit': ").title()
    
    if user.lower() == "exit":
        print("Returning to welcome page...")
        return "exit"
    
    password = input("Enter your password: ")
    
    #checking for right username and password
    if user in users and users[user] == password:
        print("Log-in Successful!")
        return True
    else:
        print("Invalid username or password. Please try again.") 
        return False
    

#Main menu for login and sign-up ☆ ZEA
while True:
    print("""
================================""")
    print("""
Welcome to Pisay Asap☆! 

[1] Log-in (If you have an existing account in the application)
[2] Sign-up (If you plan to create an account in the application.)
[3] Close the program""")
    
    welcomeChoice = input("""
Choice(1, 2, or 3): """)

    #Condition to check if user chose to log-in or input 1
    if welcomeChoice == "1":
        result = login()
        
        if result == "exit":
            continue # Sends user back to the start of the while loop
        elif result == True:
            break # goes to snack menu
        else:
            continue # Sends user back to the start of the while loop
    
     #Condition to check if user chose to sign-up or input 2
    elif welcomeChoice == "2":
        signUp()
    
    
    elif welcomeChoice == "3":
        print("See you again! Speedy services only here at Pisay ASAP!")
        exit()
        
    else:
        print("Invalid Choice! Please try again.")
    
#Main menu/interface for ordering 
        
print("""Welcome to the main menu!

================================

ORDER INFORMATION""")

while True:

    try:
         #Function to ask user's choice between snacks or meals 
        foodchoice = input("""
================================

Choose your food Category:

[1] Snacks
[2] Meals
[3] Exit the Program

Input your choice here: """)
        
        #Condition to check if user chose snacks or inputted 1. 
        if foodchoice == "1":
            while True:
                print("""
    Choose from the provided list:
    """)
                for food, price in snacks.items():
                    print(f"""
    {food}: Php {price}.00""")
                    
                snackchoice = input("""
    Pick your Snack: """).title()
                
                if snackchoice in snacks:
                    print(f"Added {snackchoice} to your tray!")
                    
                    addDrinksChoice = input("""
Add drinks? [Y/N]: """).upper()
                    if addDrinksChoice == "Y":
                        
                        print("-----DRINK MENU-----")
                        
                        for drinkName, drinkPrice in drinks.items():
                            print(f"""{drinkName}: Php {drinkPrice}.00""")
                            
                        while True:
                            drinkadd = input("""
Enter your drink choice here: """).title()
                            
                            if drinkadd in drinks:
                                print("Noted!")
                                break
                            
                            else:
                                print("""
Invalid input! Please try again.
""")
                        
                    elif addDrinksChoice == "N":
                        print("Noted!")

                    else:
                        print("Invalid Value.")

                    print("""
Order Recorded! (Checkout feature comming soon)""")
                    break
            
                else:
                    print(f"Sorry, '{snackchoice}' is not on the menu. Please Try Again.")
                
                
    
        #Condition to check if user chose meals or inputted 2. 
        elif foodchoice == "2":
            
            while True:
                print("""
    Choose from the provided list:
    """)
                for food, price in meals.items():
                    print(f"""
    {food}: Php {price}.00""")
                    
                mealchoice = input("""
    Pick your Meal: """).title()
                
                if mealchoice in meals:
                    print(f"Added {mealchoice} to your tray!")
                    
                    
                #Rice Selection
                    while True:
                        for food, price in rice.items():
                            print(f"""
            {food}: Php {price}.00""")
                        
                        ricechoice = input("""
            Pick your Rice: """).title()
                        
                        if ricechoice in rice:
                            print(f"Added {ricechoice} to your tray!")
                            break
                        
                        else:
                            print("Invalid input! Please try again.")
        
                    addDrinksChoice = input("""
    Add drinks? [Y/N]: """).upper()
                    if addDrinksChoice == "Y":
                        print("-----DRINK MENU-----")
                        for drinkName, drinkPrice in drinks.items():
                            print(f"""{drinkName}: Php {drinkPrice}.00""")
                                
                                
                        while True:
                            drinkadd = input("""
    Enter your drink choice here: """).title()
                                
                            if drinkadd in drinks:
                                print("Noted!")
                                break
                                
                            else:
                                print("""
    Invalid input! Please try again.
    """)
                            
                    elif addDrinksChoice == "N":
                        print("Noted!")

                    else:
                        print("Invalid Value.")
                    
                    print("""
    Order Recorded! (Checkout feature comming soon)""")
                    break
                
                else:
                     print(f"Sorry, '{mealchoice}' is not on the menu. Please Try Again.")

                   
            
        elif foodchoice == "3":
            print("See you again! Speedy services only here at Pisay ASAP!")
            break
        
    except ValueError:
        
        print("""
Invalid choice. Please Try Again.""")
        continue
    except TypeError:
        
        print("""
Invalid choice. Please Try Again.""")
        continue
    
        
