#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
import threading

def run(n):
    while True:
        print '[%s]------running----\n' % n
        time.sleep(2)


def main():

    for i in range(5):
        t = threading.Thread(target=run,args=[i,])
        t.start()
        print('starting thread', t.getName())


m = threading.Thread(target=main,args=[])
m.setDaemon(True)
m.start()
print("---main thread done----")