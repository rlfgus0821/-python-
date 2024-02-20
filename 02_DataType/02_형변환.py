
# Day2 :
# 1. 자료형(Data Type)

# 기본자료형 : 정수(int), 실수(float), 부울(bool), 문자열(str)
# interactive / 집합적 자료 / sequence : 리스트, 딕셔너리, 튜플, 세트

# 1) 진법 변환 함수
# 2진, 8진수, 16진수, 10진수
# bin(), oct(), hex()

#10진수를 2진수
print('bin(123)=', bin(123))
#8진수
print('bin(0o123)=', bin(0o123))
#16진수
print('bin(0x123)=', bin(0x123))

print('oct(123)=', oct(123))
print('oct(0o10101111)=', oct(0b10101111))
print('oct(0x123)=', oct(0x123))

print('hex(123)=', hex(123))
print('hex(0o10101111)=', hex(0b10101111))
print('hex(0o123)=', hex(0o123))

# 변수의 자료형 : 실행할 때 결정(동적타이핑)
# id(), type()

# 2) 형변환
# int(string), float(string), str(number)
# int(string, '진수 숫자') -> string은 진수 숫자이다. 10진수로 변환

# int(string, base=10)
# int(string) : 10진수 기본
# int(string, 2)

print("int('123')=", int('123'))
print("int('1010', 2)=", int('1010', 2))
print("int('ff', 16)=", int('ff', 16))
print("int('123', 8)", int('123', 8))

# 에러 : NameError(변수의 이름 에러) , TypeError(ex)문자와 숫자 더할때 타입에러) , ValueError(값을 잘못 썼을 때)
# print('int('ff')=', int('ff')) -> ValueError ff가 숫자가 아니라서 값 에러

#float(string) : 문자열을 실수형으로 변환

print('float("13.5")=', float('13.5'))
print('float("13")=', float('13'))

# str(숫자) : 숫자를 문자열로 변환
print('나이는 = %d'%'20') # -> TypeError 발생 '20'은 숫자가 아닌 문자라서
print('나이는 = %d'%int('20'))
print('나이는 ='+ 20) # -> typeError 문자와 숫자 더하기 라서
print('나이는=' + str(20))


# input() 함수 : 키보드로 값을 입력받아서 문자열로 반환
# input(prompt) : prompt는 화면에 표시되는 문자열

name = input('이름은:')
year = int(input('출생연도는'))
print(f'이름은{name}, 나이는 {2024-year}')

num = float(input('실수입력: '))
result = num * 10
print(f'{num}*10={result}')

# 연산자 : *, +
# 문자열 + 문자열 = 두 문자열을 연결
# 문자열 * 숫자 = 문자열을 숫자만큼 생성해서 연결

# 문제1. 두 정수를 입력받아서 합계 출력

num = int(input('첫번째 정수 입력:'))
num1 = int(input('두번째 정수 입력:'))
print(f'두 정수의 합은 {num+num1}')

# 문제2. 몸무게와 키 값을 입력받아 BMI 지수 계산

w = float(input('몸무게(kg):'))
h = float(input('키(m):'))
print(f'당신의 BMI는 {w/(h*h):0.2f}')

# eval() : 값에 따라 변환
