from functools import reduce

a=[1,2,3]

def xx (x1, x2):
    return x1+x2


b=reduce(xx,a)

print(b)

#变成整数
def fn(x1,x2):
    return x1*10+x2


a = [4, 3, 9, 6]

print(reduce(fn,a))


#使用匿名函数
print(reduce(lambda x1, x2: x1*10+x2, a))


#二进制转十进制

a=1010
a=str(a)
sum=0
j=0

for i  in a[::-1]:
    sum=sum+int(i)*pow(2,j)
    j=j+1
print(sum)
