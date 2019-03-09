def doc(func):
    def addsome(*args,**kwargs):
        print('节日快乐')
        a=func(*args,**kwargs)
        print("可以滚了")
        return a
    return  addsome


@doc
def say(a):
    print('欢迎进入')
    return  a

# print(say('欢迎使用'))

def doc2(func):
    def addsome(*args,**kwargs):
        print('节日快乐')
        func()
        print("可以滚了")

    return  addsome


@doc2
def say2():
    print('欢迎进入')


say2()