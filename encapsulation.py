# Encapsulation
class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


my_account = BankAccount()

print(my_account.get_balance())  # Output: 1000
