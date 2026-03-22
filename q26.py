
# Q4.Menu-driven program to:
# 1 → Check vowel or consonant
# 2 → Check uppercase or lowercase



def character_check():
    char=input("enter character: ") 
    char.lower()
    vowels=["a","i","e","o","u"]
    if char in vowels:
        print("vowel")
    else:
        print("consonant")

def character_size():
    char=input("enter character ")
    if  char.isupper():
        print("uppercase letter ")
    elif char.islower():
        print("lowercase letter ")
    else:
        print("not existed ")
      
while True:
    print("\n___menu____")
    print("1.character_check ")
    print("2.character_size ")
    print("3.exit ")

    choice=input("enter choice ")
    if choice=="1":
        character_check()
    elif choice=="2":
        character_size()
    elif choice=="3":
        print("exit")
        break
    else:
        print("invalid please try again")
      
