#Global Variables
from datetime import date

from tabulate import tabulate

balance = 0.0 #This is the balance variable for the program, all income and expense will be deducted from here.
transactions =[] #This list stores all transactions that happen in the program, whether it is an income or expense

def login():
    user = { #This dictionary stores the lists of users that are allowed to log into the Financy System
        'umar': 'umar@1234',
        'yovin': 'yovin@1234'
    }

    while True:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if username_input in user and password_input in user[username_input]:
            print(f"Welcome back {username_input}!")
            break
        else:
            print("Username or password is incorrect")
################################################################################################
def main_menu(): #This is the main menu of Financy, it is where users can navigate to the different pages and sub-menus
    print("Thank you for using Financy.")
    print("---Main Menu---")
    print(f"Current balance: ${balance}")
    print("1. Income")
    print("2. Expense")
    print("3. Show Transactions History")
    print("4. Exit")
    while True:
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
    while True: #This while true loop check for a valid user choice.
        income_choice = input("Enter your choice: ")
        if income_choice not in ('1', '2', '3','exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    if income_choice == '1':
        print("---------------")
        add_income()
    elif income_choice == '2':
        print("---------------")
        show_income_table()
    elif income_choice == '3':
        print("Returning to Main Menu")
    return main_menu()
################################################################################################
def expense_menu():
    print("---------------")
    print("1. Add Expense")
    print("2. View Expense History")
    print("3. Exit to Main Menu")
    while True:
        expense_choice = input("Enter your choice: ")
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
    elif expense_choice == '3':
        print("Returning to Main Menu")
    return main_menu()
################################################################################################
def transactions_menu():
    pass
################################################################################################
def menu_selector(main_menu_choice):
    if main_menu_choice == '1':
        income_menu()
    elif main_menu_choice == '2':
        expense_menu()
    elif main_menu_choice == '3':
        transactions_menu()
    elif main_menu_choice == '4' or main_menu_choice == 'exit':
        print("Thank you for using Financy.")
        exit()
##################################################################################################
def add_income():
    income = input("Enter your income ($): ")
    income = float(income)
    income_date = date.today().strftime("%d-%m-%Y")
    income_entry = {
        "Type": "Income",
        "Amount": f"${income}",
        "Date": income_date
    }
    transactions.append(income_entry)
    print(f"Your new balance is ${balance + income}")
    return income_menu()
###################################################################################################
def add_expense():
    expense = input("Enter your expense ($): ")
    expense = float(expense)
    expense_description = input("Enter your expense description: ")
    expense_category = input("Enter your expense category: ").capitalize()
    expense_date = date.today().strftime("%d-%m-%Y")
    while expense_category not in ('Food', 'Rent', 'Entertainment', 'Clothing', 'Loan'):
            print("Invalid choice. Please enter a valid category of expense such as 'Food', 'Rent', 'Entertainment', 'Clothing', 'Loan', 'Gift'")
            expense_category = input("Enter your expense category: ")

    expense_entry = {
        "Type": "Expense",
        "Amount": f"${expense}",
        "Description": expense_description,
        "Category": expense_category,
        "Date": expense_date
    }
    transactions.append(expense_entry)
    print(f"Your new balance is ${balance - expense}")
    return expense_menu()
####################################################################################################
def show_income_table():
    incomes = []
    for t in transactions:
        if t["Type"] == "Income":
            incomes.append(t)
    tabulate_income_data = incomes
    print(tabulate(incomes, headers="keys", tablefmt="fancy_grid"))
    return income_menu()
#####################################################################################################
def show_expense_table():
    expenses = []
    for t in transactions:
        if t["Type"] == "Expense":
            expenses.append(t)
    tabulate_expense_data = expenses
    print(tabulate(expenses, headers="keys", tablefmt="fancy_grid"))
    return expense_menu()
####################################################################################################
