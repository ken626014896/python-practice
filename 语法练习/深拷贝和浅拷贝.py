import copy
a=[1,2,{'1':2}]
b=copy.copy(a)
c=copy.deepcopy(a)
a[2]['1']=3
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))