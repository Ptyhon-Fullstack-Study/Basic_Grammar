

# if문
money = True
if money:
     print("택시를 타고 가라")
else:
     print("걸어 가라")

# 조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다. 각각의 연산자는 다음처럼 동작한다.
print()
money = 2000
card = True
if money >= 3000 or card:
     print("택시를 타고 가라")
else:
     print("걸어가라")

# in, not in
print()
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print()
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
     print("택시를 타고 가라")
else:
     print("걸어가라")


# 다양한 조건을 판단하는 elif
print()
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else:
     print("걸어가라")




# while문
print()
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# while문 강제로 빠져나가기
print()
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# while 문의 맨 처음으로 돌아가기
print()
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue  # continue 문은 while 문의 맨 처음인 조건문(a < 10)
    print(a)

# 무한루프 while True:




# for문
print()

test_list = ['one', 'two', 'three'] 
for i in test_list:
     print(i)



print()
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)



# for 문과 continue 문
print()
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue   # if조건에 맞을경우 continue를 수행 -> for문의 처음으로 돌아감.
    print("%d번 학생 축하합니다. 합격입니다. " % number)



# for 문과 함께 자주 사용하는 range 함수 

print()
a = range(10)
print(a)

add = 0 
for i in range(1, 11):
     add = add + i 
print(add)



# for와 range를 이용한 구구단
for i in range(2,10):        # 1번 for문
     for j in range(1, 10):   # 2번 for문
          print(i*j, end=" ")
     print('')

print()
print()
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)



    
