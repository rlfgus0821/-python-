# 리스트 컴프리헨션 : 값이 순차적인 리스트를 한 줄로 생성하는 방법
# 새로운 리스트 = [문장 for 변수 in range() (if 조건식)]
numlist =[]
for num in range(1,6):
    numlist.append(num)
print(numlist)
# 컴프리헨션 사용
numlist = [num for num in range(1,6)]
print(numlist)

numlist2 = [num*2 for num in range(1,6)]
print(numlist2)

# 문제1. : 1~20의 정수 중 짝수만으로 구성된 리스트 생성
#1.
numlist = []
numlist = [num for num in range(2,21,2)]
print(numlist)

#2.
numlist = [num for num in range(1,21) if num%2 == 0]
print(numlist)

# 문제2. : 1~20 정수 중 3의 배수로 구성된 리스트
numlist = [num for num in range(1,21) if num%3 == 0]
print(numlist)

# zip() : 리스트 2개를 묶어서 사용
food = ['떡볶이','짜장면','라면','피자']
side = ['단무지','김치','피클']
for food, side in zip(food, side):
    print(food, '---', side)

print(list(zip(food, side)))