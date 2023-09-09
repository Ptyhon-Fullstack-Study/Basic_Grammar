a=[1,2,3,["a","b","c"]]
print(a[-1])
print(a[-1][0])

b=[1,2,["a","b",["Life","is"]]]
print(b[2][2][0])

c= [1,2,3,["a","b","c"],4,5]
print(c[2:5])
print(c[3][:2])
print(len(c))

d=[1,2,3]
d[2]=4
print(d)

e= [1,2,3,4,5]
del e[2:]
print(e)

print(e)

e.append([5,6])
print(e)

f=[1,4,3,2]
f.sort()
print(f)
print(f.index(4))
f.insert(0,4)
print(f)


