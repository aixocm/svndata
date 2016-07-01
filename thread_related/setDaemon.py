#_*_coding:utf-8_*_
__author__ = 'jieli'
import time
import threading

def run(num):
    if not num == 5:
        time.sleep(1)
    print 'Hi, I am thread %s..lalala\n' % num

def main(n):
    print "----running main thread-----"
    for i in range(n):#10
        t = threading.Thread(target=run,args=(i,))
        t.start()
    time.sleep(3)
    print "-----done main thread -------"

main_thread = threading.Thread(target=main,args=(10,))
main_thread.setDaemon(True)
main_thread.start()
print '\n----->>>>'
main_thread.join()