import random as rn
L = [10,20,30,40,50]
print("randrange : ")
for i in range(10):
    print(rn.randrange(0,3),end =' ')

print("\nrandint : ")
for i in range(10):
    print(rn.randint(0,3),end =' ')

print("\nshuffle : ")
for i in range(10):
    print(rn.shuffle(L), end = ' ')

print("\nchoice : ")
for i in range(10):
    print(rn.choice(L), end = ' ')

print("\nsample : ")
for i in range(10):
    print(rn.sample(L,1), end= ' ')
