class BankAccount:
    accounts = []

    def __init__(self, interest_rate=0.02, balance=0) -> None:
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
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def create_account(self, interest_rate=0.02, balance=0):
        account = BankAccount(interest_rate, balance)
        self.accounts.append(account)
        return account

    def make_deposit(self, account_index, amount):
        account = self.accounts[account_index]
        account.deposit(amount)
        return self

    def make_withdrawal(self, account_index, amount):
        account = self.accounts[account_index]   
        account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        for i, account in enumerate(self.accounts):
            print(f"Account {i+1} Balance:", account.balance)
        return self
        
    def transfer_money(self, amount, other_user, from_account_index, to_account_index):
        from_account = self.accounts[from_account_index]
        to_account = other_user.accounts[to_account_index]

        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print("Transfer successful.")
        else:
            print("Insufficient funds for transfer.")

        return self    

# Create two instances of the BankAccount class
user1 = User('ada luis', 'adaluis@gmail.com')
user2 = User('adam luisa', 'adamluisa@gmail.com')

# Create bank accounts for users
user1.create_account(interest_rate=0.02, balance=1000)
user2.create_account(interest_rate=0.02, balance=500)

# Perform operations on user1's account
user1.make_deposit(0, 200).make_deposit(0, 300).make_withdrawal(0, 100).display_user_balance()

# Perform operations on user2's account
user2.make_deposit(0, 100).make_deposit(0, 200).make_withdrawal(0, 50).make_withdrawal(0, 50).display_user_balance()

# Transfer money from user1 to user2
user1.transfer_money(300, user2, 0, 0)

# Display balances after transfer
user1.display_user_balance()
user2.display_user_balance()