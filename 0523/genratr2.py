def c_g():
    alist = range(1,4)

    for x in alist:
        yield x

myG =  c_g()

print(myG)

for n in myG:
    print(n, end=" ")

def c_g2():
    for x in range(4):
        yield x

myG2 =  c_g2()

for n in myG2:
    print(n, end=" ")

"""def c_g3():
    alist = range(1,4)

    for x in alist:
        return x#리턴은 안

myG3 =  c_g3()

print(myG3)

for n in myG3:
    print(n, end=" ")"""