#WAP to find out whether a given name is present in a list or not
l = ["Ishita", "Krati", "Riya", "Ishu"]

name = input("Enter the name: ")
if(name in l):
    print("Your is present in the list")
else:
    print("Your name is not present in the list")