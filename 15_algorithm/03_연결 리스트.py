# 노드 = 데이터 + 링크
# 선형리스트는 데이터만 있고 연결리스트는 노드로 데이터와 링크가 같이 있다.
# 파이썬은 노드가 없어서 노드라는 데이터형을 만드는 클래스 생성
# 단순 연결 리스트의 마지막은 링크가 없고, 원형 연결 리스트의 마지막은 링크로 헤드를 가르킨다.
## 함수
class node():
    def __init__(self):
        self.data = None
        self.link = None

## 변수


## 메인
node1 = node()
node1.data = '다현'

node2 = node()
node2.data = '정연'
node1.link = node2

node3 = node()
node3.data = '쯔위'
node2.link = node3

node4 = node()
node4.data = '사나'
node3.link = node4

node5 = node()
node5.data = '지효'
node4.link = node5

# 노드데이터 삽입
newnode = node()
newnode.data = '재남'
newnode.link = node2.link
node2.link = newnode

# 노드 데이터 삭제
newnode.link = node3.link
del (node3)

# 연결리스트는 head만 찾으면 추적해서 데이터를 알 수 있다.
head = node1
print(head.data, end=' ')
print(head.link.data, end=' ')
print(head.link.link.data, end=' ')
print(head.link.link.link.data, end=' ')
print(head.link.link.link.link.data, end=' ')
print()

current = head
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')
print()