from mysingleton import singleton
a=singleton
b=singleton

print(id(a))
print(id(b))
print(a is b)