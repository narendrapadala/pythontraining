x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
z = int(input("Enter third number"))

if x>y and x>z:
    print("X is the largest number",x)
elif y>z:
    print("Y is the largest number :",y)
else:
    print("z is the largest number :",z)