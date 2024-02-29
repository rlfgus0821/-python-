## 함수
from random import randint
def findinindex(ary):
    minidx = 0
    for i in range(1,len(ary)):
        if ary[minidx] > ary[i]:
            minidx = i
    return minidx

## 변수
before = [randint(30,200) for _ in range (8)]
after = []

## 메인
print('정렬 전-->', before)
for _ in range(len(before)):
    minpos = findinindex(before)
    after.append(before[minpos])
    del (before[minpos])
print('정렬 후-->', after)
