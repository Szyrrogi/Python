class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczające środki")
        else:
            self.balance -= amount

konto = BankAccount(100)
konto.deposit(50)
konto.withdraw(30)
print(konto.balance)