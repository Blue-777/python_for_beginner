#for와 range를 이용한 구구단(multiplication table)
'''for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end = ' ' )
    print('')'''
    
#or 
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)
