
# Q.Menu-driven program using functions:
# 1 → Factorial of a number
# 2 → Fibonacci series
# 3 → Prime number ch


def armstrong():
    n = int(input("Enter a number: "))
    temp = n
    sum = 0
    while temp > 0:
        d = temp % 10
        sum = sum + d**3
        temp = temp // 10
    if sum == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

  
def palindrome():
    n = int(input("Enter a number: "))
    temp = n
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    if rev == n:
        print("Palindrome number")
    else:
        print("Not a Palindrome number")

def prime():   
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not a Prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")

while True:
    print("\n___ MENU ___")
    print("1. Armstrong number")
    print("2. Palindrome number")
    print("3. Prime number")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
              armstrong()
    elif choice == "2":
        palindrome()
    elif choice == "3":
        prime()
    elif choice == "4":
        print("Exit program")
        break
    else:
        print("Invalid choice, try again")
