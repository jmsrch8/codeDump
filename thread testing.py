import threading
from queue import Queue
import time

pl = threading.Lock()
q = Queue()

def exjob():
    time.sleep(0.5)

    with pl:
        print(threading.current_thread().name)


def threader():
#        q.get()
        exjob()
#        q.task_done()



start = time.time()
threads = []
for x in range(10):
    t = threading.Thread(target = threader, daemon = True)
    t.start()
    threads.append(t)

#for worker in range(20):
#    q.put(worker)
    
#q.join()

for t in threads:    
    t.join()
print('Entire job took:', time.time()-start)


