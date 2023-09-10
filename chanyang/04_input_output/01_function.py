def add(a, b):
    return a + b


print(add(3, 4))

def add_many(*args):
    result = 0
    for i in args:
        result = result + i

    return result


print(add_many(1,2,3,4,5))

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name = 'foo')

# default1.py
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

# lambda
add = lambda a, b: a+b
print(add(3,4))