def sum(L): #리스트를 받음
    res = 0
    for i in range(len(L)):
        res += L[i]
    return res

def avg(total, L):
    res = total/len(L)

    return res

def grade(a):
    if a >=90:
        res='a'
    elif a>=80:
        res='b'
    elif a>=70:
        res='c'
    elif a>=60:
        res='f'

    return res

if __name__ == '__main__':#확인
    L = [90, 90, 90]
    hab = sum(L)
    print(hab)

    mavg = avg(hab, L)
    print(mavg)

    mgrade = grade(mavg)
    print(mgrade)