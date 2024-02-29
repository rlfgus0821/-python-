## 함수
from random import randint, choice
def seqsearch(ary, fdata):
    pos = -1
    for i in range(len(ary)):
        if (ary[i] == fdata):
            pos = i
            break
    return pos

## 변수
dataary = [randint(30,200) for _ in range (8)] # 데이터 자료
finddata = choice(dataary) # 찾을 데이터

## 메인
print('배열-->', dataary)
position = seqsearch(dataary, finddata)
if (position != -1):
    print(finddata,'는',position, '위치에 있어요')
else:
    print(finddata, '는', position, '없어요')

