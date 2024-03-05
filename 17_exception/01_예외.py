# ZeroDivisionError: 0으로 숫자를 나눌 때
10/0

# TypeError: 타입이 알맞지 않게 사용 되었을 때
print('나이는' +23 + '살')

# NameError: 존재하지 않은 변수를 호출할 때
print(b)

# ValueError: 변환할 수 없는 문자/숫자를 변환할 때
c =100
print('%d%'%c)

# SyntaxError: 문법적인 오류
if x > 10
        print('hello')

# IndexError: 리스트의 인덱스 범위를 넘어 갈 때
a=[1,2,3,4]
print(a[5])

# UnboundLocalError: 변수의 스코프가 적절하지 않을떄 ex) 전역변수를 함수내에서 global없이 사용할 때
def add():
    a = a+1
add()

# ModuleNotFoundError: 모듈을 찾을 수 없는 에러
import mymodule

# FileNotFoundError: 파일을 찾을 수 없는 에러
with open('except.txt','r') as f:
    f.read()

# OSError
with open('c:\file\except.txt','r') as f:
    f.read()