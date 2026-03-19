
#question 9
# Input marks of 5 subjects.
# Calculate percentage and print grade using if-else.

# >=90 A  
# >=80 B  
# >=70 C  
# >=60 D  
# else Fail


marks=int(input("enter marks of five subject"))
if marks>=90:
    print("grade A ")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
elif marks>=60:
    print("grade D")
else:
    print("fail")
