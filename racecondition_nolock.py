""" 
https://www.glassdoor.com/Interview/Pure-Storage-Interview-Questions-E364364.htm
This is the race condition, both P1 and P2 race to see who will write the value last.

https://www.pythonpool.com/python-threading-vs-multiprocessing/
"""

import threading
import time
 
x = 10
 
def increment(increment_by):
    global x
 
    local_counter = x
    local_counter += increment_by
 
    time.sleep(1)
 
    x = local_counter
    print(f'{threading.current_thread().name} increments x by {increment_by}, x: {x}')
 
# creating threads
t1 = threading.Thread(target=increment, args=(5,))
t2 = threading.Thread(target=increment, args=(10,))
 
# starting the threads
t1.start()
t2.start()
 
# waiting for the threads to complete
t1.join()
t2.join()
 
print(f'The final value of x is {x}')