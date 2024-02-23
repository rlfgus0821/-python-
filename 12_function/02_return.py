# 함수 반환문 : return

def get_area():
    w = int(input('가로길이 : '))
    h = int(input('세로길이 : '))
    result = w*h
    print(f'사각형 가로 = {w}, 세로 = {h}, 면적은 {result}')
    return result
print(get_area())

def multi_return():
    return 1,2,3
print(multi_return(),type(multi_return()))
a,b,c = multi_return()
print(a,b,c)

def get_name():
    name = []
    for i in range(3):
        n = input('이름입력: ')
        name.append(n)
    return name
names = get_name()
print(names)

def get_info():
    name = input('이름입력: ')
    age =  int(input('나이'))
    info ={'name': name, 'age': age}
    return info
print(get_info())

