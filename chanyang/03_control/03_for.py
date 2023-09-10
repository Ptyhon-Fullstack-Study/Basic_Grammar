test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, second) in a:
    print(first+second)

marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

add = 0
for i in range(1, 11):
    add = add+i
print(add)

# list comprehension
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num)
print(result)

result = [num for num in a]
print(result)