# push : 스택에 데이터를 삽입하는 작동
# pop : 스택에 데이터를 추출하는 작동
# top : 스택에 들어 있는 가장 위의 데이터

## 함수
## 변수
stack = [None,None,None,None,None]
top = -1

## 메인
# push()
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print('바닥: ', stack)
# 위 push()과 같다
for i in range(len(stack)-1,-1,-1):
    print(stack[i])

# pop()
data = stack[top]
stack[top] = None
top -= 1
print('pop1 -->', data)
print('바닥: ', stack)

data = stack[top]
stack[top] = None
top -= 1
print('pop2 -->', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop3 -->', data)
# 위 pop()과 같다
for i in range(len(stack)-1,-1,-1):
    print(stack[i])