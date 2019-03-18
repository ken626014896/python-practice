import inspect

def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> recived', a, b)

    c = yield a + b
    print('-> recived', a, b, c)

    yield

# run 
sc = simple_coroutine(5)

print('产出的%s'%next(sc))  #停在第6行

print('产出的%s'%sc.send(6)) # 5, 6   #停在第9行
print('产出的%s'%sc.send(7)) # 5, 6, 7    #停在第12行

sc.close()