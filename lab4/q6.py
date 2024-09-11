# Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance.

class BankAccount:
  def __init__(self):
    self.customer_name = ""
    self.date_of_opening = " "
    self.account_number = " "
    self.balance = 0.0

  def getData(self):
    self.customer_name = input("Enter the customer's name: ")
    self.date_of_opening = input("ENter the date of openng: ")
    self.account_number = input()
