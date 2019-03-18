# encoding: UTF-8
import threading
import time

event = threading.Event()


def func():
    # 等待事件，进入等待阻塞状态
    print ('%s wait for event...' % threading.currentThread().getName())
    event.wait()

    # 收到事件后进入运行状态
    print ('%s recv event.' % threading.currentThread().getName())

for i  in  range(10):
    t1 = threading.Thread(target=func)

    t1.start()





# 发送事件通知
print ('MainThread set event.')
event.set()

#event无法进入同步阻塞状态 接受信息时没有顺序
