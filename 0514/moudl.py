def func1():
    print("moudl.py > func1() call")

def func2():
    print("moudl.py > func2() call")


def func3():
    print("moudl.py > func3() call")

if __name__ == '__main__':#import는 안됨 메모리에 올라와 있기에 moudl.func1()으로 가
    func1()
    func2()
    func3()