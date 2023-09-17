a = "Life is too short"
b = a.encode('utf-8')
print(b)
print(type(b))

a = '한글'
b = a.encode('utf-8')
print(b)
print(type(b))

b = a.encode('euc-kr')
print(b)
print(type(b))

c = b.decode('euc-kr')
print(c)

with open('euc_kr.txt', encoding='euc-kr') as f:
    data = f.read()  # 유니코드 문자열

# 2. unicode 문자열로 프로그램 수행하기
data = data + "\n" + "추가 문자열"

# 3. euc-kr로 수정된 문자열 저장하기
with open('euc_kr.txt', encoding='euc-kr', mode='w') as f:
    f.write(data)