#!/usr/bin/env python
# -*- coding:utf-8 -*-
import SocketServer
import os
import json
import hashlib
BASE_DIR = 'C:\Users\Administrator\PycharmProjects\s11day2\\backend\server'
os.chdir(BASE_DIR)

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        if self.auth():
            print 'get connection from:',self.client_address
            self.cmd_func()
        else:
            print " user authentication failed!"
    def auth(self):
        auth_data = json.loads(self.request.recv(1024))
        if auth_data['username'] == '' and auth_data['password'] == '':
            self.request.send('True')
            return True
        else:
            self.request.send('False')
            return False

    def cmd_func(self):
        while True:
            cmd_str = self.request.recv(1024)
            if not cmd_str:
                break
            if  cmd_str.startswith('ls'):
                # print cmd_str
                if len(cmd_str) > 2:
                    cmd_str = cmd_str[2:]
                    self.ls_file_dir_cmd(cmd_str)
                else:
                    self.ls_cmd(cmd_str)

            elif cmd_str.startswith('get'):
                if len(cmd_str) >3:
                    cmd_str = cmd_str[3:]
                    self.get_cmd(cmd_str)


            elif cmd_str.startswith('put'):
                # print cmd_str
                self.request.send('ok')
                self.put_cmd()

            else:
                print "have no this function"

    def put_cmd(self):
        shutdown_flag = False
        while not shutdown_flag:
            file_dir = self.request.recv(1024)
            if not file_dir:
                os.chdir(BASE_DIR)
                break
            self.request.sendall('OK')
            if file_dir == 'dir':
                file_name=self.request.recv(1024)
                self.request.sendall('文件夹传输已建立，请等待....')
                # file_name=file_name[:-3]
                print "文件夹:",file_name
                os.mkdir(file_name)
                os.chdir(file_name)
                continue
            if file_dir == 'file':
                file_name=self.request.recv(1024)
                if file_name:
                    self.request.sendall('文件传输已建立，请等待....')
                    total_size=int(self.request.recv(1024))
                    self.request.sendall('OK,正在上传')
                    recive_size=0
                    f=open(file_name,'wb')
                    file_md5 = hashlib.md5()
                    while recive_size != total_size:
                        data=self.request.recv(4096)
                        f.write(data)
                        f.flush()
                        recive_size+=len(data)
                        file_md5.update(data)
                    else:
                        f.close()
                        file_md5_str = file_md5.hexdigest()
                        self.request.sendall('finish')
                        self.request.recv()
                        print "got the file:",file_name
                        self.request.send(file_md5_str)
                else:
                    print "文件异常"


    def get_cmd(self,cmd_str):
        if  os.path.isdir(cmd_str):
            self.request.send('dir')
            kaishi = self.request.recv(1024)
            if kaishi:
                file_list = os.listdir(cmd_str)
                list_len = len(file_list)
                self.request.send(str(list_len))
                self.request.recv(1024)
                for file in file_list:
                    # print file,
                    self.request.send(file)
                    self.request.recv(1024)
                    f_size = os.path.getsize(cmd_str+'/'+file)
                    self.request.send(str(f_size))
                    self.request.recv(1024)
                    f=open(cmd_str+'/'+file,'rb')
                    send_size = 0
                    file_md5 = hashlib.md5()
                    while send_size != f_size:
                        data = f.read(4096)
                        self.request.send(data)
                        send_size+=len(data)
                        file_md5.update(data)
                    else:
                        f.close()
                        self.request.recv(1024)
                        file_md5_str = file_md5.hexdigest()
                        self.request.send(file_md5_str)
            else:
                print "error"
        elif os.path.isfile(cmd_str):
            self.request.send('file')
            kaishi = self.request.recv(1024)
            if kaishi:
                f_size = os.path.getsize(cmd_str)
                self.request.send(str(f_size))
                self.request.recv(1024)
                f=open(cmd_str,'rb')
                send_size = 0
                file_md5 = hashlib.md5()
                while send_size != f_size:
                    data = f.read(4096)
                    self.request.send(data)
                    send_size+=len(data)
                    file_md5.update(data)
                else:
                    f.close()
                    self.request.recv(1024)
                    file_md5_str = file_md5.hexdigest()
                    self.request.send(file_md5_str)

        else:
            print "have no this file  or dir"









    def ls_cmd(self,cmd_str):
        x = os.listdir('.')
        len_dir = len(json.dumps(x))
        self.request.send(str(len_dir))
        self.request.recv(1024)
        self.request.send(json.dumps(x))



    def ls_file_dir_cmd(self,cmd_str):
        x = os.listdir('.')
        if cmd_str in x:
            if os.path.isdir(cmd_str):
                send_dir = os.listdir(cmd_str)
                len_dir = len(json.dumps(send_dir))
                self.request.send(str(len_dir))
                self.request.recv(1024)
                self.request.send(json.dumps(send_dir))
            elif os.path.isfile(cmd_str):
                self.request.send('1')


        else:
            self.request.send('0')






if  __name__ == '__main__':
    server=SocketServer.ThreadingTCPServer(('127.0.0.1',8411),MyServer)
    server.serve_forever()


