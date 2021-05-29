calls=int(input("enter the number of calls:- "))
if (calls<=100):
    print ("calls cost per month is" ,200)
elif(calls>100 and calls<150):
    print("call cost per month is ", 200+(0.60*(calls-100)))
elif(calls>150 and calls<200):
    print("call cost per month is ", 200+(0.60*50)+(0.50*(calls-150)))
elif(calls>200):
    print("call cost per month is ", (200+(0.60*50)+(0.50*50)+(0.40*(calls-200))))
    
    
