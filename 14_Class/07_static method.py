# 정적 메소드(static method) :
# 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용하는 메소드
# @staticmethod 키워드를 지정하여 정의

class cal:
    @staticmethod
    def add(a,b):
        print(a+b)
    @staticmethod
    def sub(a,b):
        print(a-b)

mycal = cal()
mycal.add(10,20)
cal.add(10,20) # 정적 메소드 : 따로 객체를 만들어서 사용하지 않고 클래스에서 메소드 바로 호출