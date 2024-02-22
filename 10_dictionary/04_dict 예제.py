# in 연산자
# 딕셔너리에서는 키가 있는지 확인

d = {'nine':9, 'ten':10}
print('two' in d)
print('two' not in d)
if 'two' not in d:
    d.setdefault('two',2)
print(d)

#예제.
book = {}
book['저자'] = '홍길동'
book['책 제목'] = '파이썬'
book['출판일'] = '2020-01-30'
book['가격'] = 25000
print(book)

#문제. book 딕셔너리의 키와 값을 모두 출력하시오
for key, value in book.items():
    print(f'{key} : {value}')
