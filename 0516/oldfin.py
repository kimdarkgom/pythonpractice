import random as r
def adult_func(n):
    if n >= 19:
        return True
    else:
        return False

L = []
for i in range(10):
    L.append(r.randint(10,40))

print("older")

for a in filter(adult_func(),L):
    print(a, end=' ')
