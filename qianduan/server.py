#!/usr/bin/env python
# -*- coding:utf-8 -*-
import    socket

def   handle(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("<h1 style='color:red;'>12345</h1>")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8004))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle(connection)
        connection.close()

if  __name__ == '__main__':
    main()
