def add(a, b):
    return a + b

def say():
    return 'Hi'


def add_many(*args):
    result = 0 
    for arg in args:
        result += arg 

    return result

add_many(1, 2, 3, 4, 5)


def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(
    a = 1,
    foo =2
)

def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
        
# 함수 안에서 함수 밖의 변수를 변경하는 방법

a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)


add = lambda a, b: a+b