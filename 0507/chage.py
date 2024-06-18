def f(v1,v2,v3=0):
    #f(v1=0,v2,v3)는 오류
    return v1+v2+v3

hab= f(10,20)
print(hab)

hab = f(10,20,30)
print(hab)