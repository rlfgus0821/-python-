# 인스턴스(instance) 메서드 :
#   -가장 기본이 되는 클래스의 메서드
#   - 인스턴스 메서드의 첫번째 매개변수는 항상 self로 해당클래스의 인스턴스 값이 넘어옴

# 정적(static) 메서드:
#   - @staticmethod 데코레이터를 이용하여 정의
#   - self인자가 필요없는 메서드
#   - 인스턴스의 속성에 접근불가
#   - 주로 유틸리티성 함수를 위한 용도로 사용
#   - 클래스의 어떤 속성에도 변화를 일으키지 않는 함수. 순수함수의 역할
#   - 클래스 내부에 위치하는 이유는 클래스와 연관이 높은 함수를 정의하고 싶을 때

# 클래스(class) 메서드:
#   - @classmethod 데코레이터를 이용하여 정의
#   - 메서드의 첫번째 매개변수로 cls를 사용
#   - 클래스 자체가 넘어옴.
#   - 클래스의 속성에 접근 가능
#   - 팩토리 메서드(객체생성)를 작성하거나, 클래스 속성(변수)에 접근하기 위해 사용

class Person:
    count = 0  # 클래스 변수

    def __init__(self, name='myTest'):
        self.name = name
        Person.count += 1

    def print_name(self):  # 인스턴스 메서드
        print(self.name)

    @staticmethod
    def to_upper(text):
        # name = self.name  # 자신의 변수 접근 불가
        print(text.upper())

    @classmethod
    def print_count(cls):
        print(f'{Person.count}명이 태어났어요')  # cls로 클래스 속성 접근

    @classmethod
    def create(cls, name='noname'):
        p = cls()
        p.name = name# cls()로 인스턴스 생성
        return p


person1 = Person()
person1.print_name()
Person.to_upper(person1.name)
# person1.to_upper('James')
Person.print_count()
person2 = Person.create('James')
Person.to_upper('Alice')
Person.print_count()
person2.print_name()