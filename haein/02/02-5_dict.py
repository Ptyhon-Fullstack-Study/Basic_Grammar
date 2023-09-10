dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {[1,2] : 'hi'} # TypeError: unhashable type: 'list'


a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a.keys()

# dict_keys, dict_values, dict_items 객체는 리스트로 변환하지 않더라도 
# 기본적인 반복 구문(예: for 문)에서 사용할 수 있다.

for k in a.keys():
    print(k)
    
a.values() # value 의 리스트
a.items()  # key value 의 쌍 

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
'name' in a # True 


