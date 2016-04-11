#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIND_HOST='localhost'
BIND_PORT = 9999
ACCOUNT_DB = {
    'engine':'file',
    'name':'%s/conf/accounts.json' %BASE_DIR
}
USER_BASE_HOME_PATH = "%s\\var" %BASE_DIR