try:
    4/0
except ZeroDivisionError as e:
    print(e)

#try-finally
try:
    f=open("foo.txt", "w")

finally:
    f.close()


#여러 개의 오류 처리 
try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#try-else
try:
    age=int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age<=18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")

