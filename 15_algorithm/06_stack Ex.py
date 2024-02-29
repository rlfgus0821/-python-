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

def checkbracket(ex):
    for ch in ex:
        if ch == '(':
            push(ch)
        elif ch == ')':
            data = pop()
            if data == '(':
                pass
            else:
                return False
    if top == -1: # 스택이 깔끔하게 비었니?
        return True
    else:
        return False
## 변수
SIZE = 50 # 전역상수, 대문자로 표현
stack = [None for _ in range(SIZE)]
top = -1

## 메인
# 괄호 갯수 오류 검사 : (())()() --> 여는 괄호push 닫는 괄호pop
expr = '((a+b)(c+d())/f(())'
retf = checkbracket(expr)

print(expr)
if retf:
    print('정상')
else:
    print('오류')
