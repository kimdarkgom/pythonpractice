def even(n):
    l = []

    for i in range(n+1):
        if i %2 == 0:
            l.append(i)
    print("2 :",l)
    print("2 개수 :",len(l))
num = int(input("num : "))
even(num)
