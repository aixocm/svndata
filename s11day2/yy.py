#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""import socket
obj = socket.socket()
obj.connect(('localhost',8342))
print obj.getpeername()
obj.send('thanks!,LKLKLKL')
server_data=obj.recv(1024)
print server_data
obj.close()
"""
import socket
ip_port=('127.0.0.1',8009)
sk=socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    inp=raw_input('please input:')
    sk.sendall(inp)
    res_size = sk.recv(1024)
    sk.send('OK')
    total_size=int(res_size)
    recive_size=0
    while True:
        data = sk.recv(1024)
        recive_size+=len(data)
        if  total_size==recive_size:
            print data
            break
        print data
    if inp == 'exit':
        break
sk.close()
