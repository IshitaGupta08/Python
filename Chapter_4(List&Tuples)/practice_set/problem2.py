#WAP to accept marks of 6 student and display them in a sorted manner
marks = []

f1 = int(input("Enter marks name"))
marks.append(f1)
f2 = int(input("Enter marks name"))
marks.append(f2)
f3 = int(input("Enter marks name"))
marks.append(f3)
f4 = int(input("Enter marks name"))
marks.append(f4)
f5 = int(input("Enter marks name"))
marks.append(f5)
f6 = int(input("Enter marks name"))
marks.append(f6)
marks.sort() #yaha marks.sort kara h kyuki marks sorted manner me dene h to sare marks user se input kara ke tab sort karege
#make sure ke jab bhe hum user se marks input kara rahe h to wo int ke form me he hone chaiye string ke nhi 
print(marks)