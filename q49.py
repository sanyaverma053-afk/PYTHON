
# Q. Create a class Laptop with constructor having attributes ram, brand, and price. 
# Print the values using an object.


class Laptop:
    def __init__(self,ram,brand,price):
        self.ram=ram
        self.brand=brand
        self.price=price
    def display(self):
        print("ram:",self.ram)
        print("brand:",self.brand)
        print("price:",self.price)

ram=int(input("enter ram"))
brand=input("enter brand")
price=float(input("enter price"))
l=Laptop(ram,brand,price)
l.display()
