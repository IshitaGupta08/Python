# name = "Ishita"

# nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)

# print(nameshort)

# charater1 = name[1]
# print(charater1)

def print_full_name(first_name,last_name):
    print(f"Hello {first_name} {last_name}! You just delved into python.")
    print("Hello "+ first_name +" "+ last_name +" ! You just delved into python.")
    print("Hello {} {}! You just delved into python.".format(first_name,last_name))
first_name = input()
last_name = input()
print_full_name(first_name,last_name)
