#!/bin/python3
#test_threading


import threading

import time
tlock = threading.Lock()

def timer(name, delay, repeat):
    print('\nTimer: '+ name +' Started')
    tlock.acquire()
    print(name+' has acquired the lock')
    while repeat > 0:
          time.sleep(delay)
          print(name+ ': '+str(time.ctime(time.time())),'')
          repeat -= 1
    print(name, 'lock is released')
    tlock.release()
    print('Timer: ' +name+ ' is complete\n')
    

def main():
          thread1 = threading.Thread(target=timer, args=('Timer-1', 1, 5))
          thread2 = threading.Thread(target=timer, args=('Timer-2', 2, 5))
          thread1.start()
          thread2.start()
if __name__ == '__main__':
    main()
