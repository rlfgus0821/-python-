# 선형리스트의 간단구현
## 함수 선언부
## 전역 변수부
ktalk = ['다현','정연','쯔위','사나','지효']

## 메인 코드부
print(ktalk)

#! 데이터 추가(모모에게 카톡 1회)
# 1단계 : 빈 칸 추가
ktalk.append(None)
# 2단계 : 데이터 넣기
ktalk[5] = '모모'
print(ktalk)

#! 데이터 삽입(미나에게 연속 카톡 40회 -> 미나를 3등)
# 1단계 : 빈 칸 추가
ktalk.append(None)
# 2단계 : 한칸씩 뒤로 이동
ktalk[6] = ktalk[5] # 모모 이동
ktalk[5] = None
ktalk[5] = ktalk[4] # 지효 이동
ktalk[4] = None
ktalk[4] = ktalk[3] # 사나 이동
ktalk[3] = None
# 3단계 : 새친구 넣기
ktalk[3] = '미나'
print(ktalk)

#! 데이터 삭제(사나 삭제)
# 1단계 : 데이터 지우기
ktalk[4] = None
# 2단계 : 한칸씩 앞으로 5등부터 마지막까지
ktalk[4] = ktalk[5] # 지효 5등으로 이동
ktalk[5] = None
ktalk[5] = ktalk[6] # 모모 6등으로 이동
ktalk[6] = None
# 3단계 : 마지막 칸 제거
del(ktalk[6])
print(ktalk)
