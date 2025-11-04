'''
Exercise:
Write a class BankAccount with methods
    deposit,
    withdraw,
    check_balance.
Handle cases of insufficient balance.

'''

class BankAccount:
    branch = "SBI MP NAGAR" #class/static
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit(self,amount):
        print(f"Your previous balance wass {self.balance}")
        self.balance += amount
        print(f"Your current balance is {self.balance}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Your current balance is {self.balance} after withdraw of {amount}")
        else:
            print("Insufficient Balance")
            return
    def check_balance(self):
        print(f"Your current balance is {self.balance}")

john = BankAccount(500)
john.withdraw(1000)
john.deposit(10000)
john.withdraw(4568)
john.check_balance()
