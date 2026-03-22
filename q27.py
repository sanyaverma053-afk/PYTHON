
# Q5.Menu-driven program to perform:
# 1 → Check prime number
# 2 → Check palindrome number
# 3 → Check Armstrong number


def prime_check():
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            return
    print("Prime number")

def palindrome_check():
    num = input("Enter a number: ")
    if num == num[::-1]:
        print("Palindrome number")
    else:
        print("Not a palindrome number")

def armstrong_check():
    num = int(input("Enter a number: "))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

while True:
    print("\n___ MENU ___")
    print("1. Prime number check")
    print("2. Palindrome number check")
    print("3. Armstrong number check")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        prime_check()
    elif choice == "2":
        palindrome_check()
    elif choice == "3":
        armstrong_check()
    elif choice == "4":
        print("Exit program")
        break
    else:
        print("Invalid choice, try again")
