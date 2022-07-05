#regular_expression 정규 표현식
#match
import re
'''p = re.compile('[a-z]+')

m = p.match("3 python")
print(m)'''

p = re.compile('[a-z]+')
m = p.match( 'string goes here' )

if m:
    print('Match found: ', m.group())
else:
    print('No match')