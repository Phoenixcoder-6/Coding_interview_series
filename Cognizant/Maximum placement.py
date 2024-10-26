cse= int(input("Enter number of students placed in cse:"))
ece= int(input("Enter number of students placed in ece:"))
mech= int(input("Enter number of students placed in mech:"))
if cse>ece and cse>mech:
    print("Maximum placement:",cse, "in department cse.")
elif ece>cse and ece>mech:
    print("Maximum placement:",{ece},"in department ece.")
else:
    print("Maximum placement:",{mech},"in department mech.")





