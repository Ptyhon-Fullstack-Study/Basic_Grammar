a = [1, 2, 3]
print(id(a))

b = a
print(id(b))

b = a[:]
print(id(b))

from copy import copy
a = [ 1, 2, 3]
print(id(a))
b = copy(a)
print(id(b))

print(b is a)