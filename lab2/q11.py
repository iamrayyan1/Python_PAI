# 11. You have a dictionary where each key is a student’s name and each value is a list of their grades.
# You need to perform the following operations:
# • Add a new grade to a student's list of grades.
# • Calculate and print the average grade for a specific student.
# • Add a new student with an initial empty list of grades.
# • Remove a student from the dictionary

def student_dictionary():
   
    dictionary = {
        "Ali": [78,92,80],
        "Ahmed": [54,63,60], 
        "Amna": [92,85,82]
    }
#allowing the user to choose from the options
    print("What operation do you want to perform?")
    print("1. Add a new grade to a student's list of grades.")
    print("2. Calculate and print the average grade for a specific student.")
    print("3. Add a new student with an initial empty list of grades.")
    print("4. Remove a student from the dictionary")
   
    option = int(input())
#if cases
    if option == 1:
        student = input("Enter the Student's Name: ")
        if student in dictionary:
            grade = int(input(f"Enter the {student}'s new grade: "))
            dictionary[student].append(grade)
            print(f"Updated grades for {student}: {dictionary[student]} ")
            print("Updated Student Dictionary: " , dictionary)
        else:
            print(f"Student {student} not found in the list!")
    
    elif option == 2:
         student = input("Enter the name of the student you want to calculate average grade of:")
         if student in dictionary:
             grades = dictionary[student]
             average_grade = sum(grades)/len(grades)
             print(f"The Average grade for {student} is {average_grade:.2f}")
         else:
             print(f"{student} not found in the list!")

    elif option == 3:
        student = input("Enter the new student's name: ")
        if student not in dictionary:
            dictionary[student] = []
            print(f"{student} added to the dictionary with an empty list of grades.")
            print("Updated Student Dictionary: " , dictionary)
        else:
            print(f" {student} already exists in the dictionary!")
    
    elif option == 4:
        print("Current Student Dictionary: " , dictionary)
        student = input("Enter the student's name: ")
        if student in dictionary:
            del(dictionary[student])
            print(f"{student} removed from the dictionary")
            print("Updated Student Dictionary: " , dictionary)
        else:
            print(f"{student} does not exist in the dictionary!")
    
    else:
        print("Invalid option!")

student_dictionary()
