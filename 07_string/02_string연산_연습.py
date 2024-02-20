# 문자열의 모든 글자 뒤에 $ 붙이자
text = '파이썬짱!'
for tt in text:
    print(tt,end='$')
print()

# 문자열의 짝수번째 글자는 모두 #으로 변경하여 출력하기
# 방법 1.
s = '파이썬은재미있어요'
s1 = s[::2]
for tt in s1:
    print(tt,end="#")
print()
# 방법 2
s = '파이썬은재미있어요'
temp = ''
s1 = s[::2]
for tt in s1:
    temp += tt + '#'
print(temp)
print()
# 방법 3.
temp = ''
cnt = -1
for ch in s:
    if cnt%2==0:
        ch = '#'
    else:
        pass
    temp += ch
    cnt += 1
print(temp)
# 방법 4.
temp =''
for i in range(ien(s)):
    ch = '#' if i % 2 ==1 else s[i]
    temp += ch
print(temp)

