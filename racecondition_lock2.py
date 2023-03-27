# https://www.pythonpool.com/python-threading-lock/
# Threading lock using context manager
# Context managers are a way of allocating and releasing some sort of resource exactly where you need it. For instance, opening and closing database connections. Let’s modify our above example:


import threading
from threading import Lock
import time
 
x = 10
 
lock = Lock()
 
def increment(increment_by,lock):
    global x
 
    with lock:
        local_counter = x
        local_counter += increment_by
 
        time.sleep(1)
 
        x = local_counter
        print(f'{threading.current_thread().name} increments x by {increment_by}, x: {x}')
 
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