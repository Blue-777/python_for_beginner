num1 = input('num1 -->')
num2 = input('num2 -->')

try:
    num1 = int(num1)
    num2 = int(num2)
    while True:
        res = num1/num2
except ValueError:
    print('can\'t transfer str to int.')
    
except ZeroDivisionError:
    print('can\'t devided by zero.')
    
except KeyboardInterrupt:
    print('You pressed Ctrl + C.')