"""기본
def add(n1, n2):#함수 정의
    r = n1 + n2
    return r#결과 반환
"""

#연산자 추가
def calc(n1, n2 ,opr):
    if opr == '+':
        r = n1 + n2
    elif opr == '-':
        r = n1 - n2
    elif opr == '*':
        r = n1 * n2
    elif opr == '/':
        r = n1 / n2
    else:
        print("err")
    return r


num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
#연산자 추가
opr = input("+ - * / :")

#hab = add(num1, num2,opr)#기본

res = calc(num1, num2, opr)

#기본
#print("%d + %d = %d"%(num1, num2, hab))

#연산자 추가
print("%d %c %d = %.1f"%(num1, opr, num2, res))