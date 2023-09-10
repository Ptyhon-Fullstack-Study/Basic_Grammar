odd = [1, 3, 5, 7, 9]
print(odd)
print(odd[0])
print(odd[-1])

a = [1, 2, 3, [3, 2, 1]]
print(a[3])
print(a[3][1])
print(a[:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)
print(len(a))

# del?
a.append(4)
print(a)

a = [4, 5, 3, 2]
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(2))
a.insert(0, 1)
print(a)
a.remove(1)
print(a)

print(a.pop())
print(a)

b = [6, 7, 8]
a.extend(b)
print(a)


