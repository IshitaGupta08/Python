# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)

pet = input("Enter the pet name: ")
age = int(input("Enter the age: "))
if pet == "Dog":
    if age < 2:
        print("Puppy food")
    elif age >2:
        print("Adult food")
elif pet == "Cat":
    if age <2:
        print("baby cat food")
    elif age >2:
        print("Adult cat food")
else:
    print("Unknown pet")
    

        