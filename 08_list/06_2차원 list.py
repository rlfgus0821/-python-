# 2차원 리스트 : [행][열]

table = [[1,2,3,4],[7,9,8,10],[11,12,13,14]]
print(table)
print(table[0])

for item in table:
    print(item, type(item), len(item))

for row in table:
    for col in row:
        print(col, end=' ')
    print()

# 문제1. 학생별 과목별 점수와 총점, 평균 계산하고 출력
a = [[90,85,70], [88,79,92], [100,100,100], [90,60,70]]
print('---성적표 (점수)---')
for i in range(len(a)):
    print(a[i])
print()

print('---성적표 (점수, 총점, 평균)---')
for i in a:
    tot = 0
    for s in i:
        tot += s
    avg = tot / len(i)
    print(f'{i}, {tot}, {avg:.2f}')