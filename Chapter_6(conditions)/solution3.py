#A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
# marks = int(input("Enter the marks of the student: "))
marks = 100

if marks >=101:
    print("Please enter the valid marks")
    exit()

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")