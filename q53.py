
# Q2. Write a class Rectangle that calculates area and perimeter using method

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

length=float(input("enter length of rectangle"))
breadth=float(input("enter breadth of rectangle"))
r=Rectangle(length,breadth)

print("Area of rectangle:", r.area())
print("Perimeter of rectangle:",r.perimeter())

  
