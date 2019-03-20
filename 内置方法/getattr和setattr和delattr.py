class Student:
    def __getattr__(self, item):
        print('访问一个不存在的属性时候触发')
        print(item)
        return '不存在'

    def __setattr__(self, key, value):
        print('设置一个属性值的时候触发')
        # self.key = value  # 这样会无限循环
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('删除一个属性的时候触发')
        if self.__dict__.get(item, None):
            del self.__dict__[item]

stu = Student()
print('================')
stu.name = 'zlw'  # 设置一个属性值的时候触发
print('================')
print(stu.name)
print('================')
print(stu.noexit)  # 访问一个不存在的属性时候触发 , 返回'不存在'
print('================')
del stu.name  # 删除一个属性的时候触发