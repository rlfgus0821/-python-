## 함수
from random import randint, choice
def binsearch(ary, fdata):
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end):
        mid = (start + end) // 2
        if ary[mid] == fdata:
            pos = mid
            break
        elif ary[mid] < fdata:
            start = mid +1
        else:
            end = mid - 1
    return pos

## 변수
dataary = [randint(30,200) for _ in range (10)] # 데이터 자료
finddata = choice(dataary) # 찾을 데이터
dataary.sort()

## 메인
print('배열-->', dataary)
position = binsearch(dataary, finddata)
if (position != -1):
    print(finddata,'는',position, '위치에 있어요')
else:
    print(finddata, '는', position, '없어요')