# 튜플 생성

t1 = (1,2,3)
print(t1, type(t1))

t2 = 4,5,6
print(t2, type(t2))

t3 = t1, (7,8,9)
print(t3, type(t3), len(t3))

t4 = [1,2], [3,4,5]
print(t4, type(t4))

t5 = tuple((1,2,3))
print(t5)

t6 = tuple('hello')
print(t6)
#리스트를 튜플로 변환
list1 = [1,2,3]
t7 = tuple(list1)
print(t7, list1)

#튜플을 리스트로 변환
list2 = list(t4)
print(list2)