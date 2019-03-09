

d= {'a':24,'g':52,'i':12,'k':33}
a=sorted(d.items(),key=lambda x:x[1])
print(a)


#对key排序
b=sorted(d.items(),key=lambda x:x[0])
print(b)