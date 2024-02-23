#1. 함수의 매개변수
# 매개변수 : 함수를 정의할 때 함수로 전달되는 값을 갖는 변수
# 인수 : 함수를 호출할 때 전달되는 값을 갖는 변수
# witdth, height = 매개변수
# 10.20 = 인수
def get_area(width, height):
    result = width*height
    print(f'면적은 {result}')
    return result
get_area(10,20)

#문제. 사칙연산을 수행하는 함수 정의 add(), sub(), mul(), div()
# add()
def add(a, b):
    result = a + b
    print(a+ b)
    return result
# sub()
def sub(a, b):
    result = a - b
    print(a - b)
    return result
# mul()
def mul(a, b):
    result = a * b
    print(a * b)
    return result
# div()
def div(a, b):
    if b == 0:
        print('0으로 나눌 수 없다')
    else:
        result = a / b
        print(f'{a/b:.1f}')
        return result

add(9,3)
sub(9,3)
mul(9,3)
div(9,0)

#2. 디폴트 매개변수 : 매개변수의 기본값이 지정되어 있는 경우
# 디폴트 매개변수는 마지막에 있어야 한다.
def greet(name, msg='안녕!'):
    print(name + ', ' + msg)
greet('홍길동')
greet('홍길동', 'hi')

#3. 위치 매개변수 : 매개변수의 위치가 실인수로 전달받을 때 동일한 위치의 변수에 저장
def get_area(width, height):
    result = width*height
    print(f'면적은 {result}')
    return result
get_area(10,20)

#4. 함수에 여러개의 자료 전달
def show_name(name):
    a = list()
    for n in name:
        print(n, end=' ')
    return a.append(n)
show_name(['김','정','박','최'])
print()
def show_info(info):
    print(info)
    for n in info.keys():
        print(info[n],end=', ')
show_info({'이름':'김', '나이':'20'})
print()
#5. 가변길이 매개변수 : 매개변수의 길이가 정해지지 않는 경우, 여러개의 값을 전달 받을 때 사용
# *args(위치인수) or **kwargs(키워드인수) => key = value
print('hi','ho',end= '\n')
# * args : 매개변수의 수를 정하지 않고 사용할 때
def my_sum(*args):
    tot = 0
    for i in args:
        tot += i
    print(tot)
    return tot
my_sum(1,3,4,5,6)

# **kwargs : (변수 = 값) 형태로
def show_info(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])
    for value in kwargs.values():
        print(value)
    for item in kwargs.items():
        print(item)
show_info(id='abc', name='kim', age='30')

#6. 키워드 인수 : 인수들 앞에 매개변수를 키워드로 두어 사용
def my_add(a,b,c):
    return a+b+c
print(my_add(10,32,42))
print(my_add(a=1,c=2,b=3)) # 키워드 인수 : a=, b=, c=

# *args는 **kwargs 앞에 있어야한다.
def fun(a,b, *args, **kwargs):
    pass
def fun1(**kwargs, *args): # 불가능 **kwargs는 뒤로 가야한다
    pass
# 함수호출
# 위치인수와 키워드 인수를 같이 사용하는 경우 : 위치 인수 -> *args -> **kwargs
# 함수정의 : 위치매개변수 뒤에 디폴트매개변수는 뒤에