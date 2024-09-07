# Take two integer numbers from user as input. Divide these two numbers. If one number is
# being divided by zero (another number) then handle ZeroDivisionError and if entered value
# is wrong (for example, a string) then handle ValueError.

# Name: Rija Ali
# ID: 23k-0057

def divison_error():
    try: 
        num1 = int(input("Enter the number you want to divide: "))
        num2 = int(input("Enter the dividend: "))
        result = num1/num2
        print("The result is: " , result)
    except ValueError:
        print("the entered value is not valid")
    except ZeroDivisionError:
        print("you can't divide by zero")
    except Exception as e:
           print(f"An unexpected error occurred in: {e}")

    # else:
    # print(f"The Result is {result}")

divison_error()

