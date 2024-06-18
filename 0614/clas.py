class Cat:
    def __init__(self,name,color): #생성자(객채를 초기화 함)
        #객채의 고유변수들을 기술함
        self.name = name
        self.color = color

    def meow(self):
        print(f"my name {self.name}, color {self.color}, meoo")


nabi = Cat('nabi', 'black')

nero = Cat('nero','white')

mimi = Cat('mimi', 'red')

nabi.meow()
nero.meow()
mimi.meow()

print(nabi.__dict__)
print(Cat.__dict__)