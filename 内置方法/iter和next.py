#实现可迭代对象

class Foo(object):

    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)

obj = Foo([11,22,33,44])

for i in obj:
    print(i)

#实现迭代器
class Num:
    def __init__(self, max_num):
        self.max_num = max_num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_num:
            self.count += 1
            return self.count
        else:
            raise StopIteration('已经到达临界')

num=Num(10)

for i in  num:
    print(i)