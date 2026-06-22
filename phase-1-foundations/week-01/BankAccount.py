class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance"""
    pass

class NegativeAmountError(Exception):
    """Raised when a negative amount is provided"""
    pass

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
        if amount < 0:
            raise NegativeAmountError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is only {self.balance}")
            # return "Insufficient balance"
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
try:
    new_balance = account.withdraw(500000)
    print(f"Transaction Successful: {new_balance}")
except InsufficientFundsError as e:
    print(f"Transaction Failed: {e}")
except NegativeAmountError as e:
    print(f"Invalid input: {e}")
# print(account.withdraw(500000))
print(account)

print(account2)
print(account2.deposit(10000))
try:
    new_balance = account2.withdraw(500000)
    print(f"Transaction Successful: {new_balance}")
except InsufficientFundsError as e:
    print(f"Transaction Failed: {e}")
except NegativeAmountError as e:
    print(f"Invalid input: {e}")
# print(account2.withdraw(5000))
print(account2)
