lst = []
max = 0
size = int(input("Enter size of the list: "))
print("Enter the elements: ")

for i in range(0, size):
    number = int(input())
    lst.append(number)

for number in lst:
    if number > max:
        max = number

print("Maximum Number:", max)
