
maths = int(input("Enter Marks in Maths :"))
science = int(input("Enter Marks in science :"))
english = int(input("Enter Marks in Maths :"))

average = (maths+science+english)/3

if average > 90 and average < 100:
    grade = 'A'
elif average >= 80 and average <= 89:
    grade = 'B'
elif average >= 70 and average <= 79:
    grade = 'C'
elif average >= 60 and average <= 69:
    grade = 'D'
else:
    grade = 'E'
print("Student's Grade is  :",grade)