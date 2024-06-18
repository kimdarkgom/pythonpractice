num = [-30,45,5,-90,20,53,77,36]

minusNum = list(filter(lambda x:x<0, num))

print(minusNum)

plusNum = [x for x in num if x>0]

print(plusNum)