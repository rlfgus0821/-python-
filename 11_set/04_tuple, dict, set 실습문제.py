students = [{'name':'홍길동','kor':87,'math':98,'eng':88,'sci':95},
{'name':'이몽룡','kor':92,'math':98,'eng':96,'sci':98}]
#1. 학생들의 이름과 성적이 있는 딕셔너리를 사용하여 각 학생의 성적에 대한 총점과 평균을 출력

print(f"이름    총점    평균")
for std in students:
    tot = std['kor'] + std['math'] + std['eng'] + std['sci']
    avg = tot/4
    print(f"{std['name']}    {tot}    {avg:.1f}")

#2. 딕셔너리를 이용하여 사용자로부터 영어단어와 뜻을 입력
din = dict()

while True:
    a = input('영어 단어 등록(종료는 quit) : ')
    if a.lower() =='quit':
        break
    else:
        b = input(f'{a}의 뜻입력 : ')
        if a in din:
            print('이미 등록된 단어입니다.')
            continue
        else:
            din.setdefault(a, b)
c = 0
while True:
    c = input('검색할 단어 입력(종료는 quit): ')
    if c.lower() =='quit':
        print('종료합니다.')
        break
    if c.lower() !='quit':
        meaning = din.get(c)
        if meaning is None:
            print('등록되지 않은 단어입니다.')
    else:
        print(din[c])
#6. 주어진 문제를 해결하기 위한 파이썬 코드를 작성하시오.
#6-1. my_variable 이름의 비어있는 튜플 생성
my_variable = tuple()
#6-2. 숫자1이 저장된 튜플 생성
my_variable = (1,)
print(my_variable)
#6-3. 변수 t에 'a', 'b', 'c' 세 문자열을 갖는 튜플을 생성
t = ('a','b','c') # t=tuple('abc')
print(t)
#6-4. 6-3에서 생성한 변수 t가 ('A','B','C')튜플을 가리키도록 생성
t = ('A','B','C')
print(t)
#6-5. 다음 튜플을 리스트로 변경
interest = ('삼성전자', 'LG전자', 'sk hynix')
a= list(interest)
print(a)
#6-6. 다시 튜플로 변경
b = tuple(a)
print(b)
#6-7. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만든 후 출력
t = (1,2,3) + (4,)
print(t)
#6-8. 'B'에 해당하는 값 추출하고 삭제
a = {'A':90,'B':80,'C':70}
b = a.pop('B')
print(b, a)

#7. 세트를 생성하고, 아래 조건에 맞게 출력하는 코드작성
partyA = 'park','kim','lee'
partyB = 'park','길동','몽룡'
#7-1. 파티에 참석한 모든 사람은?
s = set(partyA)
s1 = set(partyB)
print(s|s1)
#7-2. 2개의 파티에 모두 참석한 사람은?
print(s&s1)
#7-3. 파티A에만 참석한 사람
print(s-s1)
#7-4. 파티B에만 참석한 사람
print(s1-s)
