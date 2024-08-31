operator = input("Which operation you want to perform(+, -, /, *): ")
a = int(input("Enter A: "))
b = int(input("Enter B: "))

if operator == "+":
    print(a, operator, b,"=", a-(-b))
elif operator == "-":
    print(a, operator, b,"=", a - b)
elif operator == "*":
    print(a, operator, b,"=", a * b)
elif operator == "/":
    print(a, operator, b,"=", a/b)
else:
    print("Try Again!")
