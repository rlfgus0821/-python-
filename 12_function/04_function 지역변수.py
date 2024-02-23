# # 지역변수와 전역변수
# # 지역변수 : 함수 내부에서 정의된 변수, 함수 내에서만 사용가능
# #          함수 호출 시 생성되고, 함수종료되면 소멸
#
# a = 10 # a는 전역변수 / a에 다른 값을 지정하지 않는 한 모듈안에서 사용가능
#
# def info(name):
#     age = 10 # age 지역변수 / 함수 밖에서 사용x
#     print(name, age)
#
# print(a) # a는 전역변수
# print(age) # age 지역변수
#
# def show():
#     global a #지역변수 a를 전역변수로 사용
#     a += 1
#     print(a)
# show()

def sub(x,y):
    global b # 함수내에 global 변수는 전역변수로 변환
    a = 1
    b = 3
    x, y= y, x
    print(a,b,x,y)
a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)

def showlist(mylist):
    cplist = mylist.copy()
    cplist[-1] = 100
    print(cplist, id(cplist))

mylist = [1,2,3,4]
showlist(mylist)
print(mylist, id(mylist))