#1. .get() : 지정한 키의 값을 반환(지정한 키가 없으면 n반환) / .get(4:n)

d = {'one':1, 'two':2, 'three':3}
print(f"f.get('two')= {d.get('two')}")
print(f"f.get('four',4)= {d.get('four',4)}")
print(d.get('four'))
print(d)

#2. .setdefault() : .get()과 동일하나 값이 존재하지 않을 때 값을 추가
d.setdefault('four', 4)
d.setdefault('two')
print(d)

#3. .pop(): key값을 지정, .popitem(): 맨 마지막 key
# .popitem()
key, value = d.popitem()
print(f'd= {d},key= {key}, value= {value}')

d['six'] = 6
d['ten'] = 10
print(d)

# .pop(key)
result = d.pop('two')
print(result)
print(d)

#4. .copy()
d2 = d.copy()
print(d, id(d))
print(d2, id(d2))

#5. .update(): 딕셔너리를 합치기 (같은 부분 중복x)
d2['four'] = 4
d2['five'] = 5
d.update(d2)
print(d)

#6. .clear() : 딕셔너리 요소들을 모두 제거
d.clear() # d.clear()는 메모리가 같으면서 요소들을 제거 /
          # d={} 새로운 딕셔너리로 메모리가 달라진다.
print(d)
