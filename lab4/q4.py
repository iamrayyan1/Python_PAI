class Employee:
    def __init__(self):
        self.name = ""
        self.monthly_salary = 0.0
        self.tax_percentage = 2.0 

    def get_data(self):
        self.name = input("Enter your full name: ")
        self.monthly_salary = float(input("Enter your monthly salary: "))
       # self.tax_percentage = float(input("Enter tax percentage: "))
        self.tax_percentage = 2

    def salary_after_tax(self):
        tax_amount = (self.tax_percentage / 100) * self.monthly_salary
        salary_after_tax = self.monthly_salary - tax_amount
        return salary_after_tax

    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage


emp = Employee()
emp.get_data()
print(f"Salary after 2% tax: ${emp.salary_after_tax():.2f}")

  
new_tax = float(input("Enter new tax percentage to update: "))
emp.update_tax_percentage(new_tax)
print(f"Salary after tax with updated tax percentage: ${emp.salary_after_tax():.2f}")
