# 메소드

s = {10,1,3,4}
print(s)

#1. 데이터 추가
# .add(값) : 값을 요소로 추가
s.add(100)
print(s)

# .update() : 값을 요소로 추가
s.update([5,6])
print(s)

#2. 데이터 삭제, 추출
# .pop() : 맨 앞에 있는 요소를 가져온다
result = s.pop()
print(result)
print(s)

# .remove(값) : 값을 요소에서 제거 / 없는 값을 입력하면 Error
s.update((10,11,12,13,14,15,16))
print(s)
s.remove(15)
print(s)

# .discard() : 값을 요소에서 제거 / 없는 값을 입력하면 넘어가고 진행
s.discard(10)
print(s)

# .clear() : 값을 모두 제거하고 빈 세트로 반환
s.clear()
print(s) # -> set()

# 합집합 : union() == |
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.union(s2))
print(s1|s2)
# 교집합 : intersection() == &
print(s1&s2)
# 차집합 : difference() == -
print(s1-s2)
