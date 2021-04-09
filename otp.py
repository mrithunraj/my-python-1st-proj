import random
b=random.randint(1000,1500)
print(b)
a=int(input("enter otp to check"))


if a==b:
    print("the otp is correct")
else:
    print("the otp is not correct")

#print(random.random())
#print(random.randint(1000,1500))
#print(random.randrange(1,6))
