class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

S1 = Student("divya", 19)
S1.myfunc()
