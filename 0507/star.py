def func(*para):
    result = 0
    for i in para :
        result += i
    return result

hab = func(10,20)
print(hab)

hab = func(10,20,30)
print(hab)