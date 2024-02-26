# 텍스트 파일 읽기 : read(), readline(), readlines(), seek()

# 텍스트 파일 생성 : 메모장을 이용

# 1단계: 파일열기 / 한글파일 = encoding='utf-8'
file1 = open('asd.txt','r',encoding='utf-8')
# 2단계: 파일처리
text = file1.read()
text1 = file1.readline() # 한줄씩 읽어 오기 + ('\n'포함이라서 한줄씩 띄어쓰기 적용)
text2 = file1.readline() # 그 다음줄 읽어 오기
while True:
    text = file1.readline()
    if not text:  # <-읽을 내용이 없으면(마지막)
        break
    print(text)

# readlines()으로 파일읽기
text3 = file1.readlines() # 줄마다 내용(+'\n')을 리스트로 만들기
for textline in file1.readlines():
    print(textline, end='')
# readlines() 없이 파일읽기
for line in file1:
    print(line, end='')
# 3단계: 파일닫기
# file1.close()
