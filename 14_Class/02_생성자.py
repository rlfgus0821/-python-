# 생성자(constructor)
# def __init__(self, *args):
#       필드(변수) 초기화

# __메서드명__( )  : 예약함수

# 비공개 필드와 메서드 : 정보은닉(encapsulation)
# __변수명 : 비공개 필드 => 클래스 내부에서에서만 사용
#    비공개필드는 필드 접근 가능한 메서드를 정의하여 이용
# __메서드명( )  => 비공개메서드
#   - 클래스 내부에서만 사용가능한 메서드
#   - 비공개메서드를 접근할 수 있는 메서드를 구현

class Car:
    def __init__(self, color, modelN, date, model='BMW'): # 생성자
        self.color = color
        self.speed = 0
        self.model = model
        self.modelN =modelN
        self.__date = date

    def __modelN(self):
        return self.modelN

    def drive(self):
        self.speed = 10

    def print_date(self):
        print('제조연월일은', self.__date)

    def print_info(self):
        print('자동차번호:', self.__modelN())
        print('자동차색상:', self.color)
        print('자동차모델:', self.color )
        self.print_date()

car1 = Car('red', 'a12345', '2024-01-01', 'BMW' )
car2 = Car('black', 'a12346', '2020-01-30', 'Nexo')
car3 = Car('black', 'a12349', '2021-12-30')
print(car1.color)
print(car2.color)
print(car1.model)
# print(car1.__date)  # 비공개 필드는 직접 사용불가
car1.print_date()
print(car3.model)
# car1.__modelN()  # 비공개 메서드는 직접사용불가

car1.print_info()