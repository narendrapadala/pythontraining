with open('readwritepython.txt') as f:
    lines=f.readlines()
    for l in lines:
        print(l)
        f.close()
        
#f = open("readwritepython.txt", "r")
#print(f.read())
#f.close()
