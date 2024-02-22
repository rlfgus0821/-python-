# zip() 함수

food = ['떡','짜장','피자','라면']
side = ['김치','단무지','피클']

ziplist = list(zip(food, side))
zipdict = dict(zip(food, side))
print(ziplist)
print(zipdict)

# 리스트 컴프리헨션
alist = [num*2 for num in range(1,11)]
print(alist)

blist = [num + y for num in range(1,11) for y in range(10,21)]
print(blist,'\n', len(blist))
# tuple 컴프리헨션
flist = [(x,y) for x in ['밥','국수','짜장면'] for y in ['김치','단무지']]
print(flist)
# set 컴프리헨션
dlist = {num + y for num in range(1,5) for y in range(10,15)}
print(dlist,'\n', len(dlist))
# dict 컴프리헨션
print({f:s for f in food for s in side})
# {'떡': '피클', '짜장': '피클', '피자': '피클', '라면': '피클'}
# dict는 key가 중복될 수 없기 때문에 마지막 key부분만 반환

std = ['철수','영희','길동','순희']
std_dic = {s:0 for s in std}
print(std_dic)
# dict 컴프리헨션 예시
stds = {'철수':90,'영희':50,'길동':60,'순희':100}
stds_dic = {name : 'pass' if score > 60 else 'non-pass' for name ,score in stds.items()}
print(stds_dic)

