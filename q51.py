
#oops


# a python class person contains an attributes name .
# now create a class employee that inherit person and has attributes emp_id and salary .
# the employee class will be inherited by class manager and 
# the manager class has team_size >=5 and salary and salary>=50000 
# display the name and emp_id of the employee and print you are eligible ,
# otherwise display you are not eligible


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, emp_id, salary):
        super().__init__(name)
        self.emp_id = emp_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size

    def check_eligibility(self):
        if self.team_size >= 5 and self.salary >= 50000:
            print("Name:", self.name)
            print("Employee ID:", self.emp_id)
            print("You are eligible")
        else:
            print("Name:", self.name)
            print("Employee ID:", self.emp_id)
            print("You are not eligible")

name = input("Enter name: ")
emp_id = input("Enter employee ID: ")
salary = int(input("Enter salary: "))
team_size = int(input("Enter team size: "))

m = Manager(name, emp_id, salary, team_size)
m.check_eligibility()
