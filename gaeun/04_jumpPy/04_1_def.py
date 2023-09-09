def add(a,b):
    result=a+b
    return result

a=add(3,4)
print(a)

#입력값이 없는 함수
def say():
    return "Hi"
a= say()
print(a)

#리턴 값이 없는 함수
def add(a,b):
    print("%d,%d의 합은 %d입니다." %(a,b, a+b))
add(3,4)

#매개변수를 지정하여 호출하기
def sub(a,b):
    return a-b
result=sub(a=7, b=3)
print(result)

#여러 개의 입력값을 받는 함수
def add_many(*args):
    result=0
    for i in args:
        result+=i
    return result

result=add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice=="add":
        result=0
        for i in args:
            result+=i
    elif choice=="mul":
        result=1
        for i in args:
            result*=i
    return result

result = add_mul("add", 1,2,3,4,5)
print(result)

result= add_mul("mul", 1,2,3,4,5)
print(result)

#키워드 매개변수
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)


def say_nick(nick): #리턴값이 없는 함수에서 return으로 함수를 빠져나가
    if nick=="바보":
        return
    print("나의 별명은 %s 입니다." %nick)
say_nick("야호")
say_nick("바보")

#매개변수 초깃값 미리 설정하기
def say_myself(name, age, man=False):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용",27)
say_myself("박응용",27,True)
        
#함수 안에서 함수 밖의 변수 변경
a=1
def vartest(a):
    a+=1
    return a

a= vartest(a)
print(a)

a=1
def vartest():
    global a #함수 밖의 a변수 사용
    a+=1

vartest()
print(a)

#lambda
add= lambda a,b: a+b
result = add(3,4)
print(result)


