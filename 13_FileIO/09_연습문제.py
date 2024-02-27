#1. 파일 s.txt에 있는 줄들을 정렬해서 출력
with open('../data/mysum.txt','r') as f:
    flist = f.readlines()
    print(flist)
flist.sort()
print(flist)

# #2. Yesterday 가사가 저장되어 있는 텍스트 파일을 읽어 가사에 사용되고 있는 단어들의 목록을 알파벳 순서로 출력하고,
# # 각 단어들이 몇 개씩 사용되고 있는지 단어별 개수를 출력하는 프로그램 작성
# # 리스트, 세트, 딕셔너리 등의 자료구조를 이용
# # 단어들은 모두 소문자로 변환하여 사용한다.
list1=[]
list2=[]
list3=[]
with open('../data/yesterday.txt','r') as f:
    list1=f.readlines()
    list1.sort()
for i in list1:
    a = (i.strip('\n').split(' '))
    for s in a:
        list2.append(s.lower())
        for b in list2:
            if b == '':
             list2.remove('')
            if b != '':
             continue
print(list2)
for i in list2:
    for a in i:
        list3.append(a)
        print(f'{a}:{list3.count(a)}')

# #3. 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와 한 줄의 두 숫자를 더한 후 연산 결과를 파일로 내보내는 프로그램 작성
# #3-1. 파일을 읽어오고 파일에 쓰고, 숫자에 대해 연산하는 기능은 함수 my_sum()을 정의하여 사용 my_sum(inputfile 객체,저장파일명)
def my_sum(filename, mode = 'r'):
    with open(filename) as f:
        flist = f.readlines()
    for i in flist:
        s = i.split(' ')
        tot = int(s[0]) + int(s[1])
        print(tot)

#3-2. 메인에서는 해당 함수를 호출해서 수행

my_sum('../data/mysum.txt')

#4. 회원명단 파일을 생성하고 읽기
i = input('저장 1, 출력 2, 종료 q :')
if i == '1':
    a = input('멤버 명단을 저장할 파일명을 입력하세요 :')
    with open('../data/' + a, 'a', encoding='utf-8') as f:
        while True:
            mem = input(f'멤버를 입력하세요.(종료는 q) : ')
            if mem.lower() != 'q':
                memlist = f.write(mem+'\n')
                print('저장이 완료되었습니다.')
            if mem.lower() == 'q':
                print('종료되었습니다.')
                break
if i == '2':
    a = input('멤버 명단을 저장된 파일명을 입력하세요 :')
    with open('../data/' + a, 'r', encoding='utf-8') as f:
        flist = f.read()
    print(flist)
if i == 'q':
    print('종료되었습니다.')
