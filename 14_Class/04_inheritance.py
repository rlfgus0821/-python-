# 클래스 상속 : 부모클래스로부터 상속받은 필드와 메소드를 이용, 변경
# 메소드 재정의 : 상속받은 메소드를 다시 정의
# 기시성 : 정보은닉 / 비공개 필드, 비공개 메소드
# 비공개 필드는 직접 접근가능한 메소드를 구현하여 사용하거나
# 데코레이터(@property)를 이용하여 직접 사용

class car:
    def __init__(self,speed=0,color=''):
        self.speed = speed
        self.color = color
    def drive(self):
        print(f'{self.speed}로 주행한다.')

class truck(car):
    def __init__(self,speed,color,load):
        super().__init__(speed,color)
        self.load = load
    # 메소드 재정의(overriding)
    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 주행한다')
    def loading(self):
        print(f'최대{self.load}양의 짐을 운발할 수 있는 트럭')

car1 = car()
truck1 = truck(0,'blue',5)
truck2 = truck(10,'black',9)
truck3 = truck(20,'white',18)
for i in [car1, truck1, truck2, truck3]:
    i.drive()
car1.drive()
truck1.drive()
truck1.loading()

class animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')

class cat(animal):
    def talk(self):
        return 'Meow!'
class dog(animal):
    def talk(self):
        return 'woof woof!'

animals = [cat('Missy'), cat('Mr.Mistoffelees'),dog('zion')]
for animal in animals:
    print(animal.name + ': ' + animal.talk())

class product:
    pass
class inventory:
    def __init__(self):
        self.__items = []
    def addnewitem(self, product):
        if type(product) == product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')
    def getnumofitems(self):
        return len(self.__items)
    def getitems(self):
        print(self.__items)

# 데코레이터를 사용하여 비공개 필드를 직접접근하여 사용
    @property
    def items(self):
        return self.__items
myinvent = inventory()
myinvent.addnewitem(product())
myinvent.addnewitem(product())
myinvent.addnewitem(product())
myinvent.__items # 오류 발생 : 비공개 필드
myinvent.getitems()
print(myinvent.items)