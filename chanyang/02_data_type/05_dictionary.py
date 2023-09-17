dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)

a = {1: 'a'}
print(a)
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)
print(a[1])

a = {1:'a', 1:'b'}
print(a)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())

a.clear()
print(a)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get(1))

print('name' in a)
print(1 in a)

