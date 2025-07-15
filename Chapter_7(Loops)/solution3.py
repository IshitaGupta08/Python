#isme hame table print karani h or 5 no ko skip karna h to uske liye skip karne ke liye hum continue keyword ka use karege
# continue ka use karke us particular step ko skip kar sakte h baki sab as it is he rahata h
number = 3

for i in range(1,11):
    if i == 5:
        continue
    print(number,"X",i,"=",number * i)
    