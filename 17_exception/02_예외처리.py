# # 예외처리 형식
# # try:
# #    예외 발생가능한 문장들
# # except:
# #    예외처리
# # else:
# #     예외 발생하지않는 경우 처리문장들
# # finally:
# #     예외 발생과 상관없이 항상 처리
#
# # 예외처리가 광범위한 경우
# try:
#     print('나이'+23+'살')
#     print(10/0)
# except:
#     print('오류발생')
#
# try:
#     print('나이'+23+'살')
#     print(10/0)
# except Exception:
#     print('오류발생')
#
# # 에러 종류에 따른 구체적인 오류 담당하는 에러 클래스를 이용하여 처리
# # 에러의 종류가 명시
# # 에러메시지 변수를 활용하여 출력: 에러 담당 클래스 as 에러 메시지 변수명
# # try:
# #     에러 발생가능한 문장들
# # except 에러 담당 클래스명 as 에러메시지 변수명:
# #     에러처리 문장들
#
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없습니다.',e)
#
# try:
#     num = int(input('숫자입력: '))
#     print(num)
# except ValueError:
#     print('숫자가 아닙니다')
#
# # 첫번째 에러만 처리하고 끝난다.
# try:
#     print(10/0)
#     print('나이' + 23 + '살')
# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없습니다.',e)
# except TypeError as e:
#     print('잘못입력된 형식입니다',e)
#
# # else: 에러가 없을 경우 else문 실행
# # finally: 에러가 발생하든 안하든 실행
# try:
#     num = int(input('숫자입력: '))
#     print(num)
# except ValueError:
#     print('숫자가 아닙니다')
# else:
#     num += 10
#     print(num)
# finally:
#     print('-----종료-----')

import random
answer = random.randint(1,10)
def guess_number(answer):
    try:
        guess = int(input("숫자를 넣어 주세요: "))
        if answer == guess:
            print("정답!")
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자가 아닙니다.")
guess_number(answer)