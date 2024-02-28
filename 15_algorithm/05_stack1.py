## 함수
def isstackfull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return

def push(data):
    global SIZE, stack, top
    if isstackfull() == True:
        print('stack is full')
        return
    top += 1
    stack[top] = data

def isstackempty():
    global SIZE, stack, top
    if top <= -1:
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if isstackempty() == True:
        print('stack is empty')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# peek() 다음에 나올것을 확인해보기
def peek():
    global SIZE, stack, top
    if isstackempty() == True:
        print('stack is empty')
        return
    return stack[top]

## 변수
SIZE = 5 # 전역상수, 대문자로 표현
stack = [None for _ in range(SIZE)]
top = -1

## 메인

push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
print('바닥: ', stack)

push('게토레이')
print('바닥: ', stack)

# pop()
redata = pop()
print('pop1 --->', redata)

redata = pop()
print('pop2 --->', redata)

redata = pop()
print('pop3 --->', redata)

# peek() 다음에 나올것을 확인해보기
print('다음 예정 --->', peek())

redata = pop()
print('pop4 --->', redata)
print(stack)