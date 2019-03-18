def averager():
    total = 0.0
    count = 0
    avg = None

    while True:
        num = yield avg
        total += num
        count += 1
        avg = total/count

# run
ag = averager()
# 预激协程
print(next(ag))     # None

print(ag.send(10))  # 10
print(ag.send(20))  # 15
