marks = [90, 25, 67, 45, 80]

for i, mark in enumerate(marks):
    if mark >= 60 :
        print(f'{i}번 학생은 합격입니다.')
        
    else :
        print(f'{1}번 학생은 불합격입니다.')
        
        
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j , end=" ")
    print('')
    
    
a = [1, 2, 3, 4]
result = [num * 3 for num in a]

# [표현식 for 항목 in 반복_가능_객체 if 조건문]

result = [x*y for x in range(2,10) for y in range(1, 10)]
result