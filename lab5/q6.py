# Create a class called "Employee" with properties "name" and "salary". Add a method called "calculateBonus" that calculates a bonus amount based on the employee's salary. Managers get a bonus equal to 20% of their salary, while developers get a bonus equal to 10% of their salary. Then, create two subclasses called "Manager" and "Developer" that inherit from the Employee class. The Manager class should have a method called "hire" that logs a message indicating that the manager is hiring someone, while the Developer class should have a method called "writeCode" that logs a message indicating that the developer is writing code. Finally, create a subclass called "SeniorManager" that inherits from the Manager class and that should have the "calculateBonus" method to give senior managers a bonus equal to 30% of their salary.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def calc_bonus(self,salary):
       pass
        
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def hire(self):
        print("Hiring someone...")

    def calc_bonus(self):
        bonus = 0.2*self.salary
        return bonus
    
    def display(self):
        print(f"{self.name} has salary ${self.salary}")

class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def writeCode(self):
        print("Writing Code at the moment...")

    def calc_bonus(self):
      bonus = 0.1*self.salary
      return bonus
    
    def display(self):
     print(f"{self.name} has salary ${self.salary}")

class SenManager(Manager):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    
    def calc_bonus(self):
        bonus = 0.3*self.salary
        return bonus
    
    def display(self):
        print(f"{self.name} has salary ${self.salary}")

print("DEVELOPER..")
dev = Developer("Ali" , 100000)
dev.display()
dev.writeCode()
print(f"The bonus for developer is: {dev.calc_bonus()}")

print("MANGER..")
man = Manager("Hunaiza" , 150000)
man.display()
man.hire()
print(f"The bonus for Manager is: {man.calc_bonus()}")

print("SENIOR MANAGER..")
sen_man = SenManager("Rija" , 200000)
sen_man.display()
print(f"The bonus for Senior Manager is: {sen_man.calc_bonus()}")


        
