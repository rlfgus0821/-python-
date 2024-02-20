# 3Day

# 연습 문제1. 정수가 홀수인지 짝수인지
num = int(input('정수를 입력하시오'))
if num % 2 == 0:
    print('짝수입니다')
elif num % 2 == 1:
    print('홀수입니다')
else:
    print('잘못입력하셨습니다')

# 연습 문제2, 정수 3개 중 가장 큰 수를 찾아라
num1 = int(input('정수1:'))
num2 = int(input('정수2:'))
num3 = int(input('정수3:'))
if num1>num2>=num3 and num1>num3>=num2:
    print(f'제일 큰수는 {num1}입니다')
elif num2>num1>=num3 and num2>num3>=num1:
    print(f'제일 큰수는 {num2}입니다')
else:
    print(f'제일 큰수는 {num3}입니다')

# 연습 문제3. 도형을 선택해서 면적 구하기
sh = input('도형입력(1: 사각형, 2: 삼각형, 3: 원):')

if sh == '1':
    s = float(input('가로입력:'))
    h = float(input('세로입력:'))
    print(f'사각형의 면적 = {s*h}')
elif sh == '2':
    s = float(input('밑변입력:'))
    h = float(input('높이입력:'))
    print(f'삼각형의 면적 = {s*h/2}')
elif sh == '3':
    s = float(input('반지름 입력:')) 
    print("원의 면적 ="'%0.2f' %(3.141592*s**2))
else:
    print('오류')

# 연습 문제4 : 컴퓨터와 주사위 놀이하기 (이긴 사람 출럭하기)
from random import randint
a = int(input('주사위 눈의 수를 입력하시오:'))
b = randint(1,6)
print('나=', a, '컴퓨터=', b)
if a>b:
    print('승리하였습니다')
elif b>a:
    print('패배하였습니다')
else:
    print('비겼습니다')

# 반복문 (for:반복횟수가 정해짐, while:반복수를 정하지 x)
# for문 
for num in [1,2,3,4,5,6,7,8,9]:
    print(num)
# range(start,stop,step)
for x in range(0,10,2):
    print(x,end='')
# 짝수만 고를 때 
for i in range(2,10,2):
    print(i, end='')

# 1~10사이의 정수를 더하기
tot = 0
for x in range(1,11):
    tot += x
print(tot)
    
# 1부터 10사이의 홀수를 더하기
tot = 0
for x in range(1,11,2):
    tot += x
print(tot)

# 값을 시작값, 끝값을 입력받아 이 사이에 있는 정수 더하기
sn = int(input('시작값'))
fn = int(input('끝값'))
tot = 0
for x in range(sn,fn + 1):
    tot += x
print(tot)

for x in range(5,0,-1):
    t = print(x, end=' ')
print(t,'발사')

# 5명의 점수 입력 받아 합격>=60, 불합격<60 출력
for score in range(5):
    score = int(input('점수입력:'))
    if score>= 60:
        print(f'{score} 합격')
    else:
        print(f'{score} 불합격')

