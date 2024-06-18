def add(n1, n2):
    r = n1 + n2
    return r
def sub(n1, n2):
    r = n1 - n2
    return r
def mul(n1, n2):
    r = n1 * n2
    return r
def div(n1, n2):
    r = n1 / n2
    return r
#메인

num1 , num2 = map(int,input("num1 num2 : ").split())

opr = input("+ - * / : ")

if opr == '+':
    res = add(num1, num2)
    print("%d %c %d = %d"%(num1,opr, num2, res))
elif opr == '-':
    res = sub(num1, num2)
    print("%d %c %d = %d" % (num1, opr, num2, res))
elif opr == '*':
    res = mul(num1, num2)
    print("%d %c %d = %d" % (num1, opr, num2, res))
elif opr == '/':

    if num2 == 0:
        print("n/0 x")
    else:
        res = div(num1, num2)
        print("%d %c %d = %.1f" % (num1, opr, num2, res))
else:
    print("err")