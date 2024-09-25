# A university is deciding to upgrade its system. In order to upgrade, you need to implement the following scenario: Note the following:
#  The class student has a function that displays information about the student i.e. id and name.
#  Class marks is derived from class student and has a function that displays all the marks obtained in the courses by the students. i.e. marks_algo, marks_dataScience, marks_calculus.
#  Class result is derived from class marks. This class has a function that calculates the total marks and then calculates the average marks. It then displays both the total and the average marks.
# In the main function you are required to do the following:
#  Create an object of the result class.
#  Then display the student details, the marks obtained in each courses and the total and
# the average marks.

class Student:
    def __init__(self, id, name) :
        self.id = id
        self.name = name
    
    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")

class Marks(Student):
    def __init__(self,id,name,marks_algo,marks_dataScience,marks_calculus):
        super().__init__(id,name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        super().display()
        print(f"Marks Algo: {self.marks_algo}")
        print(f"Marks DS: {self.marks_dataScience}")
        print(f"Marks Calculus: {self.marks_calculus}")

class Result(Marks):
    def __init__(self,id,name,marks_algo,marks_dataScience,marks_calculus):
        super().__init__(id,name,marks_algo,marks_dataScience,marks_calculus)
        self.total = 0
        self.avg = 0

    def calculate(self):
        self.total = self.marks_algo+self.marks_dataScience+self.marks_calculus
        self.avg = self.total/3

        print(f"The total marks for three subjects are: {self.total}")
        print(f"The average marks for three subject are: {self.avg}")

res = Result(230057 , "Rija Ali", 85 , 90 , 95)
res.display_marks()
res.calculate()
