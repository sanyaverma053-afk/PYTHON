
#question
# A library fine system:
# Return book in <5 days → No fine  
# 5-10 days → Rs 5/day  
# 10-30 days → Rs 10/day  
# >30 days → Membership cancelled
# Take number of late days and calculate fine.



days=int(input("enter  no of days you have book"))
if days<=5:
    print(" no fine")
elif days>5 and days<=10:
    fine=5*days
    print("RS 5 charge",fine)
elif days>10 and days<=30:
    fine=10*days
    print("RS 10 charge",fine)
else:
    print("membership cancelled")
