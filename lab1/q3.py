lst = []
count = 0
size = int(input("Enter the size of the list: "))
print("Enter the elements: ")

for i in range(0, size):
    number = int(input())
    lst.append(number)

for numbers in range(0, size):
    if lst[numbers] % 2 == 0:
        count += 1

print("Even elements in list =", count)
