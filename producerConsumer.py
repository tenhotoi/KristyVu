import threading
import time

# import pdb
# pdb.set_trace()

""" In Python, we can use the debugger pdb for debugging the code. To start
debugging we have to enter following lines on the top of a Python script.
After adding these lines, our code runs in debug mode. Now we can use
commands like breakpoint, step through, step into etc for debugging. 
"""

index = 1

while 1:
    print(index)
    index += 1
    
    if(index == 5):
        break

# https://www.geeksforgeeks.org/inter-process-communication-ipc/
limit = 3
fill = 0
clear = 0
share_buff = []

class ProducerConsumer:
    def __init__(self) -> None:
        pass
        # producer = self.producer(limit, fill, clear)
        # consumer = self.consumer(limit, fill, clear)

    def producer(self,limit, fill, clear):
        # producer
        produceItem = 1
        while 1:
            while ((fill + 1) % limit == clear):
                print('waiting for CONSUMER to consume')
                # return
                self.consumer(self, limit, fill, clear)
            
            share_buff[fill] = produceItem
            fill += 1
            print(share_buff)

    def consumer(self,limit, fill, clear):
        # consumer
        while 1:
            while (fill == clear):
                print('waiting for PRODUCER to produce')
                # return
                self.producer(self, limit, fill, clear)

            consumeItem = share_buff[clear]
            clear += 1
            print(share_buff)

ProducerConsumer.producer(limit, fill, clear)