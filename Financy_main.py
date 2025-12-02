#Global Variables
from datetime import datetime #imports datetime function
from tabulate import tabulate #imports tabulate function
import financy_classes #imports classes from another file


def login(): #This function is used for simple user authentication
    user = { #This dictionary stores the lists of users that are allowed to log into the Financy System
        'umar': 'umar@1234',
        'yovin': 'yovin@1234'
    }

    while True: #This loop checks for the correct username and password from the user dictionary
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if username_input in user and password_input in user[username_input]:
            print(f"Welcome back {username_input.capitalize()}!")
            break
        else:
            print("Username or password is incorrect")
################################################################################################
def main_menu(): #This is the main menu of Financy, it is where users can navigate to the different pages and sub-menus
    print("---Main Menu---")
    print(f"Current balance: ${financy_classes.Transactions.balance}") #Displays the balance at any given moment or time
    print("1. Income")
    print("2. Expense")
    print("3. Account Analytics")
    print("4. Delete Transactions")
    print("5. Exit")
    while True: #This loop checks for correct user choice input
        main_menu_choice = input("Enter your choice: ")
        if main_menu_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if main_menu_choice == '1':
        income_menu()
    elif main_menu_choice == '2':
        expense_menu()
    elif main_menu_choice == '3':
        account_analytics_menu()
    elif main_menu_choice == '4':
        remove_transactions_menu()
    elif main_menu_choice == '5' or main_menu_choice == 'exit':
        print("Thank you for using Financy.")
        exit()
################################################################################################
def income_menu(): # This is the income submenu, it is where all the options regarding income are hosted
    print("---------------")
    print("Welcome to the Income Menu")
    print("---------------")
    print("1. Add Income")
    print("2. View Income History")
    print("3. Exit to Main Menu")
    while True: #This loop checks for correct user choice input
        income_choice = input("Enter your choice: ")
        if income_choice not in ('1', '2', '3','exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if income_choice == '1':
        print("---------------")
        add_income() #redirects to this function
    elif income_choice == '2':
        print("---------------")
        show_income_table(Analytics=False) #This calls the show_income_table function. The parameters are set so that the function returns the user to a different menu.
        #This enables us to use the same function for different use-cases. Keeping it modular
    elif income_choice == '3' or income_choice == 'exit':
        print("Returning to Main Menu")
    return main_menu() #When the function ends, it will return the user back to the main menu
################################################################################################
def expense_menu(): #This is the expense menu, it is where all options regarding expenses are hosted
    print("---------------")
    print("Welcome to the Expense Menu")
    print("---------------")
    print("1. Add Expense")
    print("2. View Expense History")
    print("3. Exit to Main Menu")
    while True: #This loop checks for correct user choice input
        expense_choice = input("Enter your choice: ").lower()
        if expense_choice not in ('1', '2', '3', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if expense_choice == '1':
        print("---------------")
        add_expense()
    elif expense_choice == '2':
        print("---------------")
        show_expense_table(AnalyticsExpense=False) #This calls the show_expense_table function. The parameters are set so that the function returns the user to a different menu.
        #This enables us to use the same function for different use-cases. Keeping it modular
    elif expense_choice == '3' or expense_choice == 'exit':
        print("Returning to Main Menu")
    return main_menu() #When the function ends, it will return the user back to the main menu
################################################################################################
def account_analytics_menu(): #This is the Account Analytics Menu, its where all the account analytics are hosted
    print("---------------")
    print("Welcome to the Account Analytics Menu")
    print("---------------")
    print(f"Current balance: ${financy_classes.Transactions.balance}")
    print("1. View Total Income History")
    print("2. View Total Expense History")
    print("3. View Account Balance")
    print("4. View Per-Category Spending History")
    print("5. Exit to Main Menu")
    while True: #This loop checks for correct user choice input
        account_analytics_choice = input("Enter your choice: ")
        if account_analytics_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if account_analytics_choice == '1':
        print("---------------")
        show_income_table(Analytics=True) #This calls the show_income_table function. The parameters are set so that the function returns the user to a different menu.
        #This enables us to use the same function for different use-cases. Keeping it modular
    elif account_analytics_choice == '2':
        print("---------------")
        show_expense_table(AnalyticsExpense=True) #This calls the show_expense_table function. The parameters are set so that the function returns the user to a different menu.
        #This enables us to use the same function for different use-cases. Keeping it modular
    elif account_analytics_choice == '3':
        print("---------------")
        print(f"Your current balance: ${financy_classes.Transactions.balance}")

    elif account_analytics_choice == '4':
        print("---------------")
        per_category_spending_history("Food") #Calls the per_category_spending_history function. The parameter calls for a specific category
        per_category_spending_history("Rent")
        per_category_spending_history("Entertainment")
        per_category_spending_history("Clothing")
        per_category_spending_history("Loan")
        per_category_spending_history("Other")
    elif account_analytics_choice == '5' or account_analytics_choice == 'exit':
        print("Returning to Main Menu.")
    return main_menu()
##################################################################################################
def add_income():
    print(f"Current balance: ${financy_classes.Transactions.balance}")
    while True: #This loops make sure the user enters a valid input
        income_amount = input("Enter your income ($): ")
        try:
            income_amount = float(income_amount) #If the input cannot be made into a float it will reprompt the user for an input
            if income_amount <= 0: #This checks for negative inputs, and if the user enters a negative valid, they will be prompted to enter another valid
                print("Invalid income. Please try again. Please enter only positive numbers.")
            else:
                break
        except ValueError:
            print("Invalid income. Please try again. Please enter only numbers.")
    while True:
        income_date = input("Enter the date of your income (DD/MM/YYYY), leave blank for today's date: ").strip() #This part enables the user to choose to enter a date for the transaction or lets the system autofill the current date. This aims at making the user experience more seemless
        if income_date == "":
            income_date = datetime.today().strftime("%d/%m/%Y")
            print(f"Using today's date: {income_date}")
            break
        try:
            datetime.strptime(income_date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date. Please try again (DD/MM/YYYY).")
    income_description = input("Enter your income description: ") #This prompts the user to enter a description for the income
    new_income = financy_classes.Income("Income", income_amount,"Income", income_description, income_date) # Here we are creating an object for that will contain this income entry. This will automcatically be appended to the transactions_registry in the Transactions class. Refer to the Transactions class for more details
    #Since the type and category are by default income, they have been pre-defined for better user experience
    financy_classes.Transactions.balance += income_amount #This function adds the income to the balance
    print(f"Your new balance is ${financy_classes.Transactions.balance}")
    return income_menu() #Once the income is recorded it, the function redirects the user to the income menu
###################################################################################################
def add_expense():
    valid_expenses = ['Food', 'Rent', 'Entertainment', 'Clothing', 'Loan', 'Other'] #This list contains a number of valid expense categories that we have pre-defined for convenience.
    print(f"Current balance: ${financy_classes.Transactions.balance}")
    while True: #Looks checks for correct user input - similar loop to the one used for income
        expense_amount = input("Enter your expense ($): ")
        try:
            expense_amount = float(expense_amount)
            if expense_amount <= 0:
                print("Invalid expense. Please try again. Please enter only positive numbers.")
            else:
                break
        except ValueError:
            print("Invalid expense. Please try again. Please enter only numbers.")
    while True: #This part enables the user to choose to enter a date for the transaction or lets the system autofill the current date. This aims at making the user experience more seemless
        expense_date = input("Enter the date of your income (DD/MM/YYYY), leave blank for today's date: ").strip()
        if expense_date == "".strip():
            expense_date = datetime.today().strftime("%d/%m/%Y")
            print(f"Using today's date: {expense_date}")
            break
        try:
            datetime.strptime(expense_date, "%d/%m/%Y") #This checks for date format
            break
        except ValueError:
            print("Invalid date. Please try again (DD/MM/YYYY).")
    expense_description = input("Enter your expense description: ") # prompts the user to add a description to the expense

    while True:
        print("Enter a category from the following: Food, Rent, Entertainment, Clothing, Loan and Other")
        expense_category = input("Enter your expense category: ").capitalize() #Capitalize is to make sure the input is as intended for us to verify with the list
        if expense_category not in valid_expenses:
            print("Invalid choice. Please enter a valid category such as Food, Rent, Entertainment, Clothing, Loan and Other") # validates the input with the valid categories
        else:
            break

    new_expense = financy_classes.Expenses("Expenses", expense_amount,expense_category, expense_description, expense_date) # Here we are creating an object for that will contain this expense entry. This will automcatically be appended to the transactions_registry in the Transactions class. Refer to the Transactions class for more details
    financy_classes.Transactions.balance -= expense_amount
    print(f"Your new balance is ${financy_classes.Transactions.balance}")
    return expense_menu()
####################################################################################################
def show_income_table(Analytics):
    incomes = [t for t in financy_classes.Transactions.transactions_registry if t.ttype == "Income"] #This list comprehension enables us to filter the Transactions_registry for Income
    income_table = []
    for t in incomes: # We store the transactions into the income_table list as a dictionary so that we can display it properly using the tabulate function
        income_table.append({
            "ID": t.id,
            "Type": "Income",
            "Amount ($)": t.amount,
            "Category": "Income",
            "Description": t.description,
            "Date": t.date
        })
    sum_of_income = sum(t.amount for t in incomes) #This calculates the total sum of all income recorded and filtered into the incomes list
    income_table.append({ #Here we append it to the income_table so that it has a row of its own. This makes it so that this record is only displayed once and not on each row on the last column.
        "Sum of Income ($)": sum_of_income,
    })

    if not incomes:
        print("No transactions were found.")
        return income_menu()
    else:
        print(tabulate(income_table, headers="keys", tablefmt="fancy_grid"))

    if Analytics: #This statement makes the function more modular and enables us to use it in the Income Menu and Account Analytics Menu
        return account_analytics_menu()
    else:
        return income_menu()
#####################################################################################################
def show_expense_table(AnalyticsExpense): #This is a replica of the above function, please refer to it for comments on the logic of each statement.
    expenses = [t for t in financy_classes.Transactions.transactions_registry if t.ttype == "Expense"]
    expense_table = []
    for t in expenses:
        expense_table.append({
            "ID": t.id,
            "Type": "Expense",
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
        })
    sum_of_expenses = sum(t.amount for t in expenses)
    expense_table.append({
        "Sum of Expenses ($)": sum_of_expenses,
    })

    if not expense_table:
        print("No transactions were found.")
        return expense_menu()
    else:
        print(tabulate(expense_table, headers="keys", tablefmt="fancy_grid"))

    if AnalyticsExpense:
        return account_analytics_menu()
    else:
        return expense_menu()
####################################################################################################
def per_category_spending_history(category): #This module enables us to display transactions from each category Separately.
    sp_category =[t for t in financy_classes.Transactions.transactions_registry if t.category == category] #This list comprehension filters the transactions registry for transactions of a specific category as stated in the function parameters.

    sp_category_history = [] # This list stores a dictionary that enables the tabulate function to display everything properly.
    for t in sp_category:
        sp_category_history.append({
            "ID": t.id,
            "Type": t.ttype,
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
        })
    if sp_category_history == []:
        print(f"No transactions found for category: {category}.")
    else:
        print(f"Please find your spending history for {category} below.")
        print("____________________________________________________________________")
        print(tabulate(sp_category_history, headers="keys", tablefmt="fancy_grid"))
############################################################## ######################################
def remove_transactions_menu(): #This section enables users to delete certain transactions
    all_transactions_filter = [t for t in financy_classes.Transactions.transactions_registry]
    all_transactions = []
    for t in all_transactions_filter:
        all_transactions.append({
            "ID": t.id,
            "Type": t.ttype,
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
    })
#The above lines of code is used to create a dictionary out of all the transactions in registry to be displayed below
    if all_transactions == []:
        print("____________________________________________________________________")
        print("No transactions to delete.")
        print("Returning to Main Menu.")
        print("____________________________________________________________________")
        return main_menu()
    else:
        print("Welcome to the transactions Deleting Tool!")
        print("____________________________________________________________________")
        print(tabulate(all_transactions, headers="keys", tablefmt="fancy_grid"))
        print("____________________________________________________________________")
        print("1. Delete Transactions")
        print("2. Exit")
        while True: #This loop checks for correct user choice input
            remove_transactions_choice = input("Enter your choice: ")
            if remove_transactions_choice not in ('1', '2', 'exit'):
                print("Invalid choice. Please try again.")
            else:
                break

        if remove_transactions_choice == '1':
            remove_transaction()
        elif remove_transactions_choice == '2':
            return main_menu()
####################################################################################################
def remove_transaction(): #This module does the actual deleting on transactions
    while True: # This loop is the verify for the correct transaction ID
        delete_id = input("Enter the transaction ID of the transaction to be deleted: ")
        try:
            delete_id = int(delete_id)
            break
        except ValueError:
            print("Invalid ID. Please try again.")
    transaction_found = False #This is a marker to understand if we were able to find the transaction or not
    for t in financy_classes.Transactions.transactions_registry: #Filtering the transactions registry
        if t.id == delete_id:
            financy_classes.Transactions.transactions_registry.remove(t)
            print("Transaction Deleted")
            transaction_found = True #Since we were able to delete the transaction, this marker becomes true
            if t.ttype == "Income":
                financy_classes.Transactions.balance -= t.amount
            else:
                financy_classes.Transactions.balance += t.amount
            new_all_transactions_filter = [t for t in financy_classes.Transactions.transactions_registry] #creating a new list + dictionary for displaying using tabulate
            new_all_transactions = []
            for t in new_all_transactions_filter:
                new_all_transactions.append({
                    "ID": t.id,
                    "Type": t.ttype,
                    "Amount ($)": t.amount,
                    "Category": t.category,
                    "Description": t.description,
                    "Date": t.date
                })
            print(tabulate(new_all_transactions, headers="keys", tablefmt="fancy_grid")) # We display the transaction list again
            break
    if not transaction_found: #Here we check if we were able to delete the transaction, if not then we print that it wasn't found.
        print("Transaction not found.")
    return remove_transactions_menu()
######################################################################################################
#login() # Call the login function
print(r""" 
$$$$$$$$\ $$\                                                   
$$  _____|\__|                                                  
$$ |      $$\ $$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\ $$\   $$\ 
$$$$$\    $$ |$$  __$$\  \____$$\ $$  __$$\ $$  _____|$$ |  $$ |
$$  __|   $$ |$$ |  $$ | $$$$$$$ |$$ |  $$ |$$ /      $$ |  $$ |
$$ |      $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ |      $$ |$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |
\__|      \__|\__|  \__| \_______|\__|  \__| \_______| \____$$ |
                                                      $$\   $$ |
                                                      \$$$$$$  |
                                                       \______/ """) #This is just a fun thing i tried, thought it would be coool
main_menu() #Call the main menu function, thanks to the return functions, the user can gracefully navigate through the program. This greatly reduces the lines of code needed.