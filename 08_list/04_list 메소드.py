# list 메소드(함수)

#1. appemd() : 리스트 맨 뒤에 항목을 추가

a = []
a.append('apple')
a.append('hotdog')
a.append('banana')
a.append('melon')
print(f'alist = {a}')

#2. pop([idex]) : 리스트 index를 사용하지 않으면 맨 마지막 요소를 추출, 제거
value = a.pop()
print(f'alist : pop 적용 {a}', f'value={value}')
a.pop(0)
print(f'alist : a.pop(0) {a.pop(0)}', f'pop적용 후{a}')

#3. sort() : 리스트의 요소들을 정렬하여 정렬된 리스트로 변경
b = [6,3,5,1,-3]
print(f'blist : {b}')
b.sort()
print(f'sort적용 후 : {b}')

#4. reverse() : 리스트를 역순으로 변경
b.reverse()
print(f'reverse적용 후 : {b}')
print(f'reverse적용 후 : {a}')

#5. index() : 리스트에서 지정한 값의 위치를 반환, 값이 없는 경우 에러 발생
c = ['김','장','최','박','정']
idx = c.index('장')
print(idx)

