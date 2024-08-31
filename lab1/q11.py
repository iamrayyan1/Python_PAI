dict = {"Maths": "", "Physics": "", "Chemistry":" "}

dict["Physics"] = int(input("Enter your marks in Physics: "))
dict["Chemistry"] = int(input("Enter your marks in Chemistry: "))
dict["Maths"] = int(input("Enter your marks in Maths: "))

total = 0
for marks in dict.values():
    total += marks

avg = total / 3
percentage = ((total/300)*100)

print("Average:", avg)
print("Percentage:", percentage)
