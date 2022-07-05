#regular_expression 정규 표현식
#re.compile 모듈 단위로 수행하기

import re
'''p = re.compile('[a-z]+')
m = p.match("python")'''
m = re.match('[a-z]+', "python")
print(m)