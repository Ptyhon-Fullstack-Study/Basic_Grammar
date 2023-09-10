# 파이썬으로 파일 생성하기

f = open("1.txt", 'w')
f.close()

f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파이썬으로 파일 읽기

f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()


f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("C:/doit/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

 #파일 객체(f)는 기본적으로 위와 같이 for 문과 함께 
 # 사용하여 파일을 줄 단위로 읽을 수 있다.
 
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")