# Make a class "Student"and make a function "Print_biodata" inside it. Pass name and age of
# student to constructor. Now access "Print_biodata" function using object to print name and
# age of student.

class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def Print_biodata(self):
    print(self.name,self.age)
   # print(self.age)

  # def getAge(self):
  #   print(self.age)

  # def setAge(self,age):
  #   self.age = age
  
student = Student('Rija' , 20)
student.Print_biodata()
