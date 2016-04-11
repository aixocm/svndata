#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  smtplib
from email.mime.text import  MIMEText
from email.utils import formataddr
def email():
    msg=MIMEText('Hello,马哥! I am JJ','plain','utf-8')
    msg['From'] = formataddr(["JJ",'aixocm@126.com'])
    msg['To'] = formataddr(["马哥",'79585379@qq.com'])
    msg['Subject']="JJ"
    server = smtplib.SMTP('smtp.126.com',25)
    server.login("aixocm@126.com",'pnsuqtpgacrhxzzw')
    server.sendmail("aixocm@126.com",["79585379@qq.com",],msg.as_string())
    server.quit()
email()
