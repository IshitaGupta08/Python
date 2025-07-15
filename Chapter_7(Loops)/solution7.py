while True:
    number = int(input("Enter the number: "))  # user se number lo
    if 1 <= number <= 10:                      # agar valid number hai
        print("Thanks")                        # message do
        break                                  # loop se bahar jao
    else:
        print("Invalid number, try again")     # galat input par dobara pucho
