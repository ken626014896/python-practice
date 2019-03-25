class SingleClass(object):


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_ins'):
            cls._ins=super(SingleClass,cls).__new__(cls)

        return  cls._ins

class TestClass(SingleClass):

    def __init__(self,name):

        print(name)


a=TestClass('ken')
b=TestClass('sam')

print(a is b)