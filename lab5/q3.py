# Write a program in which a class named Account has private member variables 
# named account_no ,account_bal ,security_code. Use a public function to initialize the variables and print all data.

class Account:
    def __init__(self,__account_no,__account_bal,__security_code):
        self.__account_no = __account_no
        self.__account_balance = __account_bal
        self.__security_code = __security_code
    
    def print_data(self):
        print(f"The Account Number is: {self.__account_no}")
        print(f"The Account Balance is: {self.__account_balance}")
        print(f"The Security Code is: {self.__security_code}")

acc = Account(121,1000,911)
acc.print_data()
