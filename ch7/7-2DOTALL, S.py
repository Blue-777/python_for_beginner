#이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
import re
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
