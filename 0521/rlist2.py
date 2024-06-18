def square(n):
    return n**2

a=list(range(1,8))
#L=map(square, a) 반복문을 넣음 list를 붙여 리스트 형태로 변경
L=list(map(square, a))

print(L)