# 정수형

print("정수형 테스트코드")
a = 123
print(a)
a = -178
print(a)
a = 0
print(a)


# 기본연산
print()
print("사칙연산  테스트코드")
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print()
print("x의 y제곱을 나타내는 ** 연산자")
a = 3
b = 4
print(a ** b)
print(a//b) # 몫 출
print(a%b) #나머지 출력



# 문자열 연산하기
print()
head = "python"
tail = " is fun!"
print(head + tail)
print(head*2) #문자열에서 "*"는 반복문의
print()
print("=" * 50)
print("My Program")
print("=" * 50)


# 문자열 인덱싱 슬라이싱
print()
a = "Life is too short, You need Python"
print(a[3])  #0,1,2,3 이므로 4번째 위치한 e가 출력 / 파이썬은 숫자를 0부터 셈
print(a[-1])
print(a[0:4])
print(a[0:3]) # 0 <= a < 3 이기 때문에 그럼
print(a[19:])
print(a[:])



# 문자열 포매팅
print()
print()
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 300
print("I eat %d apples." % number)
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))



# 리스트 자료형
print()
print()
odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
f = list() # 비어있는 리스트 생성

print(c)
print(c[2])
print(e[2])
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)
print(len(a))

a = [1, 2, 3]
a.append(4)
print(4)

a = [1, 4, 3, 2]
a.sort()
print(a)



# 튜플 자료형
print()
print()
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# 튜플의경우 리스트와 다르게 요소의 값을 한번 정하면 지우거나 변경할 수 없다 아래에 example
# t1 = (1, 2, 'a', 'b')
# del t1[0]
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object doesn't support item deletion
# 이외에 요소 추가 인덱싱 길이구하기 등 같은 조회성 함수는 가능



# 딕셔너리 자료형 (key = value 형태)
print()
print()
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)
a = {'a': [1, 2, 3]}
print(a) # 딕셔너리에 리스트 넣는 형태도 가능
print(dic['name']) # key를 통해 value 출력가능
c = dic.keys()
print(c)
d = dic.values()
print(d)


# 집합 자료형
print()
print()






































