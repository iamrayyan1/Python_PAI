def factorial(n):
    
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1

    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

# Example usage
user_input = int(input("Enter a number to compute its factorial: "))
print(factorial(user_input))
