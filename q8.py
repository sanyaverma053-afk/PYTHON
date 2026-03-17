#question 8
#A shop gives 10% discount if bill amount is above 1000.
#Calculate final amount with/without discount.

bill=int(input("enter bill amount"))
if bill>1000:
    discount=bill*10/100
    final_amount=bill-discount
    print("discount applied",discount)
    print("final amount after discount",final_amount)
else:
    print("no discount applied")
