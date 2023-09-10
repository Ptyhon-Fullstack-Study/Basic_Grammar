# 숫자형은 어떻게 만들고 사용할까?

# 정수형 
a = 123
a = -178
a = 0

# 실수형 
a = 1.2
a = -3.45
a = 4.24E10
a = 4.24e-10


# 8진수와 16진수
a = 0o177
print(a)

b = 0xABC
print(b)

# 사칙 연산
a = 3 ; b =4 
print(a + b ,a-b , a * b , a / b)

# X의 Y 제곱
7 ** 4
# 나눗셈 후 나머지
7 % 4  
# 나눗셈 후 몫
7 //4


# 문자열은 어떻게 만들고 사용할까?

# 문자열을 만들어 주는 주인공은 작은따옴표(')와 큰따옴표(")이다. 
# 그런데 문자열 안에도 작은따옴표와 큰따옴표가 들어 있어야 할 경우가 있다. 
# 이때는 좀 더 특별한 기술이 필요하다. 
# 예제를 하나씩 살펴보면서 원리를 익혀 보자.

# 문자열에 작은따음표 포함하기 
food = "Python's favorite food is perl"

# 문자열에 큰따음표 포함하기 
say = '"Python is very easy." he says.' 

# 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기 
multiline='''
Life is too short
You need python
'''
multiline="""
Life is too short
You need python
"""

# 이스케이프 코드 
'''
\n
\t 
\\ 
\'
\"
'''

# 문자열 연산하기 
# 파이썬에서는 문자열을 더하거나 곱할 수 있다. 
# 이는 다른 언어에서는 쉽게 찾아볼 수 없는 재미있는 기능으로, 
# 우리 생각을 그대로 반영해 주는 파이썬만의 장점이라고 할 수 있다. 
# 문자열을 더하거나 곱하는 방법에 대해 알아보자.

# 문자열 더해서 연결하기

head = "Python"
tail = " is fun!"
head + tail

# 문자열 곱하기 
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기 
a = "Life is too short"
len(a)

# 문자열 인덱싱
a = "Life is too short, You need Python"
a[0] 
a[12]
a[-1]

# 문자열 슬라이싱 
a[0:3]

# 이렇게 되는 이유는 슬라이싱 기법으로 
# a[시작_번호:끝_번호]를 지정할 때 
# 끝 번호에 해당하는 문자는 포함하지 않기 때문이다. 
# 즉, a[0:3]을 수식으로 나타내면 다음과 같다.

print(a[19:-7])

a = "20230331Rainy"
date = a[:8]
weather = a[8:]
date

# Pithon 문자열을 Python으로 바꾸려면?
a = "Pithon|"
a[1] = 'y'  # TypeError: 'str' object does not support item assignment

a[:1] + 'y' + a[2:]

# 문자열 포매팅 따라 하기

"I eat %d apples." % 3
"I eat %s apples." % "five"

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

"Error is %d%%." % 98

# 정렬 
"%10s" % "hi"

"%-10sjane." % 'hi'

# 소수점 표현 
"%0.4f" % 3.42134234

# format 함수를 사용한 포매팅
"I eat {0} apples".format(3)
# "I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

# 정렬
"{0:<10}".format("hi") # 문자열 길이 10, 왼쪽정렬
"{0:^10}".format("hi") # 문자열 길이 10, 가운데정렬 

y = 3.42134234
"{0:0.4f}".format(y)

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
 
f'{"hi":<10}'
f'{"hi":>10}'
f'{"hi":=^10}'
loss = 0.2423242314123
f'loss:{loss:.3f}'

# 문자열 관련 함수들
a = "hobby"
a.count('b')
a.find('b') # 처음으로 나온 위치 반한 
a.index('t') # 없으면 에러 발생 

",".join('abcd')
",".join(['a', 'b', 'c', 'd'])
''.join(['a', 'b', 'c'])

a.upper()
a.lower() 
a.strip()
a.replace("Life", "Your leg")

a = "Life is too short"
a.split()