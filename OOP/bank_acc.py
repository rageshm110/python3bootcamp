#!/usr/bin/python3
# For this challenge, create a bank account class that has two attributes:
#   > owner
#   > balance
# and two methods:
#   > deposit
#   > withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balace updated. Current Balance: {0}".format(self.balance))
    
    def withdraw(self, amount):
        if (self.balance < amount):
            print("We can not process your request. Insufficeint balance.")
        else:
            self.balance = self.balance - amount
            print("Withdrawal success. Current Balance: {0}".format(self.balance))
    
    def __str__(self):
        message = "Account owner\t: {0}\nAccount Balance\t: {1}".format(self.owner, self.balance)
        return message

def main():
    account1 = BankAccount("Abhijith", 200)
    account1.withdraw(100)
    print(account1)
    print("\n")
    account1.deposit(300)
    print(account1)
    account1.withdraw(500)
    print(account1)

if __name__ == '__main__':
    main()
