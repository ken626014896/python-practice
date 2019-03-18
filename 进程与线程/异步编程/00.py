
def test_a(b):
    while True:
       b=b+10;
       a=yield b
       print(a)


my_a=test_a(6)

print(next(my_a))
print(my_a.send(7))

#b被输出两次 不同值