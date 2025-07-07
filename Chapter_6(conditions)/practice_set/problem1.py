#WAP to find the greatest of four numbers enter by the user

a1 = int(input("Enter the 1st number: "))
a2 = int(input("Enter the 2nd number: "))
a3 = int(input("Enter the 3rd number: "))
a4 = int(input("Enter the 4th number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3", a3)
else:
    ("Greatest number is a4",a4)
    