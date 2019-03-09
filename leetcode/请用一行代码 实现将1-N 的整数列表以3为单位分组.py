
# [ab for i in range(5)]
# ab不一定要是与i有关
#以下为例子
print([1 for i in range(5)])

print([[x for x in range(1, 100)][i:i + 3] for i in range(0,101, 3)])