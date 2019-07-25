import random

mylist = []
num = int(input('How many random numbers do you want?: '))
for i in range(0,num):
    x = random.randint(1,10)
    mylist.append(x)

print(mylist)
