def myDan(n): #한단을 출력
    for i in range(1,11):
        print("%d * %d = %d"%(n, i , n*i))
def myAllDan(): #구구단 전체
    for i in range(1,10):
        for j in range(1,10):
            print("%d * %d = %d"%(i, j , i*j))


#main
while True:
    chack = int(input("1 : 한번만 / 2 : 전채 / 0 : 종료 "))

    if chack == 1:
        dan = int(input("몇단 : "))
        myDan(dan)
    elif chack == 2:
        myAllDan()
    elif chack == 0:
        print("program end")
        break