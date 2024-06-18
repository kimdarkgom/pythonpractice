import random as r

L = []
for i in range(10):
    L.append(r.randint(10,40))
print(L,"\n")
print("old")
oL = list( filter(lambda x : x>=19, L))
print(oL, end=' ')