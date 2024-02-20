#1. 인덱싱 : 요소 접근

a = [1,2,3,4,5]
b = [[1,2],[3,4],[5,6]]
print(a[0], a[-1], a[-3])
print(b[0],b[2], b[0][0]) #b[0][0] = b리스트 중 0번째 리스트 안에 0번째 문자

#2. 슬라이싱 : 부분문자열
print('a[:] = ', a[:])
print('a[1:] = ', a[1:])
print('a[:2] = ', a[:2])
print('a[::2] = ', a[::2])
print('a[::-1] = ', a[::-1])

#3. 리스트 값 변경
a = [1,2,3,4,5]
print('변경전', a)
a[1] = 200
print('변경후', a)
a[1:2] = [[200,201]]
print('변경후1', a)

#4. 리스트 합치기 : +
a = [1,2,3,4,5]
b = [[1,2],[3,4],[5,6]]
print(a+b)

#5. 리스트 곱하기
print(a*3)

#6. 리스트 복사
# 리스트는 복사되지않고 주소값만 복사
# shallow copy(얕은 복사)
a_list = [1,2,3,4,5]
b_list = a_list # shallow copy(얕은 복사)
print('a_list:', a_list, 'b_list:', b_list)
a_list[0] = 'apple'
print('a_list:', a_list, 'b_list:', b_list)
b_list[-1] = 'banana' # list가 아니면 a_list는 안바뀌는데 list는 b를 바꿔도 a가 바뀐다
print('a_list:', a_list, 'b_list:', b_list)
print(id(a_list), id(b_list))

# deep copy (깊은 복사)
c_list = list(a_list) # deep copy (깊은 복사) # c_list = a_list 대신
print('a_list:', a_list, 'c_list:', c_list)
a_list[0] = 'apple'
print('a_list:', a_list, 'c_list:', c_list)
c_list[-1] = 'banana' # list가 아니면 a_list는 안바뀌는데 list는 b를 바꿔도 a가 바뀐다
print('a_list:', a_list, 'c_list:', c_list)
print(id(a_list), id(c_list))