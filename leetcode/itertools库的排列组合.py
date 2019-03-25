import itertools

a=[1,2,3,4,5,6]
b=[]
for i in itertools.combinations_with_replacement(a, 7):
    b.append(i)
print(b)