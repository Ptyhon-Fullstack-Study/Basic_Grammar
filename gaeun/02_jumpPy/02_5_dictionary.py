a={1:"a"}
a[2]="b"
print(a)

a["name"]="pey"
print(a)

a[3]=[1,2,3]
print(a)

#요소 삭제
del a[1]
print(a)

#Value
grade= {"pey":10, "julliet":99}
print(grade["pey"])

dic={"name":"pey", "phone":"010-9999-1234", "birth":"1118"}
print(dic["name"])
print(dic["phone"])
print(dic["birth"])

#Keys
a={"name":"pey","phone":"010-9999-1234","birth":"1118"}
print(a.keys())

for k in a.keys():
    print(k)

#Value list
print(a.values())

#clear
a.clear()
print(a)

a={"name":"pey", "phone":"010-9999-1234", "birth":"1118"}
print("name" in a)
print("email" in a)
