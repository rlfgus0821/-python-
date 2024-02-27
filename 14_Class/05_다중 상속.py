# 다중상속 : 여러 클래스에서 상속받기
class person:
    def __init__(self,name='', age=0):
        self.name = name
        self.age = age
    def greeting(self):
        print('안녕하세요.')
class student(person):
    def __init__(self,name='',age=0,stid=''):
        super().__init__(name,age)
        self.stid = stid
    def study(self):
        print('공부하기')
class unistudent:
    def __init__(self,department='',grade=''):
        self.department = department
        self.grade = grade
    def managescore(self):
        print(f'{self.department}에서 공부하기')
# 다중 상속
class undergra(student, unistudent):
    pass


lee = person('lee', 20)
kim = student('kim', 17)
lee.greeting()
kim.greeting()
kim.study()
choi = undergra()
choi.study()