# Write a program in which a class named Account has private member variables named
# account_no ,account_bal ,security_code. Use a public function to initialize the variables
# and print all data. [2 marks]

class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no          
        self.__account_bal = account_bal         
        self.__security_code = security_code   

    def display_info(self):
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")


account = Account("101", 1560090.0, "2502")
account.display_info()
