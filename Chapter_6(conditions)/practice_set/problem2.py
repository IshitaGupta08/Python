#WAP to find out whether a student passed or failed if it required a total of 40% and 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user
marks1 = int(input("Enter the marks1: "))
marks2 = int(input("Enter the marks2: "))
marks3 = int(input("Enter the marks3: "))

#check for total percentage
total_percentage = ((marks1 + marks2 + marks3)/300)*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Pass")
else:
    print("You are fail, try next year")
    
