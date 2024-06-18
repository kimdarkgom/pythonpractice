import random as r


def evenAdd(L):
    print("L even add : ",end="")
    res = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            res += L[i]

    return res

def evenAvg(total,L):
    print("L even avg : ",end= "")
    resAvg = 0
    L2 = []
    for i in range(len(L)):
        if L[i] % 2 ==0:
            L2.append( L[i])

    resAvg = total / len(L2)
    return resAvg


def evenCount(L):
    print("L even count : ",end="")
    resC = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            resC+=1

    return resC


if __name__ == '__main__':

    L = []

    for i in range(10):
        L.append(r.randint(1,10))
    print(L)

    hab = evenAdd(L)
    print(hab)
    avg = evenAvg(hab, L)
    print("%.1f"%avg)
    count = evenCount(L)
    print(count)