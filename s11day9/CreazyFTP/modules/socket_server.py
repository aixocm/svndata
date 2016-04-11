#!/usr/bin/env python
# -*- coding:utf-8 -*-
import SocketServer
import json
import auth
import os
from conf import settings
class FtpServer(SocketServer.BaseRequestHandler):
    response_code = {
            '200': "User passed authentication!",
            '201': "Invalid username or password!",
            '202': "User expired",
            '300': "File ready to send",
            '301': "File ready to recv"
        }
    def handle(self):
        print self.client_address
        shutdown_flag = False
        while  not shutdown_flag:
            data = self.request.recv(1024)
            self.data_parser(data)
    def data_parser(self,data):
        data=json.loads(data)
        if data.get("action"):
            action_type = data.get("action")
            if hasattr(self,action_type):
                func=getattr(self,action_type)
                func(data)
            else:
                print ("invalied client data",data)
        else:
            print ("invalied client data",data)

    def cmd__get(self,data):
        print "-----client ask for downloading ----",data
        if hasattr(self,'login_user'):
            filename_path = data.get("filename")
            file_with_abs_path = "%s\%s" %(self.home_path,filename_path)
            if  os.path.isfile(file_with_abs_path):
                file_size = os.path.getsize(file_with_abs_path)
                response_data = {"status":"300",
                                 "data":[{
                                     "filename":filename_path,
                                     "size":file_size
                                 }]
                                 }
                self.request.send(json.dumps(response_data))
                client_response = json.loads(self.request.recv(1024))
                if client_response.get("status") == "301":
                    f = file(file_with_abs_path,'rb')
                    send_size = 0
                    while file_size != send_size:
                        data=f.read(4096)
                        self.request.send(data)
                        send_size+=len(data)
                        print file_size,send_size
                    else:
                        print "\033[32;1m send file done\033[0m"
                        f.close()
            else:
                print "file is not exist"
        else:
            print "user is not authorized"








    def user_auth(self,data):
        username = data.get("username")
        password = data.get("password")

        auth_status,auth_msg = auth.authentication(username,password)
        if auth_status is True:
            print "auth succesful",auth_msg
            response_data = {"status":"200","data":[]}
            self.login_user = username
            self.home_path = "%s\%s"%(settings.USER_BASE_HOME_PATH,username)
        else:
            print "auth failed....",auth_msg
            response_data = {"status":"201","data":[]}

        self.request.send(json.dumps(response_data))