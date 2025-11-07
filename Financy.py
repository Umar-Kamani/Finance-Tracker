def login():
    User = {
        'umar': 'umar@1234',
        'yovin': 'yovin@1234'
    }

    while True:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if username_input in User and password_input in User[username_input]:
            print(f"Welcome back {username_input}!")
            break
        else:
            print("Username or password is incorrect")
################################################################################################
def main_menu():
    print("Thank you for using Financy.")
    print("---Main Menu---")
    print("1. Income")
    print("2. Expense")
    print("3. Transactions")
    print("4. Show Summary")
    print("5. Exit")
    while True:
        main_menu_choice = input("Enter your choice: ")
        if main_menu_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    return main_menu_choice
################################################################################################
def income_menu():
    print("---------------")
    print("1. Add Income")
    print("2. Remove Income")
    while True:
        income_choice = input("Enter your choice: ")
        if income_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    return income_choice
################################################################################################
def expense_menu():
    print("---------------")
    print("1. Add Expense")
    while True:
        expense_choice = input("Enter your choice: ")
        if expense_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    return expense_choice
################################################################################################
def transactions_menu():
    print("---------------")
    print("1. Show Income History")
    print("2. Show Expense History")
    while True:
        transactions_choice = input("Enter your choice: ")
        if transactions_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    return transactions_choice
################################################################################################
def show_summary_menu():
    print("---------------")
    print("1. Show Summary")
    while True:
        show_summary_choice = input("Enter your choice: ")
        if show_summary_choice not in ('1', '2', '3', '4', '5', 'exit'):
            print("Invalid choice. Please try again.")
        else:
            break
    return show_summary_choice
################################################################################################
def menu_selector(main_menu_choice):
    if main_menu_choice == '1':
        income_menu()
    elif main_menu_choice == '2':
        expense_menu()
    elif main_menu_choice == '3':
        transactions_menu()
    elif main_menu_choice == '4':
        show_summary_menu()
    elif main_menu_choice == '5':
        print("Thank you for using Financy.")
        exit()
##################################################################################################
main_menu_choice = main_menu()

if main_menu_choice == '1':
    income_menu()
elif main_menu_choice == '2':
    expense_menu()
elif main_menu_choice == '3':
    transactions_menu()
elif main_menu_choice == '4':
    show_summary_menu()
elif main_menu_choice == '5':
    print("Thank you for using Financy.")
    exit()


