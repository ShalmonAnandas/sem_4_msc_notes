class Employee:
    def __init__(self, Emp_id, Emp_name, Emp_salary):
        self.id = Emp_id
        self.name = Emp_name
        self.salary = Emp_salary
    def display(self):
        print("Empoyee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        return

empid = input("Enter Employee ID:")
name = input("Enter Employee name:")
salary = input("Enter Employee salary:")

obj = Employee(empid, name, salary)
obj.display()
