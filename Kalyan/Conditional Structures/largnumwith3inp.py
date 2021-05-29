m=int(input("enter first number-"))
n=int(input("enter the secoend number-"))
p=int(input("enter the third number-"))
if(m>n):
    if(m>p):
        print("biggest number is-", m)
    else:
        print("biggest number is-", p)
else:
    if(n>p):
        print("biggest number is-", n)
    else:
        print("biggest number is-", p)
        
