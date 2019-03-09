from enum import Enum


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name in Month:
#     print(name.value)


print(Month.Feb.value)

for  i  in enumerate(['a','b']):
    print(i)