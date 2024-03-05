# Day1 ; 변수에 대해서 실습

# 변수란 데이터를 저장하는 메모리 주소
# 파이썬의 변수 : 동적타이핑, 레퍼런스 / 변수선언 필요없음
# id(), type()
# print()


# 실습1 : 두 변수의 값 교환(Swap)

# 방법1 : 고전적 방식

a = 10
b = 5
print(a, b)

temp = a
a = b
b = temp
print(a, b)

# 방법2 : 파이썬 방식

a, b = 10, 5
print('a=', a, 'b=', b)
a, b = b, a
print('a=', a, 'b=', b)

# 실습2 : 변수 삭제
del a


# 실습3 : 변수의 값 출력 print()
age = 30
name = 'HongGilDong'
print(name, age)

addr = '서울시 서초구'
result = name + '은' + addr + '에 살아요'
print(result)

print(name + ' 나이는' + str(age) + '입니다')
# TypeError : 문자열과 숫자는 연결할 수 없다 -> age = 30(정수)라서 문자 + 숫자는 불가능
# 숫자를 문자열로 변환하는 함수 활용 : str(숫자)


# 실습4 : 변수를 이용한 계산 결과값 출력
# 삼각형의 넓이 계산

w = 10
h = 5
s = w*h/2
print('넓이=', s)

# print() 함수의 다양한 출력
# print('문자열' , 변수)


# print('서식'% 값) 
print('넓이=%f' % s)

# 포맷 서식
# 방법1 : '서식'% 값
# format string ; %f , %d , %s

# ex) result = name + '은' + addr + '에 살아요' -> result = '%s은 %s에 살아요' %(name, addr)
result = '%s은 %s에 살아요' %(name, addr)
print(result)

# %를 쓰고 싶은데 format string으로 인식해서 오류가 난다
pcnt = 10.5
result2 = '전체면적의 %.3f%%입니다'% pcnt
print(result2)

# 방법2 : format() 함수
# format(숫자, '숫자서식') -> .2f = 소수점 2자리 까지, .3f = 3자리 까지 / 100, 5d = ( 100)

result4 = format(s, '넓이=.2f')
print(result4)

# 연습문제
# 다음의 변수 값들을 이용하여 총점과 평균을 계산해서 예시와 같이 출력하기

kor = 90
eng = 80
math = 75

tot = kor + eng + math
avg = format(tot/3,'.2f') 
print('총점 :', tot , '평균 :' , avg)

print('총점: %d , 평균: %.2f'%(kor + eng + math), (kor+eng+math)/3)

# 방법3 : '{0:서식}{1:서식}'.format( , ) 함수
print(format(3.141592, '10.3f'))
print('{0:.3f}'.format(3.141592))
print('{0:5d} {1:05d} {2:.3f}'.format(kor , eng , math))

# 방법4 : f'string (!!가장 최신방법!!)
# {}안에 변수를 넣어주면 된다
# ex) number = 123.456789 / f'{number:.2f} -> 123.45

print(f'수학점수는 {math:05d}이고 , 국어점수는 {kor:.3f}이고, 영어점수는 {eng:5d}이다')

balance = 10300.0
print(balance)
print(int(balance))
print(format(int(balance), '.'))

# 상수 : 고정된 변수
# 리터럴 : 값 그 자체, 실수 , 정수 , 문자 , 문자열, none , True , False

# print()함수의 매개변수 활용
print(kor, math, eng, sep='')
print(kor, math, eng, end='')
