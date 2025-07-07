age = 25
day = "Wednesday"

price = 12 if age >= 18 else 8 # new way to write a summarized code isme wo agar if condition sahi hue to 12 le lega warna 8 value le lega
if day == "Wednesday":
    # price = price - 2
    price -=2
print("Ticket price for you is $",price)
# another way to write a code 
# if age >= 18:
#     price = 12
# else :
#     price = 8
# if day == "Wednesday":
#     price = price - 2
# print("the price of the ticket is $",price) # or ek or way h print karne ka 
# print(f"the price of the ticket is ${price}") # yaha {} iske ander ke price ko valid banane ke lye aage f string lagna imp h warna ye {} as a normal text print hoga iski value nhi aaegi iske ander
