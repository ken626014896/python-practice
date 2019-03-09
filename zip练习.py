

#矩阵相加减、点乘（也可以用for循环+列表推导式实现）
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]

aa=[x*y for a, b in zip(m, n) for x, y in zip(a, b)]

bb=[x+y for a, b in zip(m, n) for x, y in zip(a, b)]

a=[1,3,5]
b=[2,4,6]
c=zip(a,b)

print(list(c))

#二维矩阵变换(矩阵的行列互换)
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2=[]
a1=[b[i] for i in range(3) for b in m]



for i in range(3):
    m3 = []
    for b  in m:

        m3.append(b[i])
    m2.append(m3)
print(m2)
print([[j[i] for j in m] for i in range(len(m[0])) ])