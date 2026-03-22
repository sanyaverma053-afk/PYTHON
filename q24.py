
#  Q2. Menu-driven program to:
# 1 → Check even or odd
# 2 → Check positive or negative
# 3 → Find square of a number


def function():
    num=int(input("enter any number"))
    if num%2==0:
        print("even")
    else:
        print("odd")

def numbers ():
    num=int(input("enetr a number"))
    if num>0:
        print("positive")
    else:
        print("negative")
def square():
    num=int(input("enter a number"))
    if num>=0:
        print(num**2)
    else:
        print("invalid")
while True:
    print("\n____menu____")
    print("1. function")
    print("2. numbers")
    print("3. square")
    print("4.exit")
    
    choice=input("enter your choice")
    if choice=="1":
        function()
    elif choice=="2":
        numbers()
    elif choice=="3":
        square()
    elif choice=="4":
        print("exit")
        break
    else:
        print("invalid choice please try again")
