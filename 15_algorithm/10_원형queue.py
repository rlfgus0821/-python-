## 함수
# 원형 큐 : 데이터가 많을 때 사용, 오버헤드x
def isqueuefull():
    global SIZE, front, rear, queue
    if ((rear+1)%SIZE == front):
        return True
    else:
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
    rear = (rear + 1)%SIZE
    queue[rear] = data

def dequeue():
    global SIZE, front, rear, queue
    if (isqueueempty() == True):
        print('queue is empty')
    front = (front +1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

# 다음 손님 확인할 때 peek()
def peek():
    global SIZE, front, rear, queue
    if (isqueueempty() == True):
        print('queue is empty')
        return
    return queue[(front+1)%SIZE]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인
# enqueue()
enqueue('화사')
enqueue('솔라')
enqueue('문별')
enqueue('휘인')
retdata = dequeue()
print('입장할 손님: ',retdata)
print(peek(),'손님 준비하세요.')
retdata = dequeue()
print('입장할 손님: ',retdata)
print(peek(),'손님 준비하세요.')
enqueue('선미')
print('출구<--',queue,'<--입구')

enqueue('재남')
print('출구<--',queue,'<--입구')

retdata = dequeue()
print('입장할 손님: ',retdata)
print(peek(),'손님 준비하세요.')