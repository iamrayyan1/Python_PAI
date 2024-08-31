# Design a console based application for Converting different currency. You are required to ask
# user to choose input which currency you want to convert and then ask the amount. After that
# ask in which currency you want to convert. Then convert that currency into desired one...
# (Currency should includ Euro , Dollar, PkR, INR , and yen)

def currency_converter():
    #dictionary allows to store name and value together
    currencies = {
        "DOLLAR": 1, #BASE CURRENCY
        "EURO": 0.90,
        "PKR": 278.58, 
        "INR": 83.89 , 
        "YEN": 146.21
         }
    
    
    convert = input("Which currency do you want to convert? ").upper()
    amount = float(input("Enter the amount: "))
    convert_to = input("Which currency do you want to convert to?").upper()

    #checking validity
    if convert in currencies and convert_to in currencies:
         
         rate_from = currencies[convert]
         rate_to = currencies[convert_to]
        
        # Convert amount to target currency
         new_amount = (amount / rate_from) * rate_to
         print(f"Converting {amount} {convert} to {convert_to} is: {new_amount: .2f} {convert_to}")
    else:
         print("Invalid currency! Please select from the given options..")    

currency_converter()


