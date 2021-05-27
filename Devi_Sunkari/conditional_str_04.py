
callsMade=int(input("Enter total calls made :"))

if callsMade<=100:
    telBill = 200

elif callsMade>100 and callsMade<150:
    callsMade = callsMade-100
    telBill = 200+(0.60*callsMade)

elif callsMade>150 and callsMade<=200:
    callsMade = callsMade - 150
    telBill = 200+(0.60*50)+(.50*50)
else:
    callsMade = callsMade - 200
    telBill = 200+(0.60*50)+(0.50*50)+(0.40*callsMade)

print("The total bill is :",telBill)