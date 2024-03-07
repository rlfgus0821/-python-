# 1. 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
set1 = set(range(3,1000,3))
set2 = set(range(5,1000,5))

print(sum(set1 | set2))

#2. n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다.
# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.
def sort_num(nlist):
    return [x for x in nlist if x < 0] + [x for x in nlist if x >= 0]

print(sort_num([-1, 1, 3, -2, 2]))