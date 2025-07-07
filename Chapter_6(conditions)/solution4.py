# Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
# fruit = "Banana"
fruit = input("Enter the fruit name: ")
# color = "yellow"
color = input("Enter the color: ")
if fruit == "Banana" or fruit == "banana":
    if color == "yellow":
        print("Ripe")
    elif color == "green":
        print("Unriped")
    elif color == "brown":
        print("Overriped")
    else:
        print("Unknown banana color")
        
# for multiple fruits

elif fruit == "Mango" or fruit == "mango":
    if color == "yellow":
        print("Ripe")
    elif color == "green":
        print("Unriped")
    elif color == "black":
        print("Overriped")
    else:
        print("Unknown mango color")

elif fruit == "Apple" or fruit == "apple":
    if color == "red":
        print("Ripe")
    elif color == "green":
        print("Unriped")
    elif color == "brown":
        print("Overriped")
    else:
        print("Unknown apple color")

else:
    print("Fruit not supported")  