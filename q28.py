
# Q6. Menu-driven program to:
# 1 → Find largest of three numbers
# 2 → Find smallest of three numbers


def largest_check():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    c=int(input("enter 3rd number"))
    if a>b:
        print("a is largest")
    elif b>c:
        print("b is largest ")
    elif c>a:
        print("c is largest ")
    else:
        print("exit")
def  smallest_check():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    c=int(input("enter 3rd number"))
    if a<b:
        print("a is smallest")
    elif b<c:
        print("b is smallest")
    elif c<a:
        print("c is smallest")
    else:
        print("exit")

while True:
    print("/n___menu___")
    print("1.largest_check")
    print("2.smallest_check")
    print("3.exit")

    ch=input("enter your choice ")
    if ch=="1":
        largest_check()
    elif ch=="2":
        smallest_check()
    elif ch=="3":
        print("exited")
        break
    else:
        print("invalid please try again")
