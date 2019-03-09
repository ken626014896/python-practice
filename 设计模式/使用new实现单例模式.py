class Rectangle:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)  # super()方法是调用其父类，即object

            return cls._instance
        else:

            return cls._instance

    def __init__(self, Length, Width):
        self.Length = Length
        self.Width = Width
        print(self.Width)

    def A(self):
        print(self.Length)


a = Rectangle(4, 6)
b = Rectangle(5, 7)
print(a, b)

# 上述代码可以发现，在第一次实例化时，我们会用一个私有属性_instance去
# 接收父类new方法开辟的内存，并返回。当我们第二次实例化时，
# 由于私有属性_instance存在,故直接返回它。
# 可以发现的是，两次实例化中，new方法所返回的内存空间是同一个，
# 故最后得到的实例化当然就是一样的内存地址了，
# b的初始化带来的属性会覆盖掉a的属性。
