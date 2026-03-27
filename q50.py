# Q. Write a program to take marks in 5 subjects and print total & percentage

s1=float(input("enter  1st subject marks"))
s2=float(input("enter  2nd subject marks "))
s3=float(input("enter 3rd subject marks"))
s4=float(input("enter  4th subject marks "))
s5=float(input("enter 5th  subject marks "))
total_marks=s1+s2+s3+s4+s5
percentage=float(total_marks/500)*100
print(total_marks)
print(percentage)
