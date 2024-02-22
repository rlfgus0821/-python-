# 뷰(view)
# keys(), values(), items()
# keys() view
d = {'one':1,'two':2,'three':3}
print(d.keys(), d.values(), d.items())
print(list(d.keys()))

# key들에 대한 value들을 출력
for key in d.keys():
    print(key, d[key])

# values() view
print(d.values())
for value in d.values():
    print(value, tuple(d.values()))
print(len(d.values()))

# items() view
print(d.items())
for item in d.items():
    print(item, list(d.items()))

for key, value in d.items():
    print(key, value)

# 문제1. 다음과 같은 자료를 갖는 딕셔너리를 생성하시오.
d = {'학번':1000, '이름':'홍길동', '학과':'컴퓨터학과'}
# 문제2. 생성한 딕셔너리에 연락처:010-1111-1111 추가하시오
d['연락처'] = '010-1111-1111'
# 문제3. '학과'의 값을 '파이썬학과'로 수정하시오
d['학과'] = '파이썬학과'
# 문제4. '학과' 키값을 삭제하시오
del(d['학과'])
print(d)