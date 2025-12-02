Financy - Personal Finance Tracker

Financy is a clean,simple and intuitive command line based personal finance tracker. It enables users to record income,
track expenses, monitor categories and view transaction history. It is built using Python and Object Oriented Programming(OOP)

Project Overview

Financy Helps
-Track income and expenses
-Track account balance
-View category wise spending reports
-Display transactions
-Ability to automatically handle dates
-Add and delete transactions
-Clean and intuitive menu system

External Modules Used:
-Tabulate - For proper table formatting
-Datetime - For timestamps

Program Features

Income Management
-Add income with description and date
-View full income history
-Auto updates balance

Expense Management
-Add expenses with description,date and category
-Validate proper category
-View full expense history

Account Analytics
-View total income
-View total expense
-View current balance
-Category-wise spending history

Transaction Deletion
-View all transactions 
-Delete transaction by transaction ID

Project File Structure

Finance Tracker
    financy_main.py
    financy_classes.py
    README.md

Login Credentials

Username/password: umar/umar@1234
Username/password: yovin/yovin@1234

Menu Structure

1. Income
    Add Income
    View Income History
2. Expense
    Add Expense
    View Expense History
3. Account Analytics
    View Total Income History
    View Total Expense History
    View Account Balance
    View per-category spending history
4. Delete Transactions
    View all Transactions
    Delete by ID
5. Exit

Sample Interactions

________________________________________________________________________________________________________________________
Adding Income 

---Main Menu---
Current balance: $0.0
1. Income
2. Expense
3. Account Analytics
4. Delete Transactions
5. Exit
Enter your choice: 1
---------------
Welcome to the Income Menu
---------------
1. Add Income
2. View Income History
3. Exit to Main Menu
Enter your choice: 1
---------------
Current balance: $0.0
Enter your income ($): 200
Enter the date of your income (DD/MM/YYYY), leave blank for today's date: 
Using today's date: 02/12/2025
Enter your income description: Salary December
Your new balance is $200.0

________________________________________________________________________________________________________________________
Adding Expense

---Main Menu---
Current balance: $200.0
1. Income
2. Expense
3. Account Analytics
4. Delete Transactions
5. Exit
Enter your choice: 2
---------------
Welcome to the Expense Menu
---------------
1. Add Expense
2. View Expense History
3. Exit to Main Menu
Enter your choice: 1
---------------
Current balance: $200.0
Enter your expense ($): 200
Enter the date of your income (DD/MM/YYYY), leave blank for today's date: 
Using today's date: 02/12/2025
Enter your expense description: KFC
Enter a category from the following: Food, Rent, Entertainment, Clothing, Loan and Other
Enter your expense category: food
Your new balance is $0.0
________________________________________________________________________________________________________________________

Deleting Transactions

---Main Menu---
Current balance: $0.0
1. Income
2. Expense
3. Account Analytics
4. Delete Transactions
5. Exit
Enter your choice: 4
Welcome to the transactions Deleting Tool!
____________________________________________________________________
╒══════╤═════════╤══════════════╤════════════╤═════════════════╤════════════╕
│   ID │ Type    │   Amount ($) │ Category   │ Description     │ Date       │
╞══════╪═════════╪══════════════╪════════════╪═════════════════╪════════════╡
│    1 │ Income  │          200 │ Income     │ Salary December │ 02/12/2025 │
├──────┼─────────┼──────────────┼────────────┼─────────────────┼────────────┤
│    2 │ Expense │          200 │ Food       │ KFC             │ 02/12/2025 │
╘══════╧═════════╧══════════════╧════════════╧═════════════════╧════════════╛
____________________________________________________________________
1. Delete Transactions
2. Exit
Enter your choice: 1
Enter the transaction ID of the transaction to be deleted: 1
Transaction Deleted
╒══════╤═════════╤══════════════╤════════════╤═══════════════╤════════════╕
│   ID │ Type    │   Amount ($) │ Category   │ Description   │ Date       │
╞══════╪═════════╪══════════════╪════════════╪═══════════════╪════════════╡
│    2 │ Expense │          200 │ Food       │ KFC           │ 02/12/2025 │
╘══════╧═════════╧══════════════╧════════════╧═══════════════╧════════════╛
Welcome to the transactions Deleting Tool!
____________________________________________________________________
╒══════╤═════════╤══════════════╤════════════╤═══════════════╤════════════╕
│   ID │ Type    │   Amount ($) │ Category   │ Description   │ Date       │
╞══════╪═════════╪══════════════╪════════════╪═══════════════╪════════════╡
│    2 │ Expense │          200 │ Food       │ KFC           │ 02/12/2025 │
╘══════╧═════════╧══════════════╧════════════╧═══════════════╧════════════╛
____________________________________________________________________
1. Delete Transactions
2. Exit
Enter your choice: 
________________________________________________________________________________________________________________________
