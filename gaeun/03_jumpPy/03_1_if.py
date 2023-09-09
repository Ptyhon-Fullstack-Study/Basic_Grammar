money= 2000
card= True
if money>=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


pocket=["paper","money","cellphon"]
if "money" in pocket:
    pass
else:
    print("카드를 꺼내라")

# elif
pocket=["paper","cellphon"]
card=True
if "money" in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
if "money" in pocket:pass
else:print("카드를 꺼내라")

