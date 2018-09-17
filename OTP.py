import random
x=random.randint(100000,1000000)
print("x:"+ str(x))
print(x)
z=int(input("Enter the One Time Password: "))
for i in (0,3,1):
    if(z == x):
        print("succcess")
        break
    else:
        z=int(input("Enter the One Time Password:"))
