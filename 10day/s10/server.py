#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import select
import Queue
message={}
ip_port= ('127.0.0.1',8898)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
sk.setblocking(False)
inputs = [sk,]
output = []
while True:
    rList,wList,e = select.select(inputs,output,inputs,1)
    import time
    print inputs
    time.sleep(2)
    for r in rList:
        if r  == sk:
            conn,address = r.accept()
            inputs.append(conn)
            message[conn] = Queue.Queue()
        else:
            client_data = r.recv(1024)
            if client_data:
                output.append(r)
                message[r].put(client_data)

            else:
                inputs.remove(r)
    for w in wList:
        try:
            data = message[w].get_nowait()
            w.sendall(data)
        except Queue.Empty:
            pass
        output.remove(w)
        del message[w]

