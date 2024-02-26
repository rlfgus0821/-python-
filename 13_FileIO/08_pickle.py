# 파이썬 객체를 파일에 저장(dump), 읽기(load)

# import pickle # 밑에 문장이랑 같은데 메모리를 더 차지한다 (위에가)
from pickle import dump, load
datalist = [['구','전체','내국인','외국인'],
            ['관악구',519864,502089,17775],
            ['강남구',54762,542498,5014],
            ['송파구',686181,679247,6934],
            ['강동구',428547,424222,4312]]

# datalist를 파일에 저장
with open('../data/datalist.pickle','wb') as f:
    dump(datalist, f)
# 저장한 파일 읽기
with open('../data/datalist.pickle','rb') as f:
    datapickle = load(f)
    for item in datapickle:
        print(item)
# 저장한 파일에 append해서 datapickle 리스트에 저장
datapickle.append(['종로구',326173,44231,4423])
print(datapickle)
# 다시 파일에 저장
with open('../data/datalist.pickle','wb') as f:
    dump(datapickle, f)