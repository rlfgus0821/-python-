#. 실습문제
#1. 회원이름을 입력받아 회원명단 리스트를 생성, 출력
namelist = []
n = 3
for i in range(n):
        a = input('회원 입력: ')
        namelist.append(a)
print(f'회원 명단: {namelist}')

#2. 학생 수를 입력받아 점수와 총점 평균을 계산하고, 80점 이상인 학생의 수를 출력
tot = 0
cnt = 0
n = int(input('학생 수 입력: '))
for i in range(n):
        a = int(input( f'학생{i+1} 점수 입력: '))
        tot += a
        if a>= 80:
                cnt += 1
print(f'총점: {tot}')
print(f'평균: {tot/3:.2f}')
print(f'80점 이상 학생: {cnt}')

#3. 상품을 리스트에 추가하고 출력
n = 3
namelist = []
for i in range(n):
        a = input('상품등록(엔터키 누르면 종료): ')
        namelist.append(a)
print(f'등록된 상품 : {namelist}')

#4. 2번 문제에서 학생들의 점수를 내림차순으로 정렬
tot = 0
cnt = 0
namelist = []
n = int(input('학생 수 입력: '))
for i in range(n):
        a = int(input( f'학생{i+1} 점수 입력: '))
        tot += a
        namelist.append(a)
        namelist.sort(reverse=True)
        if a>= 80:
                cnt += 1
print(f'총점: {tot}')
print(f'평균: {tot/3:.2f}')
print(f'80점 이상 학생: {cnt}')
print(f'점수 내림차순 정렬: {namelist}')

#5. 사자성어 맞추기 게임을 작성하시오. : 사자성어를 맞출 때까지 계속한다.
alist = ['개과천선', '구사일생', '군계일학', '무용지물', '동고동락', '유비무환', '입신양명', '괄목상대', '막역지우', '고장난명']
blist = ['잘못을...', '죽일...', '평범한...', '아무짝...', '고통과...', '미리...', '사회적...', '다른...', '생사를...', '상대...']

print('사자성어 맞추기 게임을 시작합니다')
print('-------------------------------')
i = 0
c = input(f'{blist[i]}? :')
while c != alist[i]:
        print('틀렸습니다...다시 도전 !')
        i += 1
        c = input(f'{blist[i]}? :')
while c == alist[i]:
        print('맞습니다.. 게임을 종료합니다.')
        break