# Write a program that prompts the user to input a number.
# Program should display the corresponding days to the number.


day = int(input("Enter 1 to 7 Number : "))

if (day==1):
    print (day, "is Sunday")
elif (day==2):
    print (day, "is Monday")
elif (day==3):
    print (day, "is Tuesday")
elif (day==4):
    print (day, "is Wednesday")
elif (day==5):
    print (day, "is Thursday")
elif (day==6):
    print (day, "is Friday")
else:
    print(day, "Saturday")