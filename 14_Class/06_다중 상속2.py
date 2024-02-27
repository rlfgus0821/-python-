# 다중 상속의 한 사례 : 다이아몬드 상속

class A:
    def greeting(self):
        print('안녕하세요 A입니다')

class B(A):
    def greeting(self):
        print('안녕하세요 B입니다')

class C(A):
    def greeting(self):
        print('안녕하세요 C입니다')

class D(B,C):
    pass

obj = D()
obj.greeting()

# 다이아몬드 상속 : 서로 다른 클래스에서 동일한 메소드를 상속받는 경우
# 메소드를 탐색하는 순서 : (Method Resolution Order : MRO)
# 왼쪽에서 오른쪽 순서로 메소드 탐색 : ex) D(B,C) B에서 C로
print(D.mro())