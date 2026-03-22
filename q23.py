
#MENU DRIVEN PROGRAM

# Q1. Create a menu-driven program to:
# 1 → Add two numbers
# 2 → Subtract two numbers
# 3 → Multiply two numbers
# 4 → Divide two numbers


def add():
    a=int(input("enter a numbers"))
    b=int(input("enter  another numbers "))
    print("sum=",a+b)
def subtract():
    a=int(input("enter  a number"))
    b=int(input("enter another number"))
    print("diff=",a-b)
def multiply():
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    print("mul=",a*b)
def divide():
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    if b!=0:
        print("div=",a/b)
    else:
        print(" division not possible")
while True:
    print("\n_____menu_____")
    print("1. add two number")
    print("2.subtract two number")
    print("3.multiply two number")
    print("4.divide two number")
    print("5.exit")

    choice=input("enter your choice")
    if choice=="1":
              add()
    elif choice=="2":
        subtract()
    elif choice=="3":
        multiply()
    elif choice=="4":
        divide()
    elif choice=="5":
        print("exit program")
        break
    else:
        print("invalid choice please try again")
