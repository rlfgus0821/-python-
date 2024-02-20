# 1. 문자나열
text1 = 'python is great!'
text2 = "yes, it is."
text3 = "it's not like any other"
text4 = "Don't walk."
text5 = "This is \
contain \
temp"

# 2. 문자열 포맷지정
# 1) 포맷코드 : '%5d, %10s, %.2f' %()
# 2) '{0: 2d},{2: .2f},{1:10s}', format( , , )
# 3) format(변수, '서식') : format(bmi, '.2f')

# 3. 날짜 출력 포맷 : 주민번호 / 전화번호 / 우편번호 / 시간 / 날짜
# 모듈 : 함수나 변수를 모아놓은 파일
from datetime import date, datetime

today = date.today()
print(today, type(today))
print(f'오늘은 {today.year}년, {today.month}월, {today.day}일')

curr_time = datetime.now().time()
print(curr_time,type(curr_time))

print(f'{curr_time.hour}시, {curr_time.minute}분, {curr_time.second, \
      curr_time.microsecond}초')

from datetime import date, datetime, timedelta
# timedelta : 날짜 계산을 할 때 사용 / today + timedelta(days=2) = 오늘로 +2일
print(timedelta(days=-1))
print(timedelta(weeks=-1))
print(timedelta(hours=-1))
# 포맷 형태로 출력할 수 있다 : strftime()
today.strftime('%y년 %m월 %d일 %h:%m:%s')

4. 문자열 정렬
왼쪽정렬 : < / 오른쪽 정렬 : > / 가운데 정렬 : ^ / 공백문자 지정 : 아무 문자

text1 = 'python is great!'
print(f'{text1:^}')
print(f'{text1:-<20}')
print(f'{text1:a<20}')
