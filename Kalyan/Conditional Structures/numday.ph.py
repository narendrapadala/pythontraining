num=int(input("enter a value from 1 to 7- "))
day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
for i in range(1,num+1):
    if(i==num):
        print(day[i-1])
