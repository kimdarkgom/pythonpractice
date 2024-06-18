#1부터 입력 숫자까지의 합
def hab(n):
    hab = 0
    #3. 함수 호출시
    #n = int(input("num :"))
    for i in range(n+1):
        hab += i
    #2. 함수에서 출력
    #print(f"1 ~ {n} hab :  {hab}")
    #2. 함수에서 출력시 return없어도 됨
    return hab

num = int(input("num :"))

res = hab(num)

#1. 메인에서 출력
print(f"1 ~ {num} hab :  {res}")

#2. return없이
#hab(num)

#3. 함수만 호출
#hab()