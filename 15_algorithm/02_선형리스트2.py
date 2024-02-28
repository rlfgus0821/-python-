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