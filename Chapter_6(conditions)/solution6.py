# <3 km: Walk, 3-15 km: Bike, >15 km: Car

distance = int(input("Enter the distance in Km: "))
# distance = 5

if distance < 3:
    print("Walk")
    # transport = "Walk"
elif distance <= 15:
    print("Bike")
    # transport = "Bike"
else:
    print("Car")
    # transport = "Car"
    
# print(transport)