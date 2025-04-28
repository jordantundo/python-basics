class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Invalid withdrawal amount")
    
    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance:.2f}")

if __name__ == "__main__":
    # Demo usage
    account = BankAccount("John Doe", 100)
    account.check_balance()
    account.deposit(50)
    account.withdraw(25)
    account.check_balance()
