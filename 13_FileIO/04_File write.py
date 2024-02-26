#1. 문자열을 파일에 쓰기

s = '''01234
abcde f
가나다라마바
'''

f = open('../data/write prac.txt', 'w', encoding='utf-8')
f.write(s)
f.close()

#2. 키보드로 입력받은 문자열들을 파일에 쓰기
s = input('문자열 입력: ')
f = open('../data/write prac2.txt', 'w', encoding= 'utf-8')
f.write(s)
f.close()

#3. 기존의 파일 뒤에 쓰기 : 'a'모드 사용
s = input('문자열 입력: ')
s1 = '''1행
2행
3행
'''
f = open('../data/write prac2.txt', 'a', encoding= 'utf-8')
f.write(s1)

#4. 파일을 생성(쓰기)하고 읽기

filename = '../data/readwrite.txt'
f1 = open(filename,'a',encoding='utf-8')
for i in range(5):
    f1.write(input(f'{i+1}번째 문자열 입력: '))
f1.close()

f2 = open(filename,'r',encoding= 'utf-8')
print(f2.read())
f2.close()