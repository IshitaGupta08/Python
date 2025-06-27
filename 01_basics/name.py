def print_full_name(first_name,last_name):
    print(f"Hello {first_name} {last_name}! You just delved into python.") #here we use F string to put first and last name together
    print("Hello "+ first_name +" "+ last_name +" ! You just delved into python.") #here we use concatination of string
    print("Hello {} {}! You just delved into python.".format(first_name,last_name)) #here we use .format to put first and last name together
first_name = input("Enter the first name:")
last_name = input("Enter the last name:")
print_full_name(first_name,last_name)