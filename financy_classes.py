from datetime import date

class Transactions:
    transactions_registry = []
    def __init__(self, ttype, amount, category, description, date):
        self.ttype = ttype
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date
        Transactions.transactions_registry.append(self)

class Income(Transactions):
    def __init__(self, ttype, amount, category, description, date):
        super().__init__("Income", amount, "Income", description, date)

class Expenses(Transactions):
    def __init__(self, amount, date, category, description, ttype):
        super().__init__("Expense", amount, category, description, date)
