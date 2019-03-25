
import re

pattern=re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])\w{6,12}$')

res=pattern.search('zxc12A3ken1')
print(res.group())