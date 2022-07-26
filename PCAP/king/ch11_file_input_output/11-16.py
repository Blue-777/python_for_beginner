num1 = input('num1 -->')
num2 = input('num2 -->')

try:
    num1 = int(num1)
    num2 = int(num2)
    
except:
    print('An error has occurred.')
    
else:
    print(num1, '/', num2, '=', num1/num2)

finally:
    print('This part must be print.')