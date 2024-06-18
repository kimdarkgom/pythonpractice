def add(x,y):
    return x + y
print("def : ",add(3,4))

add = lambda x, y : x+y
print("out lambda : ",add(3,4))

print("in lambda : ",(lambda x,y : x+y)(3,4))

sub = lambda x,y : x-y
print(sub(3,4))



import random as r

L = []
for i in range(10):
    L.append(r.randint(10,40))
print(L,"\n")
print("Wkr")
for i in filter(lambda x : x%2==0, L):
    print(i, end=' ')

