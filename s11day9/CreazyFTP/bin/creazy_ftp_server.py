#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print BASE_DIR
from modules import main
if __name__=='__main__':
    EntryPoint = main.ArgvHandler(sys.argv)
