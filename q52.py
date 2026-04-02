
# Q1. Create a class Student with attributes name and marks.
#  Take input from the user and display the details.



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


name=input("enter the name")
marks=int(input("enter marks"))
s=Student(name,marks)
s.display()
