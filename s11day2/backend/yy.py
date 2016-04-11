#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""import socket
obj_server = socket.socket()
obj_server.bind(('localhost',8342))
obj_server.listen(5)
while True:
    conn,addr = obj_server.accept()
    client_data = conn.recv(1024)
    print client_data
    conn.send('hao')
    conn.sendall('hsdiasduaosidosdjf')
    conn.close()
"""
"""
import socket
ip_port=('127.0.0.1',7777)
sk=socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    conn,address = sk.accept()
    conn.sendall("欢饮致电10086，请输入1xxx，0转人工服务")
    flag=True
    while flag:
        data=conn.recv(1024)
        if data == 'exit':
            flag=False
        elif data == '0':
            conn.sendall('通过可能会被录音,balabala,大堆')
        else:
            conn.sendall("请重新输入:")
    conn.close()
"""
import os
import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'get connection from:',self.client_address
        while True:
            data=self.request.recv(1024)
            print "Recv from cmd:",data
            cmd_res=os.popen(data).read()
            self.request.send(str(len(cmd_res)))
            self.request.recv(1024)
            self.request.sendall(cmd_res)

if __name__=='__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()
