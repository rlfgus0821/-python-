# 다중 for문 이용

for x in range(3):
    for y in range(1,5):
        print(y+4*x, end=' ')
    print()

# 구구단 (2~9단)
for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan:2d}*{n:3d}={dan*n:>2}')
    print()
