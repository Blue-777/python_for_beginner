def boolean(op):
    return op(False, True)


alice = False 
 # a => false  b => true 
print(boolean(lambda a, b: 'xxxxx' if b else 'alice is false' ))

