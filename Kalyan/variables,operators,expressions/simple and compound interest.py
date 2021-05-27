p=float(input("enter principal amount"))
r=float (input("enter annual rate oof interest"))
t=float(input("enter time in number of years"))

si=p*r*t/100

ci=p*(1+r)**t

print("simple interest is",si)
print("compound interest is",ci)
