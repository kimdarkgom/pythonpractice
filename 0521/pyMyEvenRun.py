import random as rd
from pyMyEven import *

L = []
for i in range(10):
    L.append(rd.randint(1,10))

print(L)

hab = evenAdd(L)
print(hab)
avg = evenAvg(hab, L)
print("%.1f"%avg)\
count = evenCount(L)
print(count)