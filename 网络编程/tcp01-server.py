import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听接口
s.bind(('127.0.0.1',9999))

s.listen(6)
print('i am waiting for connection')



def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break

        sock.send(b'i am accept your message : %s'% data.decode('utf-8').encode('utf-8'))
    sock.close()

    print('Connection from %s:%s closed.' % addr)

while True:

    # 会等待并返回一个客户端的连接
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

