#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port= ('127.0.0.1',8000)
sk=socket.socket()
sk.connect(ip_port)
sk.setblocking(False)
sk.settimeout(5)

while True:
    inp = raw_input("please input:")
    sk.sendall(inp)
    data=sk.recv(1024)
    print data
    if inp == 'exit':
        break
sk.close()

