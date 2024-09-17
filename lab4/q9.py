# 9. A university is deciding to upgrade its system. In order to upgrade, you need to implement
# the following scenario: Note the following:
# • The class student has a function that displays information about the student i.e.
# id and name.
# • Class marks is derived from class student and has a function that displays all the
# marks obtained in the courses by the students. i.e. marks_algo,
# marks_dataScience, marks_calculus.
# • Class result is derived from class marks. This class has a function that calculates
# the total marks and then calculates the average marks. It then displays both the
# total and the average marks.


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")


class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        # Call the constructor of the base class Student
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print(f"Marks in Algorithm: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_dataScience}")
        print(f"Marks in Calculus: {self.marks_calculus}")


class Result(Marks):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_algo, marks_dataScience, marks_calculus)

    def display_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")


student1 = Result(0057, "Rija", 85, 90, 92)


print("Student Information:")
student1.display_student_info()

print("\nMarks Information:")
student1.display_marks()

print("\nResult Information:")
student1.display_result()
