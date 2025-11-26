from pycparser.c_ast import While

import financy_classes
from datetime import datetime
from tabulate import tabulate

balance = 0.00  #This is the balance variable for the program, all income and expense will be deducted from here.

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
    while True:
        income_date = input("Enter the date of your income (DD/MM/YYYY), leave blank for today's date: ").strip()
        if income_date == "":
            income_date = datetime.today().strftime("%d/%m/%Y")
            print(f"Using today's date: {income_date}")
            break
        try:
            datetime.strptime(income_date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date. Please try again (DD/MM/YYYY).")

    income_description = input("Enter your income description: ")
    new_income = financy_classes.Income("Income", income_amount,"Income", income_description, income_date)
    balance += income_amount
    print(f"Your new balance is ${balance}")
    incomes = [t for t in financy_classes.Transactions.transactions_registry if t.ttype == "Income"]

    table = []
    for t in incomes:
        table.append({
            "Type": t.ttype,
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date
        })
    print(tabulate(table, headers="keys", tablefmt="fancy_grid" ))

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

    expense_date = datetime.today().strftime("%d-%m-%Y")
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
    expenses = [t for t in financy_classes.Transactions.transactions_registry if t.ttype == "Expense"]
    table = []
    for t in expenses:
        table.append({
            "Type": "Expense",
            "Amount ($)": t.amount,
            "Category": t.category,
            "Description": t.description,
            "Date": t.date,
        })
    table.append({
        "Sum of Expenses ($)": sum(t.amount for t in expenses),
    })
    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
def date_validation(date_input):
    pass
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
add_income()

#per_category_spending_history("Food")
print(r""" ________  __                                                   
|        \|  \                                                  
| $$$$$$$$ \$$ _______    ______   _______    _______  __    __ 
| $$__    |  \|       \  |      \ |       \  /       \|  \  |  \
| $$  \   | $$| $$$$$$$\  \$$$$$$\| $$$$$$$\|  $$$$$$$| $$  | $$
| $$$$$   | $$| $$  | $$ /      $$| $$  | $$| $$      | $$  | $$
| $$      | $$| $$  | $$|  $$$$$$$| $$  | $$| $$_____ | $$__/ $$
| $$      | $$| $$  | $$ \$$    $$| $$  | $$ \$$     \ \$$    $$
 \$$       \$$ \$$   \$$  \$$$$$$$ \$$   \$$  \$$$$$$$ _\$$$$$$$
                                                      |  \__| $$
                                                       \$$    $$
                                                        \$$$$$$""")
