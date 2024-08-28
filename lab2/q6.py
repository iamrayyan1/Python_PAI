def multiply(numbers):
    if not numbers:
        return 1
    
    multiple = 1
    
    for number in numbers:
        multiple *= number
    
    return multiple


example_list = [2, 3, 4, 5]
result = multiply(example_list)
print(f"The product of all numbers in the list is: {result}")
