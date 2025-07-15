numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0 # yaha ise 0 initlized karaa liya h taki isme iski value calculate kar sake

for num in numbers:
    if num >0 :
        positive_number_count += 1
print("Total postive count in number list is: ", positive_number_count)