import re

s = 'firstlinesecondline third line'


p1 = r"line"
a=re.match(p1, s)
print (a.group(0))#打印出来


b=re.search(p1, s)
print (b.group(0))#打印出来
# output> ['first']