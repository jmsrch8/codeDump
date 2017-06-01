#!/bin/python3
#   netmap()
#   Cullen Humphries
#   This program will ping scan a subnet for any responding interfaces
#   it is built to be an imoprtable module
#   NOTE: build for UBUNTU 14.04 LTS on Python 3.5.2
#   First Edit: 8-11-2016
#   most recent edit: 8-11-2016
############################################################################

import time
from subprocess import *
import threading
from queue import *

class __myclass:
        l = threading.Lock()
        q = Queue()

def netmap():
    print('Starting NETMAP')
    print('Pinging is required on the network for this program to work\n')
    time.sleep(0.5)
    print('This module is build for UBUNTU 14.04 LTS on Python 3.5.2')
    time.sleep(0.5)
    __createt()

def __task(worker1):
#   This is a place to store a task

    c.l.acquire()
    #f = open('test.txt','r')
    #read = f.readline()
    print(threading.current_thread().name)
    #num += 1
    c.l.release()
    
def __threader():
        c.q.get()
        __task(worker1)
        c.q.task_done()

#def __createt():
c = __myclass()
num = 1
#c.q = Queue()
#c.l = threading.Lock()
for number in range(10):
    t1 = threading.Thread(target=__threader)
    t1.start()
    for worker1 in range(20):
        c.q.put(worker1)
        
c.q.join()
#if __name__ == '__main__':
#    print('Netmap is being run by its self')
#    choice = input('continue?(y or n):  ')
#    while True:
#        if choice == 'y':
#            netmap()
#            break
#        elif choice == 'n':
#            SystemExit
#        else:
#            choice = input('please choose \'y\' or \'n\':  ')
#
#else:
#        netmap()
#netmap()

