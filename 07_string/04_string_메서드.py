#1. 문자열 대소문자 변환
# upper(), lower(), title(), capitalize()
text1 = 'python is great!'
text2 = "yes, it is."
text3 = "it's not like any other"

print(f'text1:{text1}')
print(f'text2:{text2}')
print(f'text3:{text3}')

print('대문자로', text1.upper())
print('소문자로', text1.lower())
print('단어별 시작문자 대문자로', text1.lower().title())
print('문장의 첫글자만 대문자로', text1.upper().capitalize())
print('대문자<->소문자', text1.swapcase())

#2. 문자열 검색
# count(단어): 단어가 몇개있는지, find(단어), rfind(단어), index(단어), rindex(단어)
text1 = 'python is great!'
text1.count('python')
print('count():', text1.count('python'))
print('find():', text1.find('python'))
print('rfind():', text1.rfind('python'))
print('rfind():', text1.rfind('melon'))
print('index():', text1.index('great'))
print('rindex():', text1.rindex('great'))
print('startswith()', text1.startswith(python))
print('endswith()', text1.endswith(python))

#3. 문자열 치환, 편집
# strip(), rstrip()오른쪽, lstrip()왼쪽 : 공백문자(지정문자) 제거
# replace() : 문자치환
text5 = '         ham haha hotong    '
text6 = '<><><><>ham haha hotong>>>>>'

print('strip():', text5.strip())
print('lstrip()왼쪽만 제거:', text5.lstrip())
print('rstrip()오른쪽만 제거:', text5.rstrip())
print('strip("<>"):', text6.strip('<>'))
print('replace(1,2)1을 2로 단어교체:', text5.replace('ham','hom'))

#4. 문자열을 분리/결합
# split(): 분할 ,rsplit(),splitlines(), join(): 합치기
text5 = '         ham haha hotong    '
print('split():',text5.split())
print('rsplit():',text5.rsplit())
text8 = 'apple banana kiwi'
data = text8.split()
print(data)
print('join():', '-'.join(data))
print('join():', 'and'.join(data))

text9 = 'firstline\
secondline\
thirdline'
print(text9.split('\n',1))
# print(text9.split('\n',최대 나눌 수 - 1))
print(text9.splitlines())

#5. 문자열 정렬
# center(), ljust(), rjust() :
text8 = 'apple banana kiwi'
print('center():가운데 정렬', text8.center(30))
print('lust():왼쪽정렬', text8.ljust(30,'!'))
print('rust():오른쪽정렬', text8.rjust(30))

#6. 문자열 판단
# isdigit(), isdecimal(), isalpha() ....
print('1234'.isdigit())
print('1234'.isalpha())
print('ㅁㄴㅇasd'.isalpha())
print('1234'.isalnum())
print('hello'.isupper())
print('hello'.islower())
print('hello'.istitle())

# 유니코드 보는 법 ->  Unicode : \u0101
print('\u2665')