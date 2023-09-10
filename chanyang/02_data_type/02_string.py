# ' '
# " "
# """ """
# ''' '''

print('"Python is very easy." he says')
print("Python's favorite food is perl")

multiline='''
Life is too short
You need python
'''
print(multiline)

multiline= """
Life is too short
You need python
"""
print(multiline)

# \\ \' \"

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a*2)
print(len(a))

a = "Life is too short, You need Python"
print(a[3])
print(a[-1])

print(a[0] + a[1] + a[2] + a[3])
print(a[0:4])
print(a[4:])
print(a[:4])
print(a)

a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "Pithon"
modified_a = a[:1] + 'y' + a[2:]
print(modified_a)

print("I eat %d apples." %3)
print("I eat %s apples." % "five")

print("%0.4f" % 3.141592)

print("I eat {0} apples".format(3))

name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

print(name.count('홍'))
print(name.find('홍'))
print(name.index('홍'))
print(name.join('짱구는못말려'))

a = " hi"
print(a.lstrip())
print(a)
print(a.rstrip())

a = " hi "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a)
print(a.split())

b = "a:b:c:d"
print(b.split(':'))