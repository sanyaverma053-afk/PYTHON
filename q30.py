
# Q8.Menu-driven program to:
# 1 → Convert lowercase to uppercase.
# 2 → Convert uppercase to lowercase (using ASCII).

 
def ascii_value():
    ch = input("Enter a character: ")
    print("ASCII value =", ord(ch))

def character_type():
    ch = input("Enter a character: ")
    if ch.isalpha():
        print("Alphabet")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special Character")

while True:
    print("\n___ MENU ___")
    print("1. ASCII value of character")
    print("2. Check character type")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ascii_value()
    elif choice == "2":
        character_type()
    elif choice == "3":
        print("Exit program")
        break
    else:
        print("Invalid choice, try again")
