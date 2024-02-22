# 튜플 조작

#1. 인덱싱
t = 1,2,3,4,5,6,7,8
print(t[0])

#2. 슬라이싱
print(t[:])
print(t[3:])
print(t[::-1])

#3. +연산
t1 = (4,5,6)
t2 = 10,11,12
t3 = t1+ t2
print(t1,t2,t3)

#4. *연산
print(t1*3)

#5. 멤버연산 : in, not in
t5 = 'hello', 'hi', 'hohoho'
print('hi' in t5)

#6. len()
print(len(t5))

#7. del(): 튜플 자체를 제거하는 것은 가능 / 튜플 요소를 제거하는 것은 불가능
del(t5)

#8. 튜플 요소 검색 : index(), count()
t6 = tuple('hello hi how are you')
print(t6)
print(t6.index('o'))
print(t6.count('h'))