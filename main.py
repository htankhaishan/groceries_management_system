#''
# Logos and Menu parts 

def logo(): # Logo
    print("\n      ::::::::    :::   :::    :::::::: ")
    print("    :+:    :+:  :+:+: :+:+:  :+:    :+: ")
    print("   +:+        +:+ +:+:+ +:+ +:+         ")
    print("  :#:        +#+  +:+  +#+ +#++:++#++   ")
    print(" +#+   +#+# +#+       +#+        +#+    ")
    print("#+#    #+# #+#       #+# #+#    #+#     ")
    print("########  ###       ###  ########       \n")

def line_break():
    print("____________________________________")

def main_menu(): # Main Info
    print(" \n +++++++++ Welcome to the Groceries Store! +++++++++ \n")
    print("1) Admin Login.")
    print("2) New Customer Register.")
    print("3) Registered Customer Login.")
    print("4) Exit the System.")
    line_break()

def admin_login_logo(): # Admin Login Logo
    print(" ___    _         _        _              _      ") # Dr Pepper 
    print("| . | _| |._ _ _ <_>._ _  | |   ___  ___ <_>._ _ ")
    print("|   |/ . || ' ' || || ' | | |_ / . \/ . || || ' |")
    print("|_|_|\___||_|_|_||_||_|_| |___|\___/\_. ||_||_|_|")
    print("                                    <___'        ")

def admin_menu_logo(): # Admin Main Logo
    line_break()
    print(" ___    _         _        ___                 _ ")  
    print("| . | _| |._ _ _ <_>._ _  | . \ ___ ._ _  ___ | |")
    print("|   |/ . || ' ' || || ' | |  _/<_> || ' |/ ._>| |")
    print("|_|_|\___||_|_|_||_||_|_| |_|  <___||_|_|\___.|_|")

def admin_menu():
    line_break()
    print("\n1) Upload Groceries.")
    print("2) View All Uploaded.")
    print("3) Update or Modify Groceries Information.")
    print("4) Delete Groceries Information.")
    print("5) Search Specific Groceries Detail.")
    print("6) View All Customers Orders.")
    print("7) Search Order of Specific Customer")
    print("8) Exit to Main Menu.")
    print("0) To open Admin Menu again.")
    line_break()

def new_register_logo():
    line_break()
    print(" _ _               _ _                 ___            _        _            ")           
    print("| \ | ___  _ _ _  | | | ___ ___  _ _  | . \ ___  ___ <_> ___ _| |_ ___  _ _ ")
    print("|   |/ ._>| | | | | ' |<_-|/ '_>| '_>/|   // ._>/ . || |<_-< _| |_/ ._>| '_>")
    print("|_\_|\___.|__/_/  `___'/__/\___.|_|   |_\_ \___.\_. ||_|/__/  |_| \___.|_|  ")
    print("                                                <___'                       ")

def user_logo():
    line_break()
    print(" ___             _                          _              _      ")
    print("|  _> _ _  ___ _| |_ ___ ._ _ _  ___  _ _  | |   ___  ___ <_>._ _ ")
    print("| <__| | |<_-<  | | / . \| ' ' |/ ._>| '_> | |_ / . \/ . || || ' |")
    print("`___/`___|/__/  |_| \___/|_|_|_|\___.|_|   |___|\___/\_. ||_||_|_|")
    print("                                                     <___'        ")

def user_menu_logo(): # Customer Menu Logo
    line_break()
    print(" ___             _                          ___                 _ ")
    print("|  _> _ _  ___ _| |_ ___ ._ _ _  ___  _ _  | . \ ___ ._ _  ___ | |")
    print("| <__| | |<_-<  | | / . \| ' ' |/ ._>| '_> |  _/<_> || ' |/ ._>| |")
    print("`___/`___|/__/  |_| \___/|_|_|_|\___.|_|   |_|  <___||_|_|\___.|_|")

# ------------------------------------------------------------------------------------------------------
# Admin Parts

def admin_choice(): # Admin Menu
    while True:
        admin_menu_choice = int(input("\nShow Admin Menu with (0) or logout with (8).\nChoose one function form Admin Menu: "))
        if admin_menu_choice < 0 or admin_menu_choice > 8: # Check Error Input and loop back
            print("Input Error, Check input again.")
            continue
        elif admin_menu_choice == 1: # Update Groceries Menu
            update_groceries()
            continue
        elif admin_menu_choice == 2: # View all Groceries Menu
            view_all_groceries()
            continue
        elif admin_menu_choice == 3: # Modify or Update Groceries 
            replace_groceries()
            continue
            
        elif admin_menu_choice == 4:
            delete_groceries()
            continue

        elif admin_menu_choice == 5:
            print("Search Specific Groceries Detail")
            specific_groceries_detail()
            continue

        elif admin_menu_choice == 6:
            print("View All Customers Orders")
            view_all_cus_orders()
            continue

        elif admin_menu_choice == 7:
            print("Search Order of Specific Customer")
            specific_cus_order()
            continue
        
        elif admin_menu_choice == 0:
            admin_menu()
            continue

        else:
            print("Exit to Main Menu.")
            line_break()
            break 

def update_groceries(): # Update Groceries (1)
    while True:
        print("\n+++++ Upload Groceries +++++\n")
        
        
        #with open("groceries.txt",'r') as ga: # Check the total number of list in groceries.
        #    groc_num = str(len(ga.readlines()) + 1)
        #ga.close()
        #print("Item Number: " + groc_num)
        
        
        groc_name = input("Item Name: ").lower()
        groc_price = input("Price, RM : ").lower()
        groc_exp_date = input("Exp date, DD/MM/YYYY : ").lower()
        groc_specification = input("Specification; Premium or Normal: ").lower()
        choice = input("\nConfirm or Redo? c or r: ")
        if choice == "r":
            continue
        elif choice == "c":
            update_groceries_list = []
            #update_groceries_list.append(groc_num)
            update_groceries_list.append(groc_name)
            update_groceries_list.append(groc_price)
            update_groceries_list.append(groc_exp_date)
            update_groceries_list.append(groc_specification)
            # x = str(update_groceries_list)
            with open("groceries.txt","a+") as groceries_add:
                for ga in update_groceries_list:
                    groceries_add.write(ga)
                    groceries_add.write("\t")
                groceries_add.write("\n")
            groceries_add.close()
            choice = input("Add more or Exit? a and e: ")
            if choice == "a":
                # line_break()
                continue
            else:
                # line_break()
                break
        else:
            print("Invalid Input.")
            break

def view_all_groceries(): # View all groceries (2)
    print("\n+++++ View All Uploded +++++\n")
    print("Item:\tPrice:\n")
    with open("groceries.txt","r") as groceries_view:
        for line in groceries_view:
            line = line.rstrip()
            print(line)
        groceries_view.close()

def replace_groceries(): # Modify the groceries (3)
    print("\n+++++ Replace Groceries +++++\n")
    view_all_groceries() # View all Groceries Function 
    while True:
        with open('groceries.txt','r+') as rpg:
            rpg_filecheck = rpg.read()
            rpg_name_price = input("\nChange Item Name or Price? n, p: ") # 
            original_groceries = input("\nWhich Item Do you want to change?: ") # 
            if rpg_name_price == "n": # replace name 
                change_item_name = input("Change Item: ").lower()
                namechange = rpg_filecheck.replace(original_groceries,change_item_name)
                rpg.close()
                with open('groceries.txt','w') as rpg:
                    rpg.write(namechange)
                rpg.close()
                view_all_groceries()
                rpg_choice = input("Change Again? y or n: ").lower
                if rpg_choice == "y":
                    continue
                else:
                    break
            elif rpg_name_price == "p": # replace price
                with open('groceries.txt','r+') as rpg:
                    for anything in rpg:
                        if anything.startswith(original_groceries) :
                            anything = anything.split()
                            anyname = str(anything[1])
                            print(anyname)
                            new_price = input("New Price: ")
                            change_price = rpg_filecheck.replace(anyname,new_price)
                            with open('groceries.txt','w') as rpg:
                                rpg.write(change_price)
                rpg.close()
                view_all_groceries()
                continue
                
            else:
                print("Invalid ")
                continue


def delete_groceries(): 
    print("Delete Groceries.")
    del_groc_name = input("Delete Groc Name: ")
    with open('groceries.txt','r') as groc_del:
         for del_name in groc_del:
            old_groc_del = del_name
    groc_del.close()

    with open('groceries.txt','r') as groc_del:
        replace_groc = ""
        rep_groc = groc_del.read()
        rep_grocies = rep_groc.replace(old_groc_del,replace_groc)
    with open('groceries.txt','w') as groc_del:
        groc_del.write(rep_grocies)
        print(rep_grocies)
    groc_del.close()


def specific_groceries_detail(): # Find Specific Groceries Detail
    groc_name = str(input("Input Groceries Name: "))
    with open('groceries.txt','r') as sgd:
        for x in sgd:
            a = x.strip()
            if a.startswith(groc_name):
                print(a)
        sgd.close()

def view_all_cus_orders(): # Admin View All Customer's Orders
    print("View All Customer Ordres.")
    print("Name\t\t\tItems\t\t\tTotal\n")
    with open('orders.txt','r') as va:
        all_orders = va.read()
        print(all_orders)
        va.close()

def user_menu(): # Customer Menu
    line_break()
    print("\n1) View All Groceries Details.")
    print("2) Order and Payment.")
    print("3) View Order.")
    print("4) View Personal Information.")
    print("5) Exit to Main Menu.")
    print("0) To open Customer Menu again.")
    line_break() 

def specific_cus_order(): # Admin Could Search Orders with the name of Customers
    cus_name = str(input("Input Customer Name: "))
    with open('orders.txt','r') as sco:
        for x in sco:
            a = x.rstrip()
            if a.startswith(cus_name) :
                print(a)
        sco.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------
# New User Registering

def new_customer_register(): 
    while True:
        print("Please write Everything without space.")
        new_username = input("Choose your Username: ") # New User Name Create
        new_password = input("Choose your password: ") # New User Password
        new_phone = input("Phone Number: ") # New User Phone Number
        new_mail = input("Email: ") # New User Email 
        new_bod = input("Date of Birth (DD/MM/YYYY): ") # New User Date of Birth
        new_gender = input("Select your Gender; Male = m, Female = f : ") # New User Gender
        new_ID =  input("National ID: ")
        print("\n")
        new_user_choice = str(input("Please check the information again.\nSubmit,Change or Exit; s,c or e: "))            
        line_break()
        if new_user_choice == "c":
            continue
        elif new_user_choice == "s":
            with open("users.txt","a") as add_user:
                add_user_list = []
                add_user_list.append(new_username)
                add_user_list.append(new_password)
                add_user_list.append(new_phone)
                add_user_list.append(new_mail)
                add_user_list.append(new_bod)
                add_user_list.append(new_gender)
                add_user_list.append(new_ID)
                for au in add_user_list:
                    add_user.write(au)
                    add_user.write("\t")
                add_user.write("\n")
            add_user.close()
            print("\nSuccessfully Register new user. You can login form Register Customer Login Page.\n")
            line_break()
            back = input("Exit to Main Menu or Add New Account? e or a: ")
            if back == "e":
                break
            elif back == "a":
                continue
            else:
                break 
        elif new_user_choice == "e":
            break
        else:
            new_user_exit = print("Input error.")
            continue
        continue

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Customer Part

def user_choice(): # User Panel
    while True:
        username = str.lower(input("User Name: ")) # User Name
        password = str.lower(input("Password: ")) # Password
        with open('users.txt','r') as uc:
            filecheck = uc.readlines()
            status = True
            for user_filecheck in filecheck:
                name_check = user_filecheck.split('\t')[0]
                pass_check = user_filecheck.split('\t')[1].strip()
                if name_check == username and pass_check == password:
                    uc.close()
                    print("success")
                    user_panel(username)
                    return True
                #user_panel()
                else:
                    uc.close()
                    status = False
            if status == False:
                print("Usename or Password Invalid.")

def user_panel(username):
    user_menu()
    while True:
        user_menu_choice = input("\nInput number: ")
        if user_menu_choice == '1': 
            print("View All Groceries Details.")
            view_all_groceries()
            # line_break()
            print("Input 0 to show User Menu: ")
            continue
        elif user_menu_choice == '2':
            print("Order and Payment.")
            cus_order_payment()
            continue
        elif user_menu_choice == '3':
            print("View Order.")
            view_own_order(username)
            continue
        elif user_menu_choice == '4':
            print("View Personal Information.")
            view_own_info(username)
            continue
        elif user_menu_choice == '5':
            print("Exit to Main Menu.")
            break
        else:
            user_menu()
            continue

def cus_order_payment(): # Customer Order and Payment
    view_all_groceries()
    total_cost = 0
    cus_total_cost = []
    num_groceries = []
    total_num_groc = int(input("How many groceries do you want to buy?: "))
    for i in range(total_num_groc):
        order_item = str(input("Input Item: "))
        num_groceries.append(order_item)
        with open('groceries.txt','r') as cus_order_items:
            for line in cus_order_items:
                if line.startswith(order_item):
                    cost = line.split()
                    choosen_cost = float(cost[1])
                    cus_total_cost.append(choosen_cost)
                    total_cost = sum(cus_total_cost)
            cus_order_items.close()
        print(total_cost)
    order_item_list = []
    customer_name = input("username: ")
    order_item_names = str(','.join(num_groceries))
    order_item_list.append(customer_name)
    order_item_list.append(order_item_names)
    order_item_list.append(str(total_cost))
    with open('orders.txt','a') as cus_order_items:
        for order_data in order_item_list:    
            cus_order_items.write(order_data)
            cus_order_items.write('\t')
        cus_order_items.write("\n")
    cus_order_items.close()

def view_own_order(username):
    with open('orders.txt','r') as voo:
        for x in voo:
            a = x.strip()
            if a.startswith(username):
                print(a)
        voo.close()

def view_own_info(username):
    with open('users.txt','r') as voi:
        print("Name\tPass\tPhone\tMail\tBOD\tGender\tID")
        for x in voi:
            a = x.rstrip()
            if a.startswith(username):
                print(a)
        voi.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------

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
        admin_login_logo()
        admin_username = str(input("Admin User Name: ")) # Admin User Name
        admin_password = input("Admin Password: ") # Admin Password
        with open("admin.txt","r") as check_admin:
            for word in check_admin:
                check_admin = word.rsplit()
                if admin_username != check_admin[0] or admin_password != check_admin[1]: # Adimn username false and pass true               
                    print("\nInvalid Username or Password.\n")
                    line_break()
                    back = str(input("Try Again or Exit System? t or e: ")) 
                    if back == "t":
                        continue # Loop back to Admin Login
                    else:
                        break # Back to Main Menu Function.
                elif admin_username == check_admin[0] and admin_password == check_admin[1]: # To Admin Main Menu
                    line_break()
                    print("Login Successfully.")
                    # --------------------------------------------------------------------------------------------
                    admin_menu_logo()
                    admin_menu() # Admin Panal Menu
                    admin_choice()
        continue
                # check_admin.close()
                  
# ------------------------------------------------------------------------------------------------------
# New Customer Registeration 
    elif main_login == 2:# New Customers
        line_break()
        new_register_logo()
        new_customer_register()

# ------------------------------------------------------------------------------------------------------
# Customer Login
    elif main_login == 3: # Register Customer Login
        line_break()
        user_choice()
    # line_break()
        #-----------
        
        #----------
# ------------------------------------------------------------------------------------------------------
    else: # Registered Login
        print("+++++ Exit System ++++++")
        break
#'''
