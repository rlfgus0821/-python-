# with 문 : close()가 자동으로 수행
# with open(파일명, 모드) as 파일객체:
#          문장들
filename = '../data/readwrite.txt'
with open(filename, 'r',encoding='utf-8') as f:
    text = f.read()
    print(f.read())

# 위 파일의 내용을 다른 파일로 복사할 때
with open('../data/file1.txt','a',encoding='utf-8') as f1:
    f1.write(text)

with open('../data/scores.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    print(data)
