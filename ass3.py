#ass3:

class BankAccount:
    def __init__(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.acc_no}")
        print(f"Account type: {self.acc_type}")
        print(f"Balance: {self.balance}")


accounts = []


def create_account():
    name = input("Enter depositor name: ")
    acc_no = input("Enter account number: ")
    acc_type = input("Enter account type: ")
    balance = float(input("Enter initial balance: "))
    account = BankAccount(name, acc_no, acc_type, balance)
    accounts.append(account)
    print("Account created successfully!")


def deposit():
    acc_no = input("Enter account number: ")
    for account in accounts:
        if account.acc_no == acc_no:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print("Amount deposited successfully!")
            account.display_details()
            return
    print("Account not found.")


def withdraw():
    acc_no = input("Enter account number: ")
    for account in accounts:
        if account.acc_no == acc_no:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            print("Amount withdrawn successfully!")
            account.display_details()
            return
    print("Account not found.")


def display():
    acc_no = input("Enter account number: ")
    for account in accounts:
        if account.acc_no == acc_no:
            account.display_details()
            return
    print("Account not found.")


while True:
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display details")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        display()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
