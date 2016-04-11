#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import socket_server
from conf import settings
class ArgvHandler(object):
    def __init__(self,args):
        self.args=args
        print self.args
        self.argv_parser()
    def argv_parser(self):
        if len(self.args)==1:
            self.help_msg()
        else:
            if hasattr(self,self.args[1]):
                func = getattr(self,self.args[1])
                func()
            else:
                self.help_msg()
    def start(self):
        server=socket_server.SocketServer.ThreadingTCPServer((settings.BIND_HOST,settings.BIND_PORT),socket_server.FtpServer)
        server.serve_forever()
    def stop(self):
        pass

    def help_msg(self):
        msg = '''
        start               :start ftp server
        stop                :stop ftp server
        create_account      :create ftp user account
        help                :print help msg
            '''
        sys.exit(msg)
