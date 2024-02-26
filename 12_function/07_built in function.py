# 내장함수
# abs() : 절대값
print(abs(-10))

# all(iter) : 모두 True인 경우 True
# any(iter) : 하나라도 True인 경우 True
print(all([0,1,2,3]))
print(any([1,0,[]]))

# chr(), ord() : 아스키 코드 값
print(chr(65))
print(ord('A'))

# divmod(), pow()
#min(), max(), sum()
print(max([1,2,3,4,-10])) # 최댓값
print(min([1,2,3,4,-10])) # 최솟값
print(sum([1,2,3,4,-10])) # 더하기
print(divmod(10,3))       # 10 / 3 -> (나머지, 몫) 반환
print(pow(10,3))          # 10의 3제곱

# round(num, ndigit) : 반올림
print(round(3.141592168945, 4))
print(round(3.141592))

# enumerate() : 인덱스 값을 포함한 enumerate 객체를 반환
print(list(enumerate(['kim','lee','choi'])))
# -> [(0,'kim'), (1,'lee'), (2,'choi')]
for index, value in enumerate(['kim','lee','choi']):
    print(index)
    print(['kim','lee','choi'][index])

for idx, value in enumerate('hello world!'):
    print(idx, value)

# eval(표현식) : 표현식을 그대로 실행
print(eval('10')) #-> int 10
print(eval('10*10')) #-> int 100
print(eval('10'+'10')) #-> int 1010

# filter() : 반복가능한 자료에 함수를 적용하여 True인 결과만 추출
def positive(x):
    return x>0
def even(x):
    if x % 2 == 0:
        return x

print(positive(10))
print(positive(-10))

print(list(map(positive, [1,2,-1,-10])))
print(list(filter(positive, [1,2,-1,-10])))
print(list(filter(even, [1,2,-1,-10])))

# help() : 도움말 시스템을 호출
help(print)

# int(), float(), str()
# bin(), hex(), oct()
# input(), print()
# zop(), map()
# range()
# len()
# list(), tuple(), dict(), set()
# id(), type()
# lambda