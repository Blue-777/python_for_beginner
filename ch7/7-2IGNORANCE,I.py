#re.IGNORECASE 또는 re.I 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션이다.
import re

p = re.compile('[a-z]+', re.I)
p.match('python')
p.match('Python')
p.match('PYTHON')


