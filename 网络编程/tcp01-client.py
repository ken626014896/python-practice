import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))

for data  in  [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)

    print(s.recv(1024).decode('utf-8'))

a=input('退出输入 exit')
s.send(b'exit')
s.close()