#if와 else만 사용
'''pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
else: 
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")'''
        
#elif
'''pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")'''
    
#simplify if statement
'''if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")'''
    
#simplify more
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")