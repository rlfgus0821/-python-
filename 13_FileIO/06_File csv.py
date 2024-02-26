# csv(comma separated value) 파일읽기
# csv모듈 import

import csv

path = '../data/scores.csv'
with open(path,'r',encoding='utf-8') as f:
    data = csv.reader(f)
    for x in data:
        print(x)

# obj = csv.writer(csvfile)
# obj.writerows(데이터) : 데이터는 csv파일에 쓸 객체
datalist = [['구','전체','내국인','외국인'],
            ['관악구',519864,502089,17775],
            ['강남구',54762,542498,5014],
            ['송파구',686181,679247,6934],
            ['강동구',428547,424222,4312]]
with open('../data/pop.csv','w', encoding='utf-8', newline='') as f:
    obj = csv.writer(f, delimiter=',')
    obj.writerows(datalist)
def writecsv(filename, datalist, encoding):
    with open(filename, 'w', encoding=encoding, newline='') as f:
        obj = csv.writer(f, delimiter=',')
        obj.writerows(datalist)

writecsv('../data/pop.csv',datalist,'utf-8')
