#예제1. 3명의 회원을 입력받아 리스트에 추가하자.
# for 이용
namelist = []
for i in range(3):
    name = input('회원 입력: ')
    namelist.append(name)
print(namelist)
print()

# while 이용
i = 0
while i < 3:
    name = input('회원 입력: ')
    namelist.append(name)
    i += 1
print(namelist)
for name in namelist:
    print(name,end=', ')
print()

#예제2. 학생 5명 점수를 입력받아 리스트에 추가하고 총점과 평균 계산

namelist = []
tot = 0
n = 5
for i in range(n):
    score = int(input(f'학생{i + 1} 점수 입력: '))
    namelist.append(score)
    tot += score
avg = tot / len(namelist)
print(f'점수: {namelist}, 총점: {tot}, 평균: {avg:.2f}')

#예제3. 예제2에서 80점 이상의 학생 수를 계산하여 출력
cnt = 0
for i in namelist:
    if i>= 80:
        cnt += 1
print(f'80점 이상 학생 : {cnt}명')

