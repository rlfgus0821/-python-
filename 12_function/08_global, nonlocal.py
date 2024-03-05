def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# 변수 사용 범위를 결정하기 위해 사용하는 키워드로 수업 시간에 배운 global과 알려주지 않은 nonlocal이 있습니다.
# 함수 외부와 내부 또는 함수내부에서 정의된 함수(중첩된함수)에서 사용되는 동일한 이름의 변수들의 경우 동일한 이름이라도  사용 범위가 구분되도록 새로운 변수처럼 생성되어 사용되는 것이 원칙입니다.
# 그런데, 두 키워드 모두 동일한 이름의 새로운 변수가 생성되는 것을 방지하기 위해서 사용합니다.
# global의 경우 함수 외부의 전역변수를 함수내부에서 사용하거나, 함수 내부에서 선언한 변수를 전역변수로 사용하려고 할 때 사용합니다.
# nonlocal은 함수 내부에서 선언된 내부함수(inner function)의 변수 사용 범위를 local에서 nonlocal로 사용하기 위해 변경하는 키워드입니다.
# 두 키워드의 차이점은 global 키워드는 일반 함수 내에서 전역(global/module) 변수를 대상으로 사용하는 반면에 nonlocal 키워드는 중첩 함수 내에서 비지역(nonlocal/closing) 변수를 대상으로 사용한다는 것입니다.
# 예제 프로그램을 보면,
# scope_test()함수 내부에서 선언한 do_local()함수의 spam변수는 do_local() 함수 내부에서만 사용되지만(local),
# scope_test()함수 내부에 선언한 do_nonlocal()함수의 spam 변수를 nonlocal로 선언하면 scope_test() 함수 내부 전체에서 사용가능하게 됩니다.
# scope_test()함수 내부에 선언한 do_global()함수의 spam변수는  global로 선언했기에 scope_test()함수 외부에서도 사용가능한 전역변수가 됩니다.
# 예제 프로그램 실행 순서를 보면,
# 1) scope_test()함수 호출
# 2) spam = "test spam"
#    spam 변수는 local 변수로 "test spam"을 저장
# 3) do_local() 함수 호출
#     spam = "local spam" 수행
#     이 spam 변수는 do_local() 함수의 내부변수로  'local spam'값이 저장되며,
#     2) 단계의 spam 변수와 다른 변수임
# 4) print("After local assignment:", spam)
#   => scope_test() 함수의 지역변수 spam값 출력
#       "After local assignment: test spam"
# 5) do_nonlocal() 함수 호출
#     nonlocal spam  # spam변수를 nonlocal로 선언
#      => scope_test() 함수 내부에서 사용 가능
#     spam = "nonlocal spam"
#      => "test spam"의 값을 갖던 spam변수의 값이 "nonlocal spam"으로 변경됨
# 6) print("After nonlocal assignment:", spam)
#   => nonlocal 변수 spam의 값 출력
#       "After nonlocal assignment: nonlocal spam"
# 7) do_global() 함수 호출
#    global spam # spam 변수 global로 선언
#     => scope_test()함수 밖에서도 사용가능한 전역변수가 됨
#    spam = "global spam"
#     => spam 변수 값이 "global spam"으로 저장
# 8) print("After global assignment:", spam)
#   => global 변수 spam의 결과 출력
#       "After global assignment: global spam"
# 9) print("In global scope:", spam) 실행
#   => global 변수  spam의 값 출력
#        "In global scope: global spam"
# [출력결과]
# "After local assignment: test spam"
# "After nonlocal assignment: nonlocal spam"
# "After global assignment: global spam"
# "In global scope: global spam"