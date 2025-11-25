#Global Variables
from datetime import date
from tabulate import tabulate
import financy_classes


balance = 0.00  #This is the balance variable for the program, all income and expense will be deducted from here.

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
    print("Thank you for using Financy.")
    print("---Main Menu---")
    print(f"Current balance: ${balance}") #Displays the balance at any given moment or time
    print("1. Income")
    print("2. Expense")
    print("3. Account Analytics")
    print("4. Exit")
    while True: #This loop checks for correct user choice input
        main_menu_choice = input("Enter your choice: ")
        if main_menu_choice not in ('1', '2', '3', '4', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    return menu_selector(main_menu_choice)
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
        show_income_table() #redirects to this function
    elif income_choice == '3' or income_choice == 'exit':
        print("Returning to Main Menu")
    return main_menu()
################################################################################################
def expense_menu():
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
        show_expense_table()
    elif expense_choice == '3' or expense_choice == 'exit':
        print("Returning to Main Menu")
    return main_menu()
################################################################################################
def account_analytics_menu():
    global balance
    print("---------------")
    print("Welcome to the Account Analytics Menu")
    print("---------------")
    print(f"Current balance: ${balance}")
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
        show_income_table(Analytics=True)
    elif account_analytics_choice == '2':
        print("---------------")
        show_expense_table()
    elif account_analytics_choice == '3':
        print("---------------")
        print(f"Your current balance: ${balance}")
    elif account_analytics_choice == '4':
        print("---------------")
        per_category_spending_history("Food")
        per_category_spending_history("Rent")
        per_category_spending_history("Entertainment")
        per_category_spending_history("Clothing")
        per_category_spending_history("Loan")
        per_category_spending_history("Other")
    elif account_analytics_choice == '5' or account_analytics_choice == 'exit':
        print("Returning to Main Menu.")
    return main_menu()
################################################################################################
def menu_selector(main_menu_choice):
    if main_menu_choice == '1':
        income_menu()
    elif main_menu_choice == '2':
        expense_menu()
    elif main_menu_choice == '3':
        account_analytics_menu()
    elif main_menu_choice == '4' or main_menu_choice == 'exit':
        print("Thank you for using Financy.")
        exit()
##################################################################################################
def add_income():
    global balance
    print(f"Current balance: ${balance}")
    while True:
        income_amount = input("Enter your income ($): ")
        try:
            income_amount = float(income_amount)
            if income_amount <= 0:
                print("Invalid income. Please try again. Please enter only numbers.")
            else:
                break
        except ValueError:
            print("Invalid income. Please try again. Please enter only numbers.")
    income_date = date.today().strftime("%d-%m-%Y")
    income_description = input("Enter your income description: ")
    new_income = financy_classes.Income("Income", income_amount,"Income", income_description, income_date)
    balance += income_amount
    print(f"Your new balance is ${balance}")
    return income_menu()
###################################################################################################
def add_expense():
    global balance
    valid_expenses = ['Food', 'Rent', 'Entertainment', 'Clothing', 'Loan', 'Other']
    print(f"Current balance: ${balance}")
    while True:
        expense_amount = input("Enter your expense ($): ")
        try:
            expense_amount = float(expense_amount)
            if expense_amount <= 0:
                print("Invalid expense. Please try again. Please enter only numbers.")
            else:
                break
        except ValueError:
            print("Invalid expense. Please try again. Please enter only numbers.")

    expense_date = date.today().strftime("%d-%m-%Y")
    expense_description = input("Enter your expense description: ")

    while True:
        expense_category = input("Enter your expense category: ").capitalize()
        if expense_category not in valid_expenses:
            print("Invalid choice. Please enter a valid category such as Food, Rent, Entertainment, Clothing, Loan and Other")
        else:
            break

    new_expense = financy_classes.Expenses("Expenses", expense_amount,expense_category, expense_description, expense_date)
    balance -= expense_amount
    print(f"Your new balance is ${balance}")
    return expense_menu()
####################################################################################################
def show_income_table(Analytics):
    incomes = [t for t in financy_classes.Transactions.transactions_registry if t.ttype == "Income"]
    income_table = []
    for t in incomes:
        income_table.append({
            "Type": "Income",
            "Amount ($)": t.amount,
            "Category": "Income",
            "Description": t.description,
            "Date": t.date
        })
    print(tabulate(income_table, headers="keys", tablefmt="fancy_grid"))

    if Analytics:
        return account_analytics_menu()
    else:
        return income_menu()
#####################################################################################################
def show_expense_table(Analytics):
    expenses = [t for t in financy_classes.Transactions.transactions_registry if t.ttype == "Expense"]
    expense_table = []
    for t in expenses:
        expense_table.append({
            "Type": "Expense",
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
        })
    print(tabulate(expense_table, headers="keys", tablefmt="fancy_grid"))
    if Analytics:
        return account_analytics_menu()
    else:
        return expense_menu()
####################################################################################################
def per_category_spending_history(category):
    sp_category =[t for t in financy_classes.Transactions.transactions_registry if t.category == category]

    sp_category_history = []
    for t in sp_category:
        sp_category_history.append({
            "Type": t.ttype,
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
        })
    print(f"Please find your spending history for {category} below.")
    print("____________________________________________________________________")
    print(tabulate(sp_category_history, headers="keys", tablefmt="fancy_grid"))
###################################################################################################


login()
main_menu()