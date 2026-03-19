
#question 10
#Check if a character is vowel or consonant.

char=input("enter any character")
char=char.lower()
a=["a","i","e","o","u"]
if len(char)==1 and char.isalpha():
    if char in a:
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid input, enter a single letter")
