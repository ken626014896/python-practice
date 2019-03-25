# coding=utf-8
import re
pattern = re.compile(r'''\(((?<mm>\()|(?<-mm>\))|.)*?(?(mm)(?!))\)''')
str = 'e+f(-(g/(h-i))*j'
print(pattern.search(str))