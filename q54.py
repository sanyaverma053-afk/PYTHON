# Q. Create a class Car with attributes brand and model. Create 2 objects and display their values.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("brand name:",self.brand)
        print("model name:",self.model)

brand1=input("enter name of the brand")
model1=input("enter model of the car")
c1=Car(brand1,model1)

brand2=input("enter name of the brand")
model2=input("enter model of the car")
c2=Car(brand2,model2)

print("first car details")
c1.display()

print("second car details")
c2.display()
