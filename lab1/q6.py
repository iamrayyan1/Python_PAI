dict = {"Physics":"", "Chemistry":"", "Maths":""}

dict["Physics"] = int(input("Enter your marks in Physics: "))
dict["Chemistry"] = int(input("Enter your marks in Chemistry: "))
dict["Maths"] = int(input("Enter your marks in Maths: "))

total = 0
for marks in dict.values():
    total += marks

avg = total / 3

highest_marks = None
subject = None

for sub, marks in dict.items():
    if highest_marks is None or marks > highest_marks:
        highest_marks = marks
        subject = sub

print("Average Marks:", avg)
print("Highest marks:", subject)
