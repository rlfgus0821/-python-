#1. '비트코인' 문자열을 화면에 출력하는 print_coin()함수 정의
def print_coin():
    print('비트코인')
#2. 1에서 정의한 함수 호출
def print_coin():
    print('비트코인')
print_coin()
#3. 1에서 정의한 함수 100번 호출
def print_coin():
    print('비트코인')
for i in range(100):
    print_coin()
#4. '비트코인' 문자열을 100번 화면에 출력하는 print_coin()함수 정의
def print_coin():
    for i in range(100):
        print('비트코인')
print_coin()

#5. 두 수를 인자로 입력받아 곱한 후 그 결과를 반환하는 mul()함수 정의
def mul(x,y):
    return x*y
#6. 소문자 문자열을 인자로 받아 대문자로 변환하여 반환하는 toUpper() 함수 정의
def toUpper(x):
    return x.upper()
#7. 리스트를 인자로 받아 짝수만 모아 반환하는 pickup_even()함수 정의
def pickup_even(*args):
    list= []
    for i in args:
        if i % 2 == 0:
            list.append(i)
    return list
list2 = [1,2,3,4,5,6,7,88]
print(list(filter(pickup_even, list2)))