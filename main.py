class BankAccount:
    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.owner}'s account balance: ${self.balance:.2f}"


account = BankAccount(input("Account holder: ").strip(), 100.00)
print(account)
account.deposit(50)
print("After depositing $50:", account)
account.withdraw(25)
print("After withdrawing $25:", account)
