
# Q3.Menu-driven program to:
# 1 → Find ASCII value of a character
# 2 → Convert ASCII to character


def find ():
    ch = input("Enter a character: ")
    print("ASCII value is:", ord(ch))

def convert ():
    num = int(input("Enter ASCII value: "))
    print("Character is:", chr(num))

while True:
    print("\n___menu___")
    print("1.find")
    print("2.convert")
    print("3.exit")

    choice=input("enter your choice")
    if choice=="1":
        find()
    elif choice=="2":
        convert()
          elif choice=="3":
        print("exit")
        break
    else:
        print("invalid please try again")
