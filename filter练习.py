

#筛选
def is_odd(n):
    return n % 2 == 1
a=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(a)

#使用匿名函数
b=list(filter(lambda n:n%2 ==1,[1, 2, 4, 5, 6, 9, 10, 15]))
print(b)