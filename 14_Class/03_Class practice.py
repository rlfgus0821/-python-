# 실습1. Dog클래스를 정의하고, Dog 인스턴스 생성하여 표현하는 코드 작성
# 예제. Dog 클래스

class Dog:
    dog_id = 0   # 클래스 변수
    def __init__(self, name='', breed='', size='', age=0, color=''):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
        Dog.dog_id = Dog.dog_id + 1

    def eat(self, food):
        print(f'{self.name}이(가) {food}를 먹는다')

    def sleep(self):
        print(f'{self.name}이(가) 잠잔다')

    def sit(self):
        print(f'{self.name}이(가) 앉아있다')

    def run(self):
        print(f'{self.name}이(가) 뛴다')

    def __repr__(self):
        return f'{self.name}의 품종: {self.breed}, 나이:{self.age}'


dog1 = Dog('삐삐', '말티즈', 'small', 2, 'white')
print(f'dog1의 id {dog1.dog_id}')

dog2 = Dog('벤', '추추', 'medium', 3, 'brown')
print(f'dog2의 id {dog2.dog_id}')

dog3 = Dog('뭉치', '진돗개', 'medium', 1, 'white')
print(f'dog3의 id {dog3.dog_id}')

dog1.eat('개껌')
dog1.sit()
print(dog1)
print(dog2)
dog4 = Dog()
print(f'dog4의 id {dog4.dog_id}')

# 인스턴스 변수 : 인스턴스가 소유하고 있는 변수
# 클래스 변수 : 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수
#   클래스이름.클래스변수명 으로 메서드 내부에서 사용하고
#   인스턴스이름.클래스변수명으로 사용

# 실습2. Line 클래스
# https://docs.python.org/ko/3/reference/datamodel.html
class line:
    def __init__(self,len): # 생성자
        self.len = len
        print(f'{self.len}길이의 선이 생성되었습니다.')
    def __del__(self):      # 소멸자
        print(f'{self.len}길이의 선이 삭제되었습니다.')
    def __repr__(self):     # print문을 사용하기 위해 return값 반환
        return f'선의 길이 : {self.len}'
    def __str__(self):      # print문을 사용하기 위해 return값 반환
        return f'{self.len}'
    def __add__(self, other): # 더하기
        return self.len + other.len
    def __sub__(self, other):
        return self.len - other.len
    def __lt__(self, other):
        return self.len < other.len
    def __gt__(self, other):
        return self.len > other.len
    def __le__(self, other):
        return self.len <= other.len
    def __ge__(self, other):
        return self.len >= other.len
    def __eq__(self, other):
        return self.len == other.len
    def __ne__(self, other):
        return self.len != other.len

line1 = line(10)
line2 = line(40)
print(line1)
print(line2)
print(line1 + line2)
print(line1 - line2)
print(line1 >= line2)

if line1 > line2:
    print('선 1이 길어요')
else:
    print('선 2가 길어요')
