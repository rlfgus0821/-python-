# 클래스 메소드(class method) :
# 인스턴스를 통하지 않고 클래스에서 바로 호출
# @classmethod 사용

class person:
    count = 0 # 클래스 변수
    def __init__(self):
        person.count += 1
    @classmethod
    def printcnt(cls): # cls: 클래스
        print(f'{cls.count}명 태어났어요')
    @classmethod
    def create(cls):  # 생성자와 같은 메소드
        p = cls() # = person()
        return p

kim = person()
person.printcnt()
choi = person()
person.printcnt()

lee = person.create() # 클래스 메소드로 인스턴스 생성
person.printcnt()
