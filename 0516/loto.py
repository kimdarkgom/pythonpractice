import random as rd

for i in range(5):
    num = list(range(1,46))

    lotoNum = rd.sample(num,6)

    #print(lotoNum)

    lotoNum.sort()
    print(lotoNum)