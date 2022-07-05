#re.MULTILINE 또는 re.M 옵션은 메타 문자인 ^, $와 연관된 옵션이다.

import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) #왜 python one이 출력됨??