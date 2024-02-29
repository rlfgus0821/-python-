## 함수
from random import randint
def selectsort(ary):
    n = len(ary)
    for i in range(n-1):  # 사이클(3회)
        minidx = i
        for k in range(i+1,n):
            if ary[minidx] > ary[k]:
                minidx = k
        ary[i], ary[minidx] = ary[minidx], ary[i]
    return ary

## 변수
dataary = [randint(30,200) for _ in range (20)]


## 메인
print('정렬 전-->', dataary)
dataary = selectsort(dataary)
print('정렬 후-->', dataary)
