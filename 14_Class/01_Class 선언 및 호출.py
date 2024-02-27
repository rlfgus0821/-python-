# 객체의 필요성

# 더하기 기능을 위한 계산기 구현

class addcal:
    def __init__(self):
        self.result = 0
    def adder(self, num):
        self.result += num
        return self.result

myadder = addcal()
myadder.adder(10)
myadder.adder(20)
myadder.adder(30)
print(myadder.result)

#1. class 선언
# 필드(변수)
# 메소드 정의
# self : 기존의 함수와 구분, 자신의 인스턴스임을 의미
# class 이름(상속class):
#    class변수 선언
#    메소드 정의 / def 메소드 이름(self, 매개변수들):

#2. 객체(인스턴스) 생성
# 이름 = class이름() : 생성

#3. class 사용 : 이름.메소드 이름

# 자동차 클래스 선언
class car:
    def drive(self):
        self.speed = 10
# 자동차 클래스 인스턴스 생성
car1 = car() # car() : 인스턴스 생성하는 생성자
car2 = car()
car3 = car()
# 클래스 실행
print(car1.speed) # 실행되기전이라 에러 발생
car1.drive()
print(car1.speed)

# car1과 car2의 메모리 주소가 다르다
print(type(car1),id(car1))
print(type(car2),id(car2))

# isinstance(인스턴스, 클래스) -> 클래스의 인스턴스인지 확인하는 함수
print(isinstance(car1, car))
a = int(10)
print(isinstance(a, int))
b = [1,2,3,4,5,2,'a']
print(isinstance(b, list))

# 인스턴스 생성 후 필드 추가
car1.color = 'red'
car1.speed = 0
print(car1.color, car1.speed)