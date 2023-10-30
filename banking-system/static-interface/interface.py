from customer import Customer
from bank import Bank
from account import SavingsAccount, CheckingAccount, JointAccount
import os
import time
import datetime

today = datetime.date.today()
current_time = datetime.datetime.now()
year = today.year

class Interface:
    __savings = Bank.get_list_savingsAccounts()
    __checking = Bank.get_list_checkingAccounts()
    __joint = Bank.get_list_jointAccounts()
    __customers = Bank.get_list_customers()

    @staticmethod
    def create_account():
        running = True
        
        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("CREATE AN ACCOUNT")
            customer = Interface.enter_credential()

            ### Check if the username exists in the system ###
            existing_username = False
            for existing_customer in Interface.__customers:
                if existing_customer.get_username() == customer.get_username():
                    existing_username = True
                    break
            
            if existing_username:
                print("\nERROR: Username already exists. Please choose a different username.")
                print("Press [Enter] to continue.")
                input()
            else:
                choice = input("\nDo you want to create this account (Y/n): ")
                if choice.upper() == 'Y':
                    print("\nCreating account...")
                    Interface.__customers.append(customer)
                    time.sleep(3)
                    print("Account Created!")
                    time.sleep(1)
                    Interface.process(customer)
                    running = False
                elif choice.lower() == 'n':
                    del customer
                    print("\nDeleting inputs...")
                    time.sleep(3)
                    running = False
                else:
                    print("ERROR: Invalid input. Press [Enter] to continue.")
                    input()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    @staticmethod
    def login():
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("LOG IN\n")
            print("[1] Log-In\n[2] Forgot Password\n[3] Back")
            
            choice = input("\nEnter Choice: ")
            if choice == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("FooBar's Bank")
                print(f"{today:%A, %B %d, %Y}\n")
                print("LOG IN\n")
                print("Enter Credentials")
                customer_username = input("Username: ")
                customer_password = input("Password: ")

                for customer in Interface.__customers:
                    username = customer.get_username()
                    password = customer.get_password()
                    if username == customer_username and password == customer_password:
                        print("\nLogging in...")
                        time.sleep(3)
                        print("Log in successful!")
                        time.sleep(1)
                        Interface.login_menu(customer)
                        running = False
                        break
                else:
                    print("\nLogging in...")
                    time.sleep(3)
                    print("Login Failed. Invalid credentials.")
                    time.sleep(1)
                    Interface.login()
                    running = False
            elif choice == '2':
               Interface.forgot_password()
            elif choice == '3':
                running = False
            else:
                print("ERROR: Invalid input. Press [Enter] to continue.")
                input()

    @staticmethod
    def login_menu(customer):
        user_verified = customer.get_isUserVerified()
        running = True
        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("What would you like to do?\n")
            print("[1] Open an account\n[2] View Profile\n[3] Check Balance\n[4] Deposit\n[5] Withdraw\n[6] Log out")
            choice = input("\nEnter choice: ")
            
            ##### Open an account #####
            if choice == '1':
                Interface.open_account(customer)
                running = False
            
            ##### View Profile ######
            elif choice == '2':
                Interface.process(customer)

            ##### Check Balance #####
            elif choice == '3':
                if user_verified == True:
                    Interface.checkBalance(customer)
                    running = False
                else:
                    print("\nPlease open an account.")
                    print("Press [Enter] to continue.")
                    input()

            ##### Deposit #####
            elif choice == '4':
                if user_verified == True:
                    Interface.deposit(customer)
                    running = False
                else:
                    print("\nPlease open an account.")
                    print("Press [Enter] to continue.")
                    input()

            ##### Withdraw #####
            elif choice == '5':
                if user_verified == True:
                    Interface.withdraw(customer)
                    running = False
                else:
                    print("\nPlease open an account.")
                    print("Press [Enter] to continue.")
                    input()

            ##### Log Out #####
            elif choice == '6':
                print("Logging out...")
                time.sleep(3)
                running = False
            else:
                print("ERROR: Invalid input. Press [Enter] to continue.")
                input()

    @staticmethod
    def open_account(customer):
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("[OPEN ACCOUNT]\n")
            print("Type of Account\n")
            print("[1] Savings Account\n[2] Checking Accont\n[3] Joint Account\n[4] Back")
            choice = input("\nEnter Choice: ")

            ###### Savings Account ######
            if choice == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                account = SavingsAccount(f"{year}-1{len(Interface.__savings) + 1}")
                print("FooBar's Bank")
                print(f"{today:%A, %B %d, %Y}\n")
                print("[OPEN ACCOUNT]\n")
                print("Conditions in opening Savings Account")
                print("- Initial deposit of PHP 500.")
                print("- Maintaining balance of PHP 2000.")
                print("- Withdrawal limit of PHP 20000 per day.")
                print("- Account will be closed if the balance falls to PHP 0.")
                accept_choice = input("\nDo you accept? (Y/n): ")
                if accept_choice.upper() == 'Y':
                    account_balance = int(account.get_accountBalance())
                    initial_deposit = int(input("\nEnter Initial Deposit: "))
                    if initial_deposit >= 500:
                        account_balance += initial_deposit
                        account.set_accountBalance(account_balance)
                        account.set_open()
                        account.get_accountHolders().append(customer)
                        customer.add_account(account)
                        customer.set_isUserVerified()
                        Interface.__savings.append(account)
                        print("\nOpening account...")
                        time.sleep(3)
                        print("Account made!")
                        time.sleep(1)
                        Interface.login_menu(customer)
                        running = False
                    else:
                        print("ERROR: Initial depoit must be PHP 500.")
                        print("Press [Enter] to continue.")
                        input()
                elif accept_choice.lower() == 'n':
                    running = False
                else:
                    print("ERROR: Invalid input. Press [Enter] to continue.")
                    input()
            
            ##### Checking Account #####
            elif choice == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                account = CheckingAccount(f"{year}-2{len(Interface.__checking) + 1}")
                print("FooBar's Bank")
                print(f"{today:%A, %B %d, %Y}\n")
                print("[OPEN ACCOUNT]\n")
                print("Conditions in opening Checking Account")
                print("- Initial deposit of PHP 25000.")
                print("- No withdrawal limit per day.")
                print("- Account will be closed if the balance falls to PHP 0.")
                accept_choice = input("\nDo you accept? (Y/n): ")
                if accept_choice.upper() == 'Y':
                    account_balance = int(account.get_accountBalance())
                    initial_deposit = int(input("\nEnter Initial Deposit: "))
                    if initial_deposit >= 25000:
                        account_balance += initial_deposit
                        account.set_accountBalance(account_balance)
                        account.set_open()
                        account.get_accountHolders().append(customer)
                        customer.add_account(account)
                        customer.set_isUserVerified()
                        Interface.__checking.append(account)
                        print("\nOpening account...")
                        time.sleep(3)
                        print("Account made!")
                        time.sleep(1)
                        Interface.login_menu(customer)
                        running = False
                    else:
                        print("ERROR: Initial depoit must be PHP 25000.")
                        print("Press [Enter] to continue.")
                        input()
                elif accept_choice.lower() == 'n':
                    running = False
                else:
                    print("ERROR: Invalid input. Press [Enter] to continue.")
                    input()
            
            ##### Joint Account #####
            elif choice == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                account = JointAccount(f"{year}-3{len(Interface.__joint) + 1}")
                print("FooBar's Bank")
                print(f"{today:%A, %B %d, %Y}\n")
                print("[OPEN ACCOUNT]\n")
                print("Conditions in opening Joint Account")
                print("- Account should be shared to two or more customers.")
                print("- Initial deposit of 50, 000 PHP")
                print("- Withdrawals could be made by either of the account holder")
                print("- Account will be closed if the balance falls to PHP 0.")

                accept_choice = input("\nDo you accept? (Y/n): ")
                if accept_choice.upper() == 'Y':
                    holders = account.get_accountHolders()
                    customer_id = input("Enter ID of joint holder: ")
                    joint_holder = None
                    for existing_customer in Interface.__customers:
                        if existing_customer.get_id() == customer_id:
                            joint_holder = existing_customer
                            account.add_customer(joint_holder)
                            joint_holder.add_account(account)
                            joint_holder.set_isUserVerified()
                            break
                    if joint_holder is not None:
                        holders.append(joint_holder)
                        account_balance = int(account.get_accountBalance())
                        initial_deposit = int(input("\nEnter initial deposit: "))
                        if initial_deposit >= 50000:
                            account_balance += initial_deposit
                            account.set_accountBalance(account_balance)
                            account.set_open()
                            customer.add_account(account)
                            customer.set_isUserVerified()
                            Interface.__joint.append(account)
                            print("\nOpening account...")
                            time.sleep(3)
                            print("Account made!")
                            time.sleep(1)
                            Interface.login_menu(customer)
                            running = False
                        else:
                            print("Invalid User ID")
                    if len(holders) < 2:
                        print('Joint account must contain two or more holders')
                        running = False
                elif accept_choice.lower() == 'n':
                    running = False
                else:
                    print("ERROR: Invalid input. Press [Enter] to continue.")
                    input()
            
            ##### Back #####
            elif choice == '4':
                Interface.login_menu(customer)
                running = False

            else:
                print("ERROR: Invalid input. Press [Enter] to continue.")
                input()

    @staticmethod
    def checkBalance(customer):
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("CHECK BALANCE\n")
            print("[1] All Accounts\n[2] Specific Account\n[3] Back")
            choice_input = input("\nEnter choice: ")
            
            if choice_input == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("FooBar's Bank")
                print(f"{today:%A, %B %d, %Y}\n")
                print("CHECK BALANCE\n")
                accounts = customer.get_list_of_accounts()
                if len(accounts) == 0:
                    print("No accounts enrolled!")
                else:
                    for account in accounts:
                        print("Accounts and Balances")
                        print(f"Account Id: {account.get_id()}")
                        print(f"Account Type: {account.get_accountType()}")
                        print(f"Account Balance: {account.get_accountBalance()}")
                        print(f"Account statis: {account.get_status()}\n")

            elif choice_input == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("FooBar's Bank")
                print(f"{today:%A, %B %d, %Y}\n")
                print("CHECK BALANCE\n")
                input_id = input("Enter account id: ")
                accounts = customer.get_list_of_accounts()
                found = False
                for account in accounts:
                    if account.get_id() == input_id:
                        print("Account and Balance")
                        print(f"Account Id: {account.get_id()}")
                        print(f"Account Type: {account.get_accountType()}")
                        print(f"Account Balance: {account.get_accountBalance()}")
                        print(f"Account statis: {account.get_status()}\n")
                        found = True
                        break
                
                if not found:
                    print(f"Account {input_id} was not found!")
                    print("Please check your accounts")
                    time.sleep(1)

            elif choice == '3':
                running = False

            print("\n[1] Back")
            choice = input("\nEnter Choice: ")

            if choice == '1':
                Interface.login_menu(customer)
                running = False
            else:
                print("ERROR: Invalid input. Press [Enter] to continue")
                input()
    
    @staticmethod
    def deposit(customer):
        running = True
        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("DEPOSIT\n")
            input_id = input("Enter account id: ")
            amount_input = input("Enter amount: ")
            found = False
            accounts = customer.get_list_of_accounts()
            for account in accounts:
                if account.get_id() == input_id:
                    current_balance = int(account.get_accountBalance())
                    current_balance += int(amount_input)
                    account.set_accountBalance(current_balance)
                    found = True
                    print("\nDepositing...")
                    time.sleep(3)
                    print("Amount deposited!")
                    time.sleep(1)
                    Interface.login_menu(customer)
                    running = False
                    break
            
            if not found:
                print("\nDepositing...")
                time.sleep(3)
                print(f"Account {input_id} was not found!")
                print("Please check your accounts")
                time.sleep(1)
                Interface.login_menu(customer)
                running = False

    @staticmethod
    def withdraw(customer):
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("WITHDRAWAL\n")
            input_id = input("Enter account id: ")
            amount_input = input("Enter amount: ")
            found = False
            accounts = customer.get_list_of_accounts()
            for account in accounts:
                if account.get_id() == input_id:
                    current_balance = int(account.get_accountBalance())
                    amount = int(amount_input)
                    if amount <= current_balance:
                        current_balance -= int(amount_input)
                        account.set_accountBalance(current_balance)
                        found = True
                        print("\nWithdrawing...")
                        time.sleep(3)
                        print("Amount withdrawed!")
                        if current_balance == 0:
                            Interface.close_account(customer, account)
                        time.sleep(1)
                        Interface.login_menu(customer)
                        running = False
                        break
                    else:
                        print("\nWithdrawing...")
                        time.sleep(3)
                        print("Insufficient Balance!")
                        time.sleep(1)
                        Interface.login_menu(customer)
                        running = False
            
            if not found:
                print("\Withdrawing...")
                time.sleep(3)
                print(f"Account {input_id} was not found!")
                print("Please check your accounts")
                time.sleep(1)
                Interface.login_menu(customer)
                running = False

    @staticmethod
    def close_account(customer, account):
        account_type = account.get_accountType()
        if account_type == 'Savings Account':
            account.set_close()
            customer.get_list_of_accounts().remove(account)
            customer.get_closed_accounts().append(account)
        elif account_type == 'Checking Account':
            account.set_close()
            customer.get_list_of_accounts().remove(account)
            customer.get_closed_accounts().append(account)
        elif account_type == 'Joint Account':
            account.set_close()
            customer.get_list_of_accounts().remove(account)
            customer.get_closed_accounts().append(account)
        
        print(f"Account {account.get_id()} has been closed, it reaches '0' balance")
        time.sleep(3)


    @staticmethod
    def enter_credential():
        id = f"{year}-0{len(Interface.__customers) + 1}"
        print("\n[ACCOUNT CREDENTIAL]")
        username = input("Username: ")
        password = input("Password: ")

        print("\n[PERSONAL INFORMATION]")
        lastName = input("Last Name: ")
        givenName = input("Given Name: ")
        middleName = input("Middle Name: ")
        full_name = f"{lastName}, {givenName} {middleName}"

        print("\n[ADDRESS INFORMATION]")
        house_number = input("House Number: ")
        street = input("Street: ")
        subdivision = input("Subdivision: ")
        barangay = input("Barangay: ")
        municipality = input("Municipality: ")
        state = input("Province: ")
        zip_code = input("Zip Code: ")
        full_address = f"{house_number}, {street}, {subdivision}, {barangay}, {municipality}, {state}, {zip_code}"

        print("\n[OTHER INFORMATION]")
        birth_date = input("Birth Date: ")
        gender = input("Gender: ")
        nationality = input("Nationality: ")
        cp_number = input("Cellphone Number: ")
        emaill_address = input("Email Address: ")
        salary =  input("Salary: ")

        customer = Customer(id, full_name, full_address, birth_date, gender, nationality, cp_number, emaill_address, salary, username, password)
        return customer
    
    @staticmethod
    def process(customer):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Customer Data")
        print(f"ID: {customer.get_id()}")
        print(f"Name: {customer.get_name()}")
        print(f"Address: {customer.get_address()}")
        print(f"Birth Date: {customer.get_birth_date()}")
        print(f"Gender: {customer.get_gender()}")
        print(f"Nationality: {customer.get_nationality()}")
        print(f"Cellphone Number: {customer.get_cp_number()}")
        print(f"Email Address: {customer.get_email_address()}")
        print(f"Salary: {customer.get_salary()}")
        print(f"Username: {customer.get_username()}")
        print(f"Password: {customer.get_password()}")
        print(f"Verified: {customer.get_isUserVerified()}")
        #print(f"Accounts: {customer.get_list_of_accounts()}")
        time.sleep(3)

    @staticmethod
    def forgot_password():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("FooBar's Bank")
        print(f"{today:%A, %B %d, %Y}\n")
        print("LOG IN\n")
        print("Try to remember your login credentials!")
        print("Press [Enter] to continue")
        input()

    @staticmethod
    def show_menu():
        running = True

        while running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FooBar's Bank")
            print(f"{today:%A, %B %d, %Y}\n")
            print("[1] Create account\n[2] Log In\n[3] Exit")

            choice = input("\nEnter Choice: ")

            if choice == '1':
                Interface.create_account()
            elif choice == '2':
                Interface.login()
            elif choice == '3':
                print("Exiting Program...")
                time.sleep(3)
                running = False
            else:
                print("ERROR: Invalid input. Press [Enter] to continue")
                input()