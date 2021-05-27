#f1=open("myfile.txt","x")
f1=open("C:/Users/T450s/PycharmProjects/Practiceprograms/PythonPrograms/myfile.txt","w")
L=["Python script is more flexible than Java script.","\nI like to learn Python."]
f1.write("Do you know?\n")
f1.writelines(L)
f1.close()
f1=open("C:/Users/T450s/PycharmProjects/Practiceprograms/PythonPrograms/myfile.txt","a")
f1.write("\nHello Everyone!")
f1.write("\nThis is my first attempt to write to a file in Python.")
f1.write("\nI'll first open the file and then write.")
f1.write("\nFinally,I'll close it.")
f1.close()
print("********************************")
f1=open("C:/Users/T450s/PycharmProjects/Practiceprograms/PythonPrograms/myfile.txt","r")
print(f1.read())
print("**************************")
line=f1.readline()
#print(line)
lines=f1.readlines()
for line in lines:
   print(line)

f1.close()
f1=open("C:/Users/T450s/PycharmProjects/Practiceprograms/PythonPrograms/myfile.txt","a+")
f1.write("\nInsert First line")
f1.write("\nAppend Next line")
f1.seek(0)
print(f1.read())
f1.close()
print("*******************************")
print("\n\nHow to read a file line-by-line using a while loop?\n")
f1=open("C:/Users/T450s/PycharmProjects/Practiceprograms/PythonPrograms/myfile.txt","r")
while f1:
   line=f1.readline()
   print(line)
   if line== "":
      break
f1.close()




