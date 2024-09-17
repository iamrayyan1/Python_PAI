# Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance.

class bankAccount:
    def __init__(self,acc_num,date_opening,name,balance=0):
        self.acc_num = acc_num
        self.balance = balance
        self.date_opening = date_opening
        self.name = name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"the ammount {amount} was deposited\nnew amount is {self.balance}")
        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"the amount {amount} was withdrawn")
        else:
            print("Insufficient balance")
            
    def check_balance(self):
        print(f"account number {self.acc_num} has balance {self.balance}")
        

bank = bankAccount(101,"7-10-1999","ahmed",1789060)

bank.deposit(55600)
bank.withdraw(250000)
bank.check_balance()
