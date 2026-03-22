

# Q7.Menu-driven program for string operations:
# 1 → Find length of string.
# 2 → Reverse the string.
# 3 → Check palindrome string.


def length_check():
    str=input("enter string")
    print("length of string",len(str))
def reverse_check():
    str=input("enter string")
    print("reversed",str[::-1])
def palindrome_check():
    num = input("Enter a number: ")
    if num == num[::-1]:
      print("Palindrome number")
    else:
        print("Not a palindrome number")
    
while True:
    print("1.length_check ")
    print("2.reverse_check")
    print("3.palindrome_check")
    print("4.exit")

    ch=input("enter choice ")
    if ch=="1":
        length_check()
    elif ch=="2":
        reverse_check()
    elif ch=="3":
        palindrome_check()
    elif ch=="4":
        print("exit")
        break
    else:
        print("invalid please try again")
