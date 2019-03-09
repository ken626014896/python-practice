a=1
print(id(a))

a=2

print(id(a))
print('a is changed')

b=['1','2']
print(id(b))
b[1]="3"
print(id(b))

print('b is not changed')