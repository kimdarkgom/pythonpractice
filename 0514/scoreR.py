from score import *

L = []
a,b,c = map(int, input("three grade in : ").split())

L.append(a)
L.append(b)
L.append(c)

msum = sum(L)
mavg = avg(msum, L)
mgrade = grade(mavg)

print("sum : %d"%msum)
print(f"avg {mavg:.1f}")
print(mgrade 1)