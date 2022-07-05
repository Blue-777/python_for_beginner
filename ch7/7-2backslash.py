#regular_expression 정규 표현식
#\ 문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용하여 이스케이프 처리를 해야 한다.
import re

p = re.compile('\\section')
p = re.compile('\\\\section')