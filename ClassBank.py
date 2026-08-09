class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited: {amount}")
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"Withdrew: {amount}")
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance


account = BankAccount("Ali", 100)

print("Owner:", account.owner)
print("Balance:", account.get_balance())

account.deposit(50)
account.withdraw(30)

print("Final balance:", account.get_balance())
