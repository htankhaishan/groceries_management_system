def logo(): # Logo
    print("\n      ::::::::    :::   :::    :::::::: ")
    print("    :+:    :+:  :+:+: :+:+:  :+:    :+: ")
    print("   +:+        +:+ +:+:+ +:+ +:+         ")
    print("  :#:        +#+  +:+  +#+ +#++:++#++   ")
    print(" +#+   +#+# +#+       +#+        +#+    ")
    print("#+#    #+# #+#       #+# #+#    #+#     ")
    print("########  ###       ###  ########       ")

def line_break():
    print("____________________________________")

def main_menu(): # Main Info
    print(" \n +++++++++ Welcome to the Groceries Store! +++++++++ \n")
    print("1) Admin Login.")
    print("2) New Customer Login.")
    print("3) Registered Customer Login.")
    print("4) Exit the System.")
    line_break()

def admin_menu(): # Admin Main Menu
    line_break()
    print(" \n +++++++++ Admin Pannel +++++++++ \n")
    print("1) Upload Groceries.")
    print("2) View All Upladed.")
    print("3) Update or Modify Groceries Information.")
    print("4) Delete Groceries Information.")
    print("5) Search Specific Groceries Detail.")
    print("6) View All Customers Orders.")
    print("7) Search Order of Specific Customer")
    print("8) Exit to Main Menu.")
    line_break()

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# Main Program 
while True:
    logo()
    main_menu()
    main_login = int(input("What would you like to do? Write the number: "))
    if main_login < 0 or main_login > 4: # Check Error Input
        print("Input Error, Check input again.")
        line_break()
        continue

# ------------------------------------------------------------------------------------------------------
# Admin Panal
    elif main_login == 1: # Admin Login
        line_break()
        print("Admin Login")
        admin_username = str(input("Admin User Name: ")) # Admin User Name
        admin_password = input("Admin Password: ") # Admin Password
        if admin_username == "admin" and admin_password == "admin": # To Admin Main Menu
            print("Login Successfully.")
            # --------------------------------------------------------------------------------------------
            admin_menu()
            while True:
                admin_menu_choice = int(input("Choose one function: "))
                if admin_menu_choice < 0 or admin_menu_choice > 8: # Check Error Input
                    print("Input Error, Check input again.")
                    line_break()

                elif admin_menu_choice == 1:
                    print("Upload Groceries.")
                    continue

                elif admin_menu_choice == 2:
                    print("View All Upladed.")
                    admin_menu()
                
                elif admin_menu_choice == 3:
                    print("Update or Modify Groceries Information.")
                    admin_menu()
                    
                elif admin_menu_choice == 4:
                    print("Delete Groceries Information")
                    admin_menu()

                elif admin_menu_choice == 5:
                    print("Search Specific Groceries Detail")
                    admin_menu()

                elif admin_menu_choice == 6:
                    print("View All Customers Orders")
                    admin_menu()

                elif admin_menu_choice == 7:
                    print("Search Order of Specific Customer")
                    admin_menu()

                elif admin_menu_choice == 8:
                    print("Exit to Main Menu.")
                    main_menu()

                else:
                    print("Invalid Output.")
                break
            # --------------------------------------------------------------------------------------------
        
        else: # Loop back to the Main Menu                
            print("\nWrong Username or Password. \nLogin form Main Menu Again.")
            line_break()
            back = str(input("Do you want to go Main Menu or Exit? m or e: ")) # Back to Main Menu Function.
            if back == "e":
                break
            else:
                main_menu()
                line_break()

# ------------------------------------------------------------------------------------------------------
# New Customer Registeration 
    elif main_login == 2:# New Customers
        line_break()
        print("New Customer Register")
        new_username = str(input("Choose your Username: ")) # New User Name Create
        new_password = input("Choose your password: ") # New User Password
        print("Invilid Number.")
        back = str(input("Do you want to go to main menu or quit? y or n: ")) # Back to Main Menu Function.
        if back == "y":
            continue
        elif back == "n":
            break
        else:
            print("Invalid Input.")
            continue

# ------------------------------------------------------------------------------------------------------
# Customer Login
    elif main_login == 3: # Register Customer Login
        line_break()
        print("Customer Login")
        old_username = str(input("User Name: ")) # Register Customer Username
        old_password = input("Choose your password: ") # Register Customer Password
        back = str(input("Do you want to go to main menu or quit? y or n: ")) # Back to Main Menu Function.
        if back == "y":
            continue
        elif back == "n":
            break
        else:
            print("Invalid Input.")
            continue

# ------------------------------------------------------------------------------------------------------

    else: # Registered Login
        print("Exit System.")
        break