
# 함수
print()
def add(a, b): 
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)


# 일반적인 함수의 형태
def add(a, b): 
    result = a + b 
    return result

# 리턴값이 없는 함
def no_return(a, b): 
     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

print(no_return(3,4))



# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args):  # *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 만들어 줌
     result = 0 
     for i in args: 
         result = result + i   # *args에 입력받은 모든 값을 더한다.
     return result

result = add_many(1,2,3)
print(result)



# 활용법
def add_mul(choice, *args): 
     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
         result = 1 
         for i in args: 
             result = result * i 
     return result


result = add_mul('add', 1,2,3,4,5)
print(result)


# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 다음 예를 살펴보자.
def say_nick(nick): 
     if nick == "바보": 
         return 
     print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('바보')


# 매개변수에 초깃값 미리설정
def say_myself(name, age, man=True):  # man변수에 변수를 입력안해주면 디폴트로 True가됨.
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")



# 함수 안에서 선언한 변수의 효력 범위
def vartest(a):
    a = a + 1

vartest(3)
print(a) #에러가 나야하는데, print(a)에서 사용한 변수 a는 어디에도 선언되지 않았기 때문. 즉 함수안에서 선언한 매개변수는 함수 안에서만 사용됨.




# 사용자 input데이터 활용
number = input("숫자를 입력하세요: ")
print(number) 
print(type(number)) # input은 입력되는 모든 것을 문자열로 취급




# 파일 읽고 쓰기
f = open("새파일.txt", 'w')  # w:write / r: read / a: append 내용추
f.close()


# readlines
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()  # 한줄씩 읽음.
for line in lines:
    print(line)
f.close()


# with문 (자동으로 파일을 닫아줌)
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

    
