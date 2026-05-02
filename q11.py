
#question11
#WAP to input three sides of a triangle and check:
#triangle is valid or not
#if valid, check whether it is Scalene, Isosceles or Equilateral

a=int(input("enter side of triangle"))
b=int(input("enter side of triangle"))
c=int(input("enter side of triangle"))
if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        print("equilateral triangle")
    elif a==b or b==c or  c==a:
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("invalid")
