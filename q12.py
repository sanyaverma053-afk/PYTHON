#question 12
#Write a program to check whether a number is Armstrong Number.
a = int(input("Enter a number: "))
sum = 0
temp = a

while temp > 0:
    digit = temp % 10
    sum += digit ** 3   
    temp //= 10

if sum == a:
    print(a, "is an Armstrong number")
else:
    print(a, "is not an Armstrong number")
