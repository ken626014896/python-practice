class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')

obj = Foo() # 执行 __init__
obj()       # 执行 __call__

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print ('My name is %s...' % self.name)
        print ('My friend is %s...' % friend)

        
    def __str__(self):
        return 'i am aaa'

p = Person('Bob', 'male')

p('Tim')
print(p)