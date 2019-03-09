class Test(object):
     cls_val = 1
     bb=0
     def __init__(self):
         self.ins_val = 10

a=Test()

print(Test.__dict__)
print(a.__dict__)
# print(dir(Test))
# print('====')
# print(dir(a))
#实例t的属性并不包含cls_val，cls_val是属于类Test的。
c=Test()
d=Test()
Test.bb=Test.bb+1
c.bb=c.bb+1
print(c.bb)
print(d.bb)
print(c.__dict__)
print(d.__dict__)