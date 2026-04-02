
# Q. Define a class Book with a constructor that initializes title and price. 
# Create an object and display the details.


class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def display(self):
        print("title :",self.title)
        print("price :",self.price)

title=input("enter the tite of book")
price=int(input("enter the price of book"))
b=Book(title,price)
b.display()
