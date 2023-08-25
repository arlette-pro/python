class BankAccount:
    accounts = []

    def __init__(self, interest_rate=0, balance=0.02) -> None:
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self 

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print("Interest rate:", account.interest_rate)
            print("Balance:", account.balance)
            

# Create two instances of the BankAccount class
account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.02, 500)

# Perform operations on the first account
account1.deposit(200).deposit(300).deposit(400).withdraw(100).yield_interest().display_account_info()

# Perform operations on the second account
account2.deposit(100).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# Print information of all accounts
BankAccount.print_all_accounts()