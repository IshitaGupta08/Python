# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_shot = True # yaha hum boolean value he rakhage ke kisi ne liya h ya nhi to true ya false he rahe rahega yaha

if extra_shot :
    coffee = order_size + " coffee with extra shot"
else:
    coffee = order_size + "coffee"
    
print("Order :", coffee)