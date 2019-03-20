class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):#需要传入当前类
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x): #不需要传入self 或当前类
        print("executing static_foo(%s)" % x)
a = A()

a.foo(6)
#普通方法要直接用类名调用对象  需要把实例对象传入方法中
A.foo(a,6)

print('======')  #不需要创建实例就可以调用方法

A.class_foo(6)
print('======')
A.static_foo(6)