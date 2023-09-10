treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        

>>> prompt = """
 1. Add
 2. Del
 3. List
 4. Quit

 Enter number: """

number = 0
while number != 4:
     print(prompt)
     number = int(input())
     
     
# while 문의 맨 처음으로 돌아가기
a = 0
while a < 10 :
    a+=1
    if a % 2 == 0 : continue
    print(a)
    
