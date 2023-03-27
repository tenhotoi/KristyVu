# https://www.educative.io/blog/top-five-concurrency-interview-questions-for-software-engineers
# https://pypi.org/project/readerwriterlock/

# Install the python package readerwriterlock on cmd window
# python3 -m pip install -U readerwriterlock

# Instantiate an instance of the chosen RWLock class:
import readerwriterlock
from readerwriterlock import rwlock
a = rwlock.RWLockFairD()

# Generate read locks and write locks using the following methods:
a_reader_lock = a.gen_rlock()
a_writer_lock = a.gen_wlock()

# Use the generated read/write locks to protect section in your code:
# Pythonic usage example
with a.gen_rlock():
  print('#Read stuff')

with a.gen_wlock():
  print('#Write stuff')

# Use case (Timeout) example
b = a.gen_wlock()
if b.acquire(blocking=True, timeout=5):
    try:
        print('#Do stuff')
    finally:
        b.release()

# Use case (Downgrade) example
b = a.gen_wlock()
if b.acquire():
    try:
        #Read/Write stuff
        b = b.downgrade()
        #Read stuff
    finally:
        b.release()

