## 함수
# 순차 큐
def isqueuefull():
    global SIZE, front, rear, queue
    # case 1: 뒤에 여유 있음
    if (rear != SIZE-1):
        return False
    # case 2: 진짜 꽉참
    elif (rear == SIZE-1 and front == -1):
        return True
    # case 3: 뒤는 마지막까지 있고 앞에 여유
    elif (rear == SIZE-1 and front != -1): # else해도 상관x
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isqueueempty():
    global SIZE, front, rear, queue
    if (front == rear):
        return True
    else:
        return
def enqueue(data):
    global SIZE, front, rear, queue
    if (isqueuefull() == True):
        print('queue is full')
        return
    rear += 1
    queue[rear] = data

def dequeue():
    global SIZE, front, rear, queue
    if (isqueueempty() == True):
        print('queue is empty')
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 다음 손님 확인할 때 peek()
def peek():
    global SIZE, front, rear, queue
    if (isqueueempty() == True):
        print('queue is empty')
        return
    return queue[front+1]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
# enqueue()
enqueue('화사')
enqueue('솔라')
enqueue('문별')
enqueue('휘인')
enqueue('선미')
print('출구<--',queue,'<--입구')

enqueue('재남')
print('출구<--',queue,'<--입구')

retdata = dequeue()
print('입장할 손님: ',retdata)
print(peek(),'손님 준비하세요.')
retdata = dequeue()
print('입장할 손님: ',retdata)
print(peek(),'손님 준비하세요.')
retdata = dequeue()
print('입장할 손님: ',retdata)
print(peek(),'손님 준비하세요.')