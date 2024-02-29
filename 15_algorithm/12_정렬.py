## 함수
from random import randint
def findinindex(ary):
    minidx = 0
    for i in range(1,len(ary)):
        if ary[minidx] > ary[i]:
            minidx = i
    return minidx

## 변수
testary = [randint(0,200) for _ in range (20)]

## 메인
minpos = findinindex(testary)
print('제일 작은값:', testary[minpos])