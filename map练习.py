
from  functools  import  reduce
def  xx(x):
  return x*x

a=[1,2,3]

b=map(xx,a)


for i in b:
    print(i)



if '__iter__' in dir(b):
    print('yes')

if '__next__' in dir(b):
    print('yes')
print(getattr(b,'__iter__'))
print(hash(b))
print(id(b))


print(dir(b))

#化str为int,当然可以直接使用int()函数

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
def fn(x, y):
    return x * 10 + y
sum=reduce(fn, map(char2num, '13579'))
print(sum)

