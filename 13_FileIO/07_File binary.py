# binary File : 이진파일
# 글자(text)가 아닌 bit 단위로 의미가 부여되는 파일
# 텍스트 파일을 제외한 파일 : 그림, 음악, 동영상, 엑셀, 실행exe
# 텍스트파일과 이진 파일 구분 : 메모장에서 파일열기 시 내용이 보이면 텍스트, 이상하면 이진파일

# C드라이브에 있는 노트패드 실행 파일을 data파일로 복사하기
instr= ''
path1 = 'C:/Windows/notepad.exe'
path2 = '../data/notepad.exe'
inf = open(path1,'rb')
outf = open(path2,'wb')

while True:
    instr = inf.read(1)
    if not instr:
        break
    outf.write(instr)
inf.close()
outf.close()
