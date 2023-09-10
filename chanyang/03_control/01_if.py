pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어가라')

if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

if 'money' in pocket: pass
else: print('카드를 꺼내라')

# conditional expression

score = 60
message = 'success' if score >= 60 else 'failure'
print(message)