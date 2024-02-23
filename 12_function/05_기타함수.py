# 재귀함수 : 함수 내부에서 자신의 함수를 다시 호출

# 1~n까지의 합
def sum(n):
    if n == 1: return 1
    return n + sum(n-1)
print(sum(10))

# 1~n까지 곱하기
def mul(n):
    if n <= 1:
        return 1
    return n * mul(n-1)
print(mul(5))

# 내부함수

def func(x,y):
    def afunc(a,b):
        return a+b
    return afunc(x,y)
print(func(10,30))

# 람다함수: 한줄짜리 함수 / return문을 사용x
# lambda <인수들>:<반환할 식>
# 람다함수는 함수 주소를 반환
# 변수로 람다함수 객체를 받아서 함수호출
f = lambda:1
print(f())

add = lambda x,y:x+y
print(add(1,9))

add1 = lambda x,y=30:x+y
print(add1(10))

add2 = lambda x,y:x+y
print(add2(y=1,x=9))

# 람다 표현식 : 함수 이름을 변수에 할당하지 않고 바로 호출
# (lambda 매개변수 : 식)(인수)

print((lambda x,y: x+y)(10,30))
# 람다표현식 안에서는 변수 생성 불가
# (lambda x: y=10; x+y)(10)
(lambda x,y=10: x+y)(10,30)

def ten(x):
    return x+10
# = 같다
(lambda x:x+10)
# [1,2,3,4,5]+10
nlist=list()
for n in [1,2,3,4,5]:
    nlist.append(n+10)
# map(함수이름, 인수들) : 함수를 인수들 하나하나 적용하여 값 반환
print(list(map(lambda x:x+10,[1,2,3,4,5])))

#문제. 두 리스트의 동일한 인덱스에 있는 값을 합하여 새로운 리스트 생성
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
def addlist(x,y):
    list3 = []
    for i in range(len(x)):
        list3.append(x[i] + y[i])
    return list3
print(addlist(list1,list2))
# lambda 함수 이용
print(list(map(lambda n1, n2:n1+n2, list1, list2)))