lst = []
size = int(input("Enter the number of elements in the list: "))
x = int(input("Enter the number: "))
print("Enter the elements: ")

for i in range(0, size):
    num = int(input())
    lst.append(num)

temp = []

for num in lst:
    if num >= x:
        temp.append(num)

print("Updated list:", temp)
