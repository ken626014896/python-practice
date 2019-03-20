#把下面字符串 按照字母表推进两位

a='abcxyz'
b=[]
for i in a:
    print(ord(i))

    a_in_num=ord(i)+2

    if a_in_num>122:
        a_in_num=97+(a_in_num-122)-1

    b.append(chr(a_in_num))

print(''.join(b))