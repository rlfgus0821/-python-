
# n개 정수를 입력받아 합계와 평균 출력
n = 4
tot = 0
num_list = list() #같은 의미 num_list = list()
for i in range(n):
    num = int(input(f'{i+1}숫자입력:'))
    num_list.append(num)
    tot += num
avg = tot /4
print('num_list = ',num_list)

for num in num_list:
    print(num,end='')

# 리스트 생성 : [], list() / 리스토 요소 추가 : append
a = list()
for i in range(100):
    a.append(0)
print(len(a))

# 리스트의 요소를 출력
#1.
for i in range(len(num_list)):
    print(num_list[i])
#2.
for x in num_list:
    print(x)