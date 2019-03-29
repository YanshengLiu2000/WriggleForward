import random
l=[0,1,2,3,4,5,6,7,8,9]
for i in range(9,0,-1):
    r=random.randint(0,i-1)
    l[i],l[r]=l[r],l[i]
print(l)