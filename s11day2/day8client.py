#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import os
import json
import sys
import time
import hashlib
ip_port=('127.0.0.1',8411)
sk=socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

def file_list():
    os.chdir('C:\Users\Administrator\PycharmProjects\s11day2\\backend\client')
    global x
    x=os.listdir('.')
    print "你能上传的文件有:"
    for file in x:
        print file+',',
    print

def transfer(file_name):
    a=os.popen('dir')
    a=list(a)[7:-2]
    for name in a:
        if '<DIR>' in name:
            if file_name == name.strip().split(' ')[-1].decode('gbk'):
                file_name =  name.strip().split(' ')[-1].decode('gbk')
                walk_dir_transfer(file_name)
        elif file_name == name.strip().split(' ')[-1].decode('gbk'):
            file_dir_transfer(file_name)
        else:
            continue

def  walk_dir_transfer(file_name):
    sk.sendall('dir')
    sk.recv(1024)
    sk.sendall(file_name)
    zhuangtai=sk.recv(1024)
    if zhuangtai:
        print zhuangtai
        os.chdir(file_name)
        name_list=os.popen('dir')
        name_list=list(name_list)[7:-2]
        for   file_name  in name_list:
            if '<DIR>' in file_name:
                file_name =  file_name.strip().split(' ')[-1].decode('gbk')
                walk_dir_transfer(file_name)
            file_name =  file_name.strip().split(' ')[-1].decode('gbk')
            file_dir_transfer(file_name)
    else:
        print "服务器异常"

    # result=os.listdir('.')
    # print os.getcwd()

def file_dir_transfer(file_name):
    sk.sendall('file')
    sk.recv(1024)
    sk.sendall(file_name)
    response=sk.recv(1024)
    if response:
        print response
        print '服务器正在接受文件:',file_name
        # with open(file_name,'rb') as f:
        file_size = os.path.getsize(file_name)
        sk.sendall(str(file_size))
        zhuangtai = sk.recv(1024)
        if zhuangtai:
            print zhuangtai
            f=open(file_name,'rb')
            send_size = 0
            file_md5 = hashlib.md5()
            while file_size != send_size:
                data=f.read(4096)
                sk.send(data)
                send_size+=len(data)
                file_md5.update(date)
            else:
                f.close()
                file_md5_str = file_md5.hexdigest()
                result=sk.recv(1024)
                sk.send('ok')
                if result == 'finish':
                    print file_name,'上传完成!'
                    file_reciv_md5 = sk.recv(1024)
                    if  file_reciv_md5 == file_md5_str:
                        print "YES,file is perfect"
                    else:
                        print "file is no perfect"
                else:
                    print "文件上传异常"
        else:
            print "服务器异常"
    else:
        print "服务器异常"

def  ls_dir_cmd(*cmd_str):
    if cmd_str[0] == 'ls':
        print cmd_str
        ls_dir = 'ls'+cmd_str[1]
        sk.send(ls_dir)
        ls_list_len = int(sk.recv(1024))
        if ls_list_len == 0:
            print "no dir"
        elif ls_list_len == 1:
            print cmd_str[1]
        else:
            sk.send('OK')
            ls_list = json.loads(sk.recv(ls_list_len))
            for i in ls_list:
                print i,
            print


def ls_cmd(*cmd_str):
    if cmd_str[0] == 'ls':
        sk.send(cmd_str[0])
        ls_list_len = int(sk.recv(1024))
        sk.send('OK')
        ls_list = json.loads(sk.recv(ls_list_len))
        for i in ls_list:
            print i,
        print
    else:
        print "cmd_str is error"

def put_cmd(*cmd_str):
    # print cmd_str[1]
    if cmd_str[1] in x:
        file_name = cmd_str[1]
        sk.send('put')
        OK  = sk.recv(1024)
        if OK == 'ok':
            transfer(file_name)
        else:
            print "server does not get the cmd "
    else:
        print "have no this file"


def get_cmd(*cmd_str):
    sk.sendall('get'+cmd_str[1])
    file_dir=sk.recv(1024)

    if file_dir == 'dir':
        sk.sendall('OK')
        os.mkdir(cmd_str[1])
        file_num  = int(sk.recv(1024))
        sk.send('file_num_ok')
        for i in range(file_num):
            file_name = sk.recv(1024)
            # print file_name
            sk.sendall('file_name_OK')
            file_size = int(sk.recv(1024))
            f=open(cmd_str[1]+"/"+file_name,'wb')

            sk.sendall('file_size_OK')
            recv_size =  0
            # last_process_num = 0
            file_md5 = hashlib.md5()
            while  file_size != recv_size:
                data = sk.recv(4096)
                file_md5.update(data)
                f.write(data)
                recv_size+=len(data)
                process_num = recv_size*100/file_size
                # new_process_num = process_num - last_process_num
                # last_process_num = process_num
                sys.stdout.write("\r\033[31;31m[%s%%]\033[0m"%process_num+"\033[31;31m#\033[0m"*process_num)
                sys.stdout.flush()
                # time.sleep(0.2)

            else:
                sk.send('1024')
                print  "dir:",file_name,"have download"
                file_str_md5 = file_md5.hexdigest()
                f.close()
                file_recive_md5 = sk.recv(1024)
                if file_recive_md5 == file_str_md5:
                    print "YES,file is perfect"
                else:
                    print "the file  is imperfect"
    elif file_dir == 'file':
        sk.send('OK')
        f=open(cmd_str[1],'wb')
        file_size = int(sk.recv(1024))
        sk.send('file_size_OK')
        recv_size = 0
        # last_process_num = 0
        file_md5 = hashlib.md5()
        while file_size != recv_size:
            data = sk.recv(4096)
            file_md5.update(data)
            recv_size+=len(data)
            f.write(data)
            process_num = recv_size*100/file_size
            # new_process_num = process_num - last_process_num
            # last_process_num = process_num
            sys.stdout.write("\r\033[31;31m[%s%%]\033[0m"%process_num+'\033[31;31m#\033[0m'*process_num)
            sys.stdout.flush()
            time.sleep(0.05)

        else:
            print
            print "file:",cmd_str[1],"have download"
            file_str_md5 = file_md5.hexdigest()
            f.close()
            sk.send('ok')
            file_recive_md5 = sk.recv(1024)
            if file_recive_md5 == file_str_md5:
                print "YES,file is perfect"
            else:
                print "the file  is imperfect"
    else:
        print "the get have no dir or file"











def  auth(username,password):
    identified = {
        'username':username,
        'password':password
    }
    sk.send(json.dumps(identified))
    identiy_flag  = sk.recv(1024)
    if identiy_flag == 'True':
        print "authentication passed !"
        return True
    else:
        print "authentication failed!"
        return False




def cmd_func(cmd_str):
    cmd_str = cmd_str.strip().split()
    if len(cmd_str) == 1:
        ls_cmd(*cmd_str)

    elif len(cmd_str) == 2:
        ls_dir_cmd(*cmd_str)
        if cmd_str[0] == 'put':
            put_cmd(*cmd_str)

        if  cmd_str[0] == 'get':
            get_cmd(*cmd_str)

    else:
        print "your cmd is error"




def Main():
    username = raw_input("input your username:")
    password = raw_input("input your password:")
    if auth(username,password):
        file_list()
        while True:
            cmd_str = raw_input("退出服务按q \033[1;31m>>>\033[0m")
            if cmd_str == 'q':
                break
            if cmd_str == '':
                continue
            cmd_func(cmd_str)



if  __name__ == '__main__':
    Main()

