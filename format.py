a="{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序
print(a)

a="{0} {1}".format("hello", "world")  # 设置指定位置
print(a)

a="{1} {0} {1}".format("hello", "world")  # 设置指定位置
print(a)


print("{:.2f}".format(3.1415926));
print(round(3.1454,2))