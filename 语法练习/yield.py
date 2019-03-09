
a=[1,2,3,4,5]
#yield把函数变成了一个生成器
def b():
    for i in a:
        yield i

c=b()
for i  in c:
    print(i)