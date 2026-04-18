#Pisay ASAP

# Dictionary/Database of usernames and passwords in the program
users = {
    "Villalon, Zea": "123"
}

# --- Menus --- oww
snacks = {
    "Mamon": 34,
    "Magic Flakes": 25,
    "Lumpia": 25, "Cream-O": 10,
    "Skyflakes Condensada": 10,
    "Nissin Wafer": 5,
    "Fita": 15,
    "Marie": 15,
    "Cassava Chips": 50}

drinks = {
    "Mogu Mogu": 34,
    "Milo": 25,
    "Chuckie": 25,
    "Calamansi Juice": 16,
    "Melon Shake": 99,
    "Mango Shake": 99,
    "Banana Shake": 99,
    "Grape Shake": 99,
    "Watermelon Shake": 99}

meals = {"Fried Chicken": 70,
         "Chicken Tinola": 70,
         "Sinigang na Isda": 50,
         "Honey Garlic Pork": 70,
         "Hungarian Sausage": 35,
         "Pork Asado": 70,
         "Hash Brown": 50,
         "Tortang Talong": 40,
         "Chicken Sisig": 75}

rice = {"Half Rice": 10,
        "Whole Rice": 15,
        "No Rice": 0}

tray = []
loggedinuser = ""

# --- FUNCTIONS ---

# function for sign-up page
def signUp():
    print("\n==========SIGN-UP PAGE☆==========")
    while True:
        username = input("\nPlease enter your full name (Last name, First Name): ").title()
        if username in users:
            print("Username already exists! Please try again.")
        else:
            password = input("Create password: ")
            users[username] = password
            print("Account created successfully!")
            break

# function for log-in page
def login():
    print("\n==========LOG-IN PAGE☆==========\n")
    user = input("Please enter your full name (Last name, First Name), or enter 'exit': ").title()
    
    if user.lower() == "exit":
        print("Returning to welcome page...")
        return "exit", ""
    
    password = input("Enter your password: ")
    if user in users and users[user] == password:
        print("Log-in Successful!")
        return True, user
    else:
        print("Invalid username or password. Please try again.") 
        return False, ""

# calculation of payment and choice of payment method
def payment(currentTray):
    if not currentTray:
        print("\nYour tray is empty!")
        return None, 0, None
    
    totalPrice = sum(item['itemPrice'] for item in currentTray)
    print("\n============================")
    print(f"            PAYMENT\nTotal: Php {totalPrice}.00")
    print("[1] Cash at Counter\n[2] Gcash")
    
    paymentMethods = {"1": "Cash at Counter", "2": "Gcash"}
    paymentChoice = input("Select Payment Method: ")
    paymentMethod = paymentMethods.get(paymentChoice, "Cash at Counter")
    
    return currentTray, totalPrice, paymentMethod

# final receipt (list of items in tray 
def receipt(userName, finalTray, totalPrice, paymentMethod):
    print("\n===================================")
    print("           PISAY ASAP!             ")
    print("       Official Digital Slip       ")
    print("===================================")
    print(f"Customer: {userName}")
    print("===================================")
    
    for item in finalTray:
        print(f"{item['itemName']:<20} Php {item['itemPrice']:>7.2f}")
    print("-----------------------------------")
    print(f"TOTAL AMOUNT:        Php {totalPrice:>7.2f}")
    print(f"PAYMENT METHOD:      {paymentMethod}")
    print("===================================")
    print(" Please show this to the canteen staff.")
    print("===================================\n")
    print("\n      Speedy services here in Pisay ASAP!        ")

# --- MAIN PROGRAM --- 

# welcome page
while True:
    print("\n================================\nWelcome to Pisay Asap☆!\n\n[1] Log-in\n[2] Sign-up\n[3] Close the program")
    welcomeChoice = input("\nChoice (1, 2, or 3): ")

    # Log-in
    if welcomeChoice == "1":
        status, loggedinuser = login()
        
        if status == "exit":
            continue
        
        elif status:
            break
        
        else:
            continue
            
    # Sign-up 
    elif welcomeChoice == "2":
        signUp()

    # Exit the program
    elif welcomeChoice == "3":
        print("See you again! Speedy services only here at Pisay ASAP!")
        exit()
        
    else:
        print("Invalid Choice! Please try again.")

# Proceeds to main menu after.
print(f"""
Welcome to the main menu, {loggedinuser}!
================================""")

# MAIN WELCOMING MENU
while True:
    try:
        foodchoice = input("""

================================

Choose your food Category:
[1] Snacks
[2] Meals
[3] CHECKOUT
[4] Exit

Input choice: """)

        # Snacks
        if foodchoice == "1":
            for food, price in snacks.items():
                print(f"{food}: Php {price}.00")
            
            while True:
                snackchoice = input("\nPick your Snack (or 'back'): ").title()
                if snackchoice == "Back":
                    break
                if snackchoice in snacks:
                    tray.append({"itemName": snackchoice, "itemPrice": snacks[snackchoice]})
                    print(f"Added {snackchoice} to tray!\n")

                    # Drinks add-on
                    addDrinksChoice = input("\nAdd drinks? [Y/N]: ").upper()
                    if addDrinksChoice == "Y":
                        for drinkName, drinkPrice in drinks.items(): print(f"{drinkName}: Php {drinkPrice}.00")
                        drinkadd = input("\nDrink choice: ").title()
                        if drinkadd in drinks:
                            tray.append({"itemName": drinkadd, "itemPrice": drinks[drinkadd]})
                    break
                else:
                    print(f"\nSorry! {snackchoice} is not on the menu. Please try again.\n")

        # Meals with Rice
        elif foodchoice == "2":
            for food, price in meals.items():
                print(f"{food}: Php {price}.00")
            
            while True:
                mealchoice = input("\nPick your Meal (or 'back'): ").title()
                
                if mealchoice == "Back":
                    break
                if mealchoice in meals:
                    tray.append({"itemName": mealchoice, "itemPrice": meals[mealchoice]})
                    print("Added {mealchoice} to your tray!\n")
                    
                    # Rice Selection
                    for riceName, ricePrice in rice.items():
                        print(f"{riceName}: Php {ricePrice}.00")
                    ricechoice = input("\nPick your Rice: ").title()
                    if ricechoice in rice:
                        tray.append({"itemName": f"Rice ({ricechoice})", "itemPrice": rice[ricechoice]})

                    # Drinks add-on
                    addDrinksChoice = input("\nAdd drinks? [Y/N]: ").upper()
                    if addDrinksChoice == "Y":
                        for drinkName, drinkPrice in drinks.items():
                            print(f"{drinkName}: Php {drinkPrice}.00")
                            
                        drinkadd = input("\nDrink choice: ").title()
                        if drinkadd in drinks:
                            tray.append({"itemName": drinkadd, "itemPrice": drinks[drinkadd]})
                    break
                else:
                    print("\nSorry! {mealchoice} is not on the menu. Please try again.\n")

        # Payment choice, bill calculation, final bill
        elif foodchoice == "3":
            finalTray, finalTotal, chosenMethod = payment(tray)
            if finalTray:
                receipt(loggedinuser, finalTray, finalTotal, chosenMethod)
            else:
                continue

        # exits the program
        elif foodchoice == "4":
            print("See you again! Speedy services only here at Pisay ASAP!")
            break

    except (ValueError, TypeError):
        print("\nInvalid choice. Please Try Again.")

