def f(**p):
    for k in p.keys():
        print("%s --> %d"%(k,p[k]))

f(t = 9, s = 7, g= 4, b= 4)