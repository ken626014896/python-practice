class People:
    a = 200

class Student(People):
    a = 100

    def __init__(self, a):
        self.a = a

    def __getattr__(self, item):
        print('没有找到:', item)

    def __getattribute__(self, item):#优先度比getattr高
        print('属性访问截断器')
        if item == 'a':
            return 1
        return super().__getattribute__(item)

stu = Student(1)
print(stu.a)  # 1