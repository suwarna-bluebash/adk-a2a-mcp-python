# Task for OOPs: Build a class hierarchy for Person, Employee, and Manager with:
# Shared attributes: name, age
# Method override for get_role()
# Use super() in Manager

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def get_role(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    employee_list = []
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department
        Employee.employee_list.append(self)
    def get_role(self):
        super().get_role()
        print(f"{self.name} works in {self.department} department.")

class Manager(Employee):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age, department)
        self.team_members = []
        print(f"{self.name} is the manager of {self.department} department.")
        self.group_team_members() # to store the manager into the team where department is same
    def group_team_members(self):
        for emp in Employee.employee_list:
            if emp.department == self.department and emp.name != self.name:
                self.team_members.append(emp.name)
    def show_team_members(self):
        print(f"Team members under {self.name} in {self.department}: {self.team_members}")

obj2 = Employee("Soso", 28, "Artificial Intelligence")  # Created before manager
obj3 = Employee("Pokimon", 28, "Artificial Intelligence")
obj4 = Employee("Doriemon", 28, "Artificial Intelligence")  
obj1 = Manager("Suwarna Shukla", 23, "Artificial Intelligence")  # Now will pick up the employee
obj1.show_team_members()
