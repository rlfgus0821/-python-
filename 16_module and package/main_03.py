# main

name = ''
def inname():
    global name
    name = input('이름 입력: ')

def getname():
    if name == '':
        return 'no name'
    else:
        return name

# 이 모듈에서 실행을 하게 될 경우 아래가 메인이 되어 실행이됨
# 단독 실행되면 수행되고 다른 파일에 import 되면 수행되지 않는다
if __name__=='__main__':
    inname()
    print(getname())
# main import / 만약 다른 파일에서 모듈을 불러왔을 경우 main 모듈 자체가 메인이 아니라서 전체실행x
import main_03
print(main_03.getname())