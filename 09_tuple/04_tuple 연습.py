# 2차원 튜플 생성

t = ((1,2,3),(4,5,6),(7,8,9))
print(t)

# 2차원 튜플의 요소를 행열의 테이블 형식으로 출력
for r in t:
    for c in r:
        print(c, end=' ')
    print()
