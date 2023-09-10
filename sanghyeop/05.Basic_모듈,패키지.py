
# 모듈
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
# 모듈의 목적은 다른 파이썬 프로그램에서 불러다가 사용할 수 있도록 만든것.


# mod1.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

# 만약 위에처럼 mod1.py라는 파일에 해당 2가지의 함수가 있다고 하자.

# mod1.py사용하기
import mod1
print(mod1.add(3,4)) # 이렇게 사용가능.

import mod1 import add
add(3,4) # 이렇게 사용도 가





# 패키지
# 패키지packages란 관련 있는 모듈의 집합을 말한다.
# 패키지는 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해 준다.

# 아래는 game이라는 가상의 패키지의 디렉토리 구조이다.
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py

# __init__.py 란?
# 디렉터리가 패키지의 일부임을 알려 주는 역할을 한다. 
# __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.
# example
# C:/doit/game/__init__.py
VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")



# 패키지를 이런식으로 호출해서 사용
import game.sound.echo
game.sound.echo.echo_test()
echo




# 예외처리
# 첫번째 방법 try-except문
# try_except.py
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


# 두번째방법 try-finally문
# try_finally.py
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.

    (... 생략 ...)

finally:
    f.close()  # 중간에 오류가 발생하더라도 무조건 실행된다.

# 여러개의 오류처리
# many_error.py
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


# try-else
# try_else.py
try:
    age=int(input('나이를 입력하세요: '))
except: #오류발생
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')



# 오류 회피하기
# error_pass.py
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass


#일부로 오류 발생시키
# error_raise.py
class Bird:
    def fly(self):
        raise NotImplementedError
