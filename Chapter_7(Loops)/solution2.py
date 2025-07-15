# n = init(input("Enter the number:"))
n = 10
sum_even = 0

for i in range(1, n+1):  #yaha range batan hoti h ke kaha se start karke kaha tak leke jana h 
    if i % 2 == 0:
        sum_even += 1 # or i #yaha agar hum 1 likhte h to jitne bhe even number is range me present honge un sabke liye ye 1 ko add karega but agar hane actual me wo number he add krana h to hum 1 nhi i denge aise +=i

print("sum of even numbers is:", sum_even)