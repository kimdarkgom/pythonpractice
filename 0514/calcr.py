from calc import *
import moudl
n1, n2 =  map(int, input("num two in :").split())
op = input("+-*/ :")

if op == '+':
    res = add(n1,n2)
    print(f"{n1} {op} {n2} = {res}")
elif op == '-':
    res = sub(n1,n2)
    print(f"{n1} {op} {n2} = {res}")
elif op == '*':
    res = mul(n1,n2)
    print(f"{n1} {op} {n2} = {res}")
elif op == '/':
    res = div(n1, n2)
    print(f"{n1} {op} {n2} = {res:.1f}")