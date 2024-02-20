'''
# 연산자

# 1. 산술연산자 : +, -, *, /, //, %, **

# divmod(x,y) : x를 y로 나눈 몫과 나머지 반환

# 문제1. 10000초는 몇시간 몇분 몇초인가?

time = 10000
m1 = time // 60
h = m1 // 60
m = m1 % 60
s = time % 60
print(f'{time}초는 {h}시간 {m}분 {s}초 입니다.')

# 연산자 우선순위 : 산술 > 비트 > 관계 > 논리


# 2. 관계연산자 : > , < , <= , >= , == , !=

a = 100
b = 5
result = a == b
print(f'{a}=={b}의 결과는 {result}') # -> False

# 3. 논리연산자 : and , or , not

a = 100
b = 5
print(a > 200 and a < 300) # -> False
print(a > 200 or a < 300) # -> True
print(not(a > 200)) # -> True

# 4. 비트 연산자(데이터분석에 많이 쓰이지는 않지만 개념을 알면 좋음) : & | ^ ~ <<  >>

a = 100
print(f'~{a}:{~a}')
print(f'{b}<<1:{b<<1}')

# 대입연산자 : += -= *= /= //= %=
print('a=',a)
a+=10
print('a+=10:', a)
'''
# 실습문제 : 지폐교환기

tot=int(input('지폐로 교환할 돈은 얼마?: '))
print(f'5만원짜리 {tot//50000}장')
tot%=50000
print(f'만원짜리  {tot//10000}장')
tot%=10000
print(f'5천원짜리 {tot//5000}장')
tot%=5000
print(f'천원짜리  {tot//1000}장')
tot%=1000
print(f'바꾸지 못한 돈 = {tot}원')

tot = int(input('금액:'))
m5,rem = divmod(tot,50000)
m,rem = divmod(rem,10000)
t5,rem = divmod(rem,5000)
t,rem = divmod(rem,1000)
print(f'{tot}는 5만원짜리 {m5}장, 만원짜리{m}장, 5천원짜리{t5}장, 천원짜리{t}장, 바꾸지못한 돈은{rem}')
