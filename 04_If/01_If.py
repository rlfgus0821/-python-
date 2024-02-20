
# 조건문

# if문
num = int(input('정수입력:'))
if num > 10:
    print('10보다 크네요')

# if~ else문
if num > 10:
    print('10보다 크네요')
else:
    pass
# 연습문제1. 로그인
ID = input('아이디 입력 :')
Password = input('비밀번호 입력:')
if ID =='flower' and Password =='1234':
    print('로그인 성공')
else:
    print('로그인 실패')
    
# 중첩 if : if 조건이 만족하는 경우 또 다른 조건에 따라 실행
if ID == 'flower':
    if Password == '1234':
        print('로그인 성공')
    else:
        print('로그인 실패 : 비밀번호가 다릅니다')
else:
    if Password == '1234':
        print('로그인 실패 : 아이디가 다릅니다')
    else:
        print('로그인 실패 : 아이디와 비밀번호 모두 다릅니다')

# if~ elif~else문 : 위에 else if 와 elif와 같다
elif Password == '1234':
    print('로그인 실패 : 아이디가 다릅니다')
else:
    print('로그인 실패 : 아이디와 비밀번호 모두 다릅니다')

# 연습문제 : 점수 입력 (0~100)받아서 학점 출력
# 90점 이상 : A, 80~90 : B, 70~80 : C, 60~70 : D, 60점 미만 : F
num = int(input('점수를 입력하시오:'))
if 100>num>= 90:
    score = 'A학점'
elif 90>num>=80:
    score = 'B학점'
elif 80>num>=70:
    score = 'C학점'
elif 70>num>=60:
    score = 'D학점'
else:
    score = 'F학점'
print(f'{num}에 대한 학점은 {score}입니다')
