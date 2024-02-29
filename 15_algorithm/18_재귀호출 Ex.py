## 함수
def addnum(num):
    if num ==1:
        return 1
    return num+addnum(num-1)

## 메인
print(addnum(100))

# 팩토리얼 구하기(10부터 1까지 곱하기)
## 함수
def factorial(num):
    if num <=1:
        return 1
    return num*factorial(num-1)
## 메인
print('\n10!=', factorial(10))

# 우주선 발사 카운트 다운
## 함수
def countdown(n):
    if n == 0:
        print('발사')
    else:
        print(n)
        countdown(n-1)
## 메인
countdown(5)

# 입력한 숫자만큼 차례대로 하트 모양을 출력하는 코드
## 함수
def printstar(n):
    if n>0:
        printstar(n-1)
        print('\u2665'*n)
## 메인
printstar(5)

# 구구단 출력하기
## 함수
def gugu(dan, num):
    print('%d*%d = %d'%(dan,num,dan*num))
    if num < 9:
        gugu(dan, num+1)
## 메인
for dan in range(2,10):
    print('  %d단'%dan)
    gugu(dan,1)

# 배열의 합 계산하기
# 랜덤하게 생성한 배열의 합계를 구하는 코드
## 함수
import random
def arysum(ary,n):
    if n <=0:
        return ary[0]
    return arysum(ary,n-1) + ary[n]
## 메인
ary = [random.randint(0,255)for _ in range(random.randint(10,20))]
print(ary)
print('배열 합계-->', arysum(ary,len(ary)-1))