#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid
import paramiko
class  Haproxy(object):
    def   __init__(self):
        self.host = '120.27.143.149'
        self.port = 22
        self.username = 'root'
        self.pwd = 'Aixocm123_jj_max'

    def   create_file(self):
        file_name = str(uuid.uuid4())
        with  open(file_name,'w') as  f:
            f.write('sb')
        return file_name

    def  run(self):
        self.connect()
        self.upload()
        self.rename()
        self.close()
    def   connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def   close(self):
        self.__transport.close()
    def  upload(self):
        file_name = self.create_file()
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(file_name,'/tmp/tttttttttttttttt.py')

    def rename(self):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        stdin,stdout,stderr = ssh.exec_command('mv /tmp/tttttttttttttttt.py  /tmp/nooooooooooooo.py')
        result = stdout.read()

ha = Haproxy()
ha.run()