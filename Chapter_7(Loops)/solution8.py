number = 29

is_prime = True  # hum man ke chal rahe h ke ye true h 

if number > 1:  #prime number bss apni table se he divide hote h kisi or ke se nhi or 1 se hote h to 1 se bade he sab no. check karne hote h
    for i in range(2, number):  #yaha humne number tak isliye liya h kyuki number +1 mtlb us same number se to wo obsivously divide hoga he to kyu he check kaarna
        if number % i == 0:  #yaha if laga ke ye check kara h ke khai wo number jo loop me bar ar number aa rahe h unme se kisi ek se bhe divide ho raha h to wo prime nhi ho sakta
            is_prime = False #or agar if ke comdition true hue ke number kisi bhe i number se divide hua to is_prime ko False kar do or loop break kar do
            break
        
print(is_prime) #otherwise prime number print kar do