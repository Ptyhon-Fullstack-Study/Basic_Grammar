multiline= """
Life is too short
You need python
"""
print(multiline)

print("="*50)
print("My Program")
print("="*50)

a="Life is too short"
print(len(a))

a="20230331Raniny"
year = a[:4]
day=a[4:8]
weather=a[8:]
print(year)
print(day)
print(weather)

a= "pithon"
b=a[:1]+"y"+a[2:]
print(b)

c= "%10s" %"hi"
print(c)

d= "%10.4f" % 3.42134234
print(d)

e=" i ate {0} apples. so i was sick for {day} day." .format(10, day=3)
print(e)
