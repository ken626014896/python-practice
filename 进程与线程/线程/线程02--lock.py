import time, threading

# 假定这是你的银行存款:
balance = 0
lock=threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

if __name__=='__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    # print(threading.enumerate())
    # print(t1.isDaemon())
    # print(t2.isDaemon())
    # print(threading.enumerate())

    print(balance)