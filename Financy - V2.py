import financy_classes
from datetime import date
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

    income_date = date.today().strftime("%d-%m-%Y")
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

    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
add_income()
