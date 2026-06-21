class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Amount can not be negative"
        else:    
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.owner}] — Balance: ${self.balance}"

account = BankAccount("abdullah", 50000)
account2 = BankAccount("ahmed", 20000)

print(account)
print(account.deposit(-10000))
print(account.withdraw(500000))
print(account)

print(account2)
print(account2.deposit(10000))
print(account2.withdraw(5000))
print(account2)
