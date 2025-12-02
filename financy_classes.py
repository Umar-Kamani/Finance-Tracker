
class Transactions:
    transactions_registry = []
    balance = 0.0
    transactions_id = 0
    def __init__(self, ttype, amount, category, description, date):
        Transactions.transactions_id += 1
        self.id = Transactions.transactions_id
        self.ttype = ttype
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date
        Transactions.transactions_registry.append(self) #This appends any object that belongs to the Transactions class to the transactions_registry list

class Income(Transactions):
    def __init__(self, ttype, amount, category, description, date):
        super().__init__("Income", amount, "Income", description, date)

class Expenses(Transactions):
    def __init__(self, ttype, amount, category, description, date):
        super().__init__("Expense", amount, category, description, date)