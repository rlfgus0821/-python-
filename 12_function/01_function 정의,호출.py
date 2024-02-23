# 함수
# 재사용 : 자주 사용하는 기능들을 위한 코드 집합
# 내장함수(built in function) / 사용자가 정의한 함수
# 함수 정의 및 호출

#예. 이름, 나이, 연락처 출력하는 함수 : show.info()
def show_info():
    print('이름 : 홍길동')
    print('나이 : 20')
    print('연락처 : 010-1111-1111')
show_info()
def show_info1():
    name = input('이름 입력: ')
    age = input('나이 입력: ')
    pnum = input('연락처 입력: ')
    print(f'이름 : {name}')
    print(f'나이 : {age}')
    print(f'연락처 : {pnum}')
show_info1()

#문제. 두 정수를 입력받아 더하는 함수 add() 정의하기
def add():
    num1 = int(input('정수1 입력: '))
    num2 = int(input('정수2 입력: '))
    result = num1+num2
    print(f'정수1 + 정수2 = {result}')
    return result
result = add()
print(result)
