a = 20
def f1():
    global a
    a = 10
    print("f => %d"%a)


def f2():

    print("f2 => %d" % a)


f1()
f2()