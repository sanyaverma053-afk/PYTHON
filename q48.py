
#Q. create a class employee with attributes name and salary .
# create classes manager and intern that  inherit employee class and has attributes bonus in manager class and stipend in intern class
# both the  manager and intern will have total_pay()  as function that will calculate the total pay as salary +bonus for manager and salary +stipend for intern .
# finally display the intern in each class


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_pay(self):
        return self.salary + self.bonus

    def display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", self.bonus)
        print("Total Pay:", self.total_pay())
    
class Intern(Employee):
    def __init__(self, name, salary, stipend):
        super().__init__(name, salary)
        self.stipend = stipend

    def total_pay(self):
        return self.salary + self.stipend

    def display(self):
        print("Intern Details:")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Stipend:", self.stipend)
        print("Total Pay:", self.total_pay())
    
m1 = Manager("Amit", 50000, 10000)
i1 = Intern("Riya", 15000, 5000)
m1.display()
i1.display()
