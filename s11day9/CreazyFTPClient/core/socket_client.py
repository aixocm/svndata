#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import socket
import json
import time
class FTPClient(object):
    response_code = {
            '200': "User passed authentication!",
            '201': "Invalid username or password!",
            '202': "User expired",
            '300': "File ready to send",
            '301': "File ready to recv"
        }
    def __init__(self,argv):
        self.args = argv
        print self.args
        self.parse_argv()

        self.handle()
    def handle(self):
        self.connect(self.ftp_host,self.ftp_port)
        if self.auth():
            self.interactive()

    def interactive(self):
        quit_flag=False
        while not quit_flag:
            user_input = raw_input("[\033[32;1m%s\033[0m][%s]:"%(self.user,self.cwd)).strip()
            if len(user_input) == 0:continue
            self.cmd_parser(user_input)
    def cmd_parser(self,user_input):
        cmd_list=user_input.split()
        if hasattr(self,"cmd__"+cmd_list[0]):
            func = getattr(self,"cmd__"+cmd_list[0])
            func(cmd_list)
        else:
            print "\033[31;1m Invalied cmd\033[0m"
    def cmd__get(self,cmd_list):
        if len(cmd_list)<2:
             print "\033[31;1m remote filename is specified  cmd\033[0m"
        else:
            remote_filename = cmd_list[1]
            msg_str = {"action":"cmd__get",
                       "filename":remote_filename,
                       }
            self.sock.send(json.dumps(msg_str))
            server_response = json.loads(self.sock.recv(1024))
            if  server_response.get("status") == "300":
                total_file_size = int(server_response["data"][0].get("size"))
                client_response = {"action":"get",
                                   "filename":remote_filename,
                                   "status":"301"
                                   }
                self.sock.send(json.dumps(client_response))
                received_size=0
                local_filename = os.path.basename(remote_filename)
                f=open(local_filename,"wb")
                last_process = 0
                while total_file_size != received_size:
                    data = self.sock.recv(4096)
                    received_size+=len(data)
                    # print total_file_size,received_size
                    f.write(data)
                    progress_num = received_size * 100 / total_file_size
                    new_progress = progress_num - last_process
                    sys.stdout.write("\r#"*new_progress+"[%s%%]"%progress_num)
                    sys.stdout.flush()
                    last_process = progress_num
                    time.sleep(0.5)
                else:
                    print "\033[32;1m file download successful"
                    f.close()

    def auth(self):
        retry_count=0
        while retry_count <3:
            username=raw_input("Username:").strip()
            if len(username)==0:
                continue
            password=raw_input("Password:").strip()
            if len(password)==0:
                continue
            data=json.dumps({"username":username,"password":password,"action":"user_auth"})
            cmd_str='%s'%(data)
            self.sock.send(cmd_str)
            server_response = json.loads(self.sock.recv(1024))
            if server_response['status']=="200":
                print self.response_code["200"]
                self.user = username
                self.cwd = '/'
                return  True
            else:
                print self.response_code[server_response["status"]]
                retry_count+=1
        else:
            sys.exit("\033[1;31m To many acctemps \033[0m")



    def parse_argv(self):
        if len(self.args)<5:
            self.help_msg()
        else:
            mandatory_fields = ["-s","-p"]
            for i in mandatory_fields:
                if i not in sys.argv:
                    sys.exit("The argument [%s] is mandatory" %i)
            try:
                self.ftp_host = self.args[self.args.index("-s")+1]
                self.ftp_port = int(self.args[self.args.index("-p")+1])
            except (IndexError,ValueError) as e:
                print "\033[1;31m%s\033[0m" %e
                self.help_msg()

            print self.ftp_host,self.ftp_port

    def  connect(self,host,port):
        try:
            self.sock=socket.socket()
            self.sock.connect((host,port))
            self.sock.settimeout(5)
            print 'sdasda'
        except socket.error as e:
            sys.exit(e)



    def  help_msg(self):
        help_msg = '''
         -s     ftp_server_addr     :the ftp server you want to connect,mandatory
         -p     ftp port            :the ftp server you want to connect,mandatory
         '''
        sys.exit(help_msg)

