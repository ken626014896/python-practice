
# -*- coding:utf-8 -*-
import socketserver
import threading

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.'.encode('utf-8'))
        Flag = True
        while Flag:

            data = conn.recv(1024)
            print(threading.currentThread())
            data = data.decode('utf-8')
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall('通过可能会被录音.balabala一大推'.encode('utf-8'))
            else:
                conn.sendall('请重新输入.'.encode('utf-8'))


if __name__ == '__main__':
    # server = SocketServer.ForkingTCPServer(('127.0.0.1', 8009), MyRequestHandler)
    #ForkingTCPServer为每一个客户端建立进程  ThreadingTCPServer为每一个客户端建立线程
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), MyServer)
    server.serve_forever()

    # 创建一个继承自SocketServer.BaseRequestHandler的类
    # 类中必须定义一个名称为handle的方法
    # 启动ThreadingTCPServer