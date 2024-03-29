# set의 특징

#1. 순서가 없다 : 입력되는 순서와 출력되는 순서는 다를 수 있다.
#2. 동일한 요소는 중복될 수 없다.
#3. 요소 추가/삭제 가능
#4. 인덱스 사용 불가
#5. 변경가능한 항목을 세트의 요소로 가질 수 없다. /리스트 x / 튜플 o

# 키만 모아놓은 딕셔너리의 특수한 형태
# 세트생성: {}, set()

s1 = {1,2,3,4,5,6,1,2,3}
print(s1, type(s1))

s2 = set([10,8,11,20,30,10])
print(s2, type(s2))

s3 = set((10,20,30))
print(s3)

s4 = set({'one':1, 'two':2})
print(s4)

# 리스트는 세트의 요소가 될 수 없다.
s5 = {1,2,[4,3]} # Error

# hashable type => hashing
# 객체를 식별할 수 있는 코드를 부여하여 테이블에 저장하는 방식: (키, 값)
