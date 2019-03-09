class Student:
    a=0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.__class__}, name={self.name}, age={self.age}'

    __repr__ = __str__


stu = Student('zlw', 26)
print(stu)  # <class '__main__.Student'>, zlw, 26
print(stu.__repr__())

print(dir(Student))
