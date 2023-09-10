f = open("./a.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("./a.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("./a.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("./a.txt", 'r')
for line in f:
    print(line)
f.close()

# with
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
