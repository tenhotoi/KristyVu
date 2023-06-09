# ReadWrite Lock: might consider race condition? 
# https://stackoverflow.com/questions/34510/what-is-a-race-condition
# https://www.pythonpool.com/python-threading-lock/
# Race condition can be avoided if locking is used

# Locked – means critical section is occupied, in binary i.e. 1
# Unlocked – means critical section is vacant, in binary i.e 0.

import threading
from threading import Lock
import time
 
x = 10
 
def increment(increment_by,lock):
    global x
 
    lock.acquire()
 
    local_counter = x
    local_counter += increment_by
 
    time.sleep(1)
 
    x = local_counter
    print(f'{threading.current_thread().name} increments x by {increment_by}, x: {x}')
 
    lock.release()
 
lock = Lock()
 
# creating threads
t1 = threading.Thread(target=increment, args=(5,lock))
t2 = threading.Thread(target=increment, args=(10,lock))
 
# starting the threads
t1.start()
t2.start()
 
# waiting for the threads to complete
t1.join()
t2.join()
 
print(f'The final value of x is {x}')