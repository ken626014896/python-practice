import threading


lock = threading.RLock()

def f():
  with lock:
    g()
    h()

def g():
  with lock:
    h()
    do_something1()

def h():
  with lock:
    do_something2()

def do_something1():
    print('do_something1')

def do_something2():
    print('do_something2')


# Create and run threads as follows
try:
    threading.Thread( target=f ).start()
    threading.Thread( target=f ).start()
    threading.Thread( target=f ).start()
except Exception as e:
    print("Error: unable to start thread")

#
# 每个thread都运行f()，f()获取锁后，运行g()，但g()中也需要获取同一个锁。如果用Lock，
# 这里多次获取锁，就发生了死锁。
# 但我们代码中使用了RLock。在同一线程内，对RLock进行多次acquire()操作，程序不会堵塞，