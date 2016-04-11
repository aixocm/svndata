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
    data = sk.recv(1024)
    print 'receive:',data
    inp=raw_input('please input:')
    sk.sendall(inp)
    if inp == 'exit':
        break
sk.close()
