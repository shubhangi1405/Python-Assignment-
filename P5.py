# Experiment 5: Bank Account Class

class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited Rs. {amount:.2f}. New Balance: Rs. {self.balance:.2f}')
        else:
            print('Invalid deposit amount.')

    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid withdrawal amount.')
        elif amount > self.balance:
            print(f'Insufficient funds! Balance: Rs. {self.balance:.2f}')
        else:
            self.balance -= amount
            print(f'Withdrawn Rs. {amount:.2f}. Remaining Balance: Rs. {self.balance:.2f}')

    def check_balance(self):
        print(f'Account: {self.account_number} | Owner: {self.owner}')
        print(f'Current Balance: Rs. {self.balance:.2f}')

    def __str__(self):
        return f'BankAccount({self.account_number}, {self.owner}, Rs.{self.balance:.2f})'

# Main Program
acc = BankAccount('ACC001', 'Rahul Sharma', 1000.00)
acc.check_balance()
print()
acc.deposit(5000)
acc.withdraw(2000)
acc.withdraw(10000)
print()
acc.check_balance()
