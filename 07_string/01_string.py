# 1. 문자열 생성

text = 'python is programming language'

# 2. 문자열 인덱싱 (인덱스)
print('text[-1] =', text[-1])

# 3. 문자열 슬라이싱 [:], [start:end:step]
# 부분문자열 반환

sub_text = text[2:10]
print('text[2:10] = ',sub_text)
print('text[::-1] =', text[::-1])
print('text[::2] =', text[::2])

# 4. + 연산, * 연산, str()
name = 'kim'
age = 20
person = name + str(age)
print(person, type(person))

print('len(text)=', len(text))

# 5. 멤버연산 : in ,not in
if 'python' in text:
    print('exist!')
else:
    print('not exist!')

for ch in text:
    print(ch, end='*')