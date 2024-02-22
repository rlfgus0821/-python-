# continue문
x = 0

while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x, end= ', ')
print('\n')
# break문
x = 0

while x < 10:
    x += 1
    if x % 2 == 0:
        break
    print(x, end= ', ')

# 연습문제 1. 숫자 10개를 입력 받아서 양, 음, 0의 갯수 출력
plus = 0
minus = 0
zero = 0

for x in range(10):
    num = int(input(f'숫자{x+1}입력:'))
    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    else:
        zero += 1
print('----------------------')
print(f'양의 갯수: {plus}')
print(f'음의 갯수: {minus}')
print(f'0의 갯수: {zero}')


plus = 0
minus = 0
zero = 0
x = 0
while x <=10:
    num = int(input(f'숫자{x+1}입력:'))
    x += 1
    if num > 0:
        plus += 1
    elif num < 0:
        minus += 1
    else:
        zero += 1
print('----------------------')
print(f'양의 갯수: {plus}')
print(f'음의 갯수: {minus}')
print(f'0의 갯수: {zero}')
