money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
         print("택시를 타고가라")
    else:
         print("걸어가라")
         

# if 문을 한 줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass 
else: print("카드를 꺼내라")

# 조건부 표현식 
message = "success" if score >= 60 else "failure"
