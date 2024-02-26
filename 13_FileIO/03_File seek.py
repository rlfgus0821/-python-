# seek(offset, whence) : 내가 탐색하고자 하는 위치를 지정
# enter(줄바꿈) = \r, \n이 있어서 2바이트(offset)
f = open('../data/seek prac.txt', 'r', encoding='utf-8')
f.seek(0,0) # 시작위치(0,0)
lines = f.read()
print(lines)
f.close()

f.seek(1,0)
f.seek(7,0) # utf-8(한글)은 3바이트(offset)
lines = f.read()
print(lines)
