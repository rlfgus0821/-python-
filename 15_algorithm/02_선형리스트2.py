# 선형리스트의 일반구현
## 함수
def add_data(friend):
    # 1단계 : 빈칸추가
    ktalk.append(None)
    klen = len(ktalk)
    # 2단계 : 추가한 빈칸에 친구 넣기
    ktalk[klen-1] = friend

def insert_data(position,freind):
    # 1단계 : 빈칸추가
    ktalk.append(None)
    klen = len(ktalk)
    # 2단계 : 한칸씩 뒤로 이동(마지막친구~바로 다음)
    for i in range(klen-1,position, -1):
        ktalk[i] = ktalk[i-1]
        ktalk[i-1] = None
    # 3단계 : 포지션 자리에 친구 넣기
    ktalk[position] = freind

def delete_data(position):
    # 1단계 : 위치 친구 지우기
    ktalk[position] = None
    klen = len(ktalk)
    # 2단계 : 지운 친구 다음부터 마지막 친구까지 앞으로 이동
    for i in range(position+1, klen):
        ktalk[i-1] = ktalk[i]
        ktalk[i] = None
    # 3단계 : 마지막 칸 제거
    del(ktalk[klen-1])
## 변수
ktalk = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(ktalk)
add_data('모모')
print(ktalk)

insert_data(3,'미나')
print(ktalk)

delete_data(4) # 사나(4등) 삭제
print(ktalk)

## 메인코드(실무 코드)
## 함수
def add_data(friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 추가한 빈칸에 친구 넣기
    katok[kLen-1] = friend

def insert_data(position, friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 한칸씩 뒤로 이동(마지막 친구~바로 다음)
    for i in range(kLen-1, position, -1) : # 어려움!
        katok[i] = katok[i-1]
        katok[i-1] = None # 생략은 가능~
    # 3단계 : 포지션 자리에 친구 넣기
    katok[position] = friend

def delete_data(position) :
    # 1단계 : 위치 친구 지우기
    katok[position] = None
    kLen = len(katok)
    # 2단계 : 지운 친구 다음부터, 마지막 친구까지 앞으로 이동
    for i in range(position+1, kLen,  1 ) : # 어려움
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계 : 마지막 칸 제거
    del(katok[kLen-1])

## 실무에서 쓰는 코드 예시 ##
## 전역 변수 선언 부분 ##
katok = []
select = -1	# 1: 추가, 2: 삽입, 3: 삭제, 4: 종료

## 메인 코드 부분 ##
while select != 4:
    select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))
    if select == 1:
        data = input("추가할 데이터--> ")
        add_data(data)
        print(katok)
    elif select == 2:
        pos = int(input("삽입할 위치--> "))
        data = input("추가할 데이터--> ")
        insert_data(pos, data)
        print(katok)
    elif select == 3:
        pos = int(input("삭제할 위치--> "))
        delete_data(pos)
        print(katok)
    elif select == 4:
        print(katok)
        exit
    else:
        print("1~4 중 하나를 입력하세요.")
        continue