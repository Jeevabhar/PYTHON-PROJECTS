class BankAccount:
    

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def check_balance(self):
        print("Current Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print("Withdrawn:", amount)


account = BankAccount("Arun", 50000)

account.check_balance()

account.deposit(10000)

account.withdraw(5000)

account.check_balance()
