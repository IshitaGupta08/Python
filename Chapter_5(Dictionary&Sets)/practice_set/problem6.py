#create empty dictionary. allow 4 friends to enter their favourite language as a value and use key as their names. assume that the name are unique
d = {}

name = input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
name = input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
name = input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})
name = input("Enter the name: ")
lang = input("Enter the language: ")
d.update({name:lang})

print(d)