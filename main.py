from root import *


print("Number Kundali...!")
num =int(input("Enter number = "))

print("select operation\n"
"1 Square\n"
"2 Cube\n"
"3 Factorial\n"
"4 Square root\n"
"5 Even or odd\n")
c = int(input("select operation = "))

if (c==1):
    sqr = num ** 2
    print("Square of ",num,"is",sqr)

elif (c==2):
    cub = num ** 3
    print("Cube of ",num,"is",cub)

elif (c==3):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of ",num,"is",fact)

elif(c==4):
    square_root =math.sqrt(num)
    print("Square root of ",num,"is",square_root)

elif(c==5):
    if(num%2==0):
        print(c," is Even number")
    else:
         print(c,"is Odd number")
         





