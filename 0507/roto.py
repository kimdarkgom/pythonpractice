import random

def gNum():
    return random.randrange(1,46)


for i in range(6):
    loto = []
    while True:
        num = gNum()

        if loto.count(num) == 0:
            loto.append(num)

        if len(loto)>=6:
            break
    loto.sort()
    print(loto)



