def multiply(numbers):
    if not numbers:
        return 1
    
    multiple = 1
    
    for number in numbers:
        multiple *= number
    
    return multiple


array = [1,3,5,7]
result = multiply(array)
print(f"The product of all numbers in the list is: {result}")
