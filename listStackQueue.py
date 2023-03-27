import time
# https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU

class ListStack:
    def __init__(self):
        self._L = []
    def push(self, item):
        self._L.append(item)
    def pop(self):
        return self._L.pop()
    def peek(self):
        return self._L[-1]
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self) == 0

class BadStack(ListStack):
    def push(self, item):
        self._L.insert(0, item)
    def pop(self):
        return self._L.pop(0)
    def peek(self):
        return self._L[0]
"""
A simple asymptotic analysis shows why this implementation is far less
efficient. Inserting a new item into a list requires that all the other items in
the list have to move over to make room for the new item. If we insert at
the beginning of the list, then every item has to be copied to a new position.
Thus, the insert call in push takes O(n) time. Similarly, if we pop an item
at the beginning of the list, then every other item in the list gets moved
over one space to fill in the gap. Thus, the list.pop call in our pop method
will take O(n) time as well. So, push and pop both take linear time in this
implementation. It really earns its name.
"""

class ListQueueSimple:
    def __init__(self):
        self._L = []
    def enqueue(self, item):
        self._L.append(item)
    def dequeue(self):
        return self._L.pop(0)
    def peek(self):
        return self._L[0]
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self) == 0

class ListQueueFakeDelete:
    def __init__(self):
        self._head = 0
        self._L = []
    def enqueue(self, item):
        self._L.append(item)
    def peek(self):
        return self._L[self._head]
    def dequeue(self):
        item = self.peek()
        self._head += 1
        return item
    def __len__(self):
        return len(self._L) - self._head
    def isempty(self):
        return len(self) == 0

class ListQueue(ListQueueFakeDelete):
    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head:]
            self._head = 0
            return item

class AnotherStack(ListStack):
    def pop(self):
        try:
            return self._L.pop()
        except IndexError:
            raise RuntimeError("pop from empty stack")

class ListDeque:
    def __init__(self):
        self._L = []
    def addfirst(self, item):
        self._L.insert(0, item)
    def addlast(self, item):
        self._L.append(item)
    def removefirst(self):
        return self._L.pop(0)
    def removelast(self):
        return self._L.pop()
    def __len__(self):
        return len(self._L)

if __name__ == '__main__':
    users = ['val', 'bob', 'mia', 'ron', 'ned']
    print('Original list: ', users)
    """
    If you want to work with an element that you're removing 
    from the list, you can "pop" the element. If you think of the 
    list as a stack of items, pop() takes an item off the top of the 
    stack. By default pop() returns the last element in the list, 
    but you can also pop elements from any position in the list.
    Pop the last item from a list
    """
    users.remove('mia')
    print('After remove mia from the list: ', users)
    most_recent_user = users.pop()
    print('Most recent user on the list: ', most_recent_user)
    # Pop the first item in a list
    first_user = users.pop(0)
    print('The first/oldest user from the list: ', first_user)
    print(sorted(users))
    print(sorted(users, reverse=True))
    # Adding an element to the end of the list
    users.append('amy')
    # Starting with an empty list
    # users = []
    users.append('val')
    users.append('bob')
    users.append('mia')
    # Inserting elements at a particular position
    users.insert(0, 'joe')
    users.insert(3, 'bea')
    print('After adding to the list: ', users)
    users.reverse()
    print('After reverse the list: ', users)
    print(list(reversed(users)))
    print(users)
    users.sort()
    print(users)

    q = ListQueue()
    for i in range(10):
        q.enqueue(i)
        time.sleep(0.5)
    for i in range(10):
        print(q.dequeue())
        time.sleep(0.5)
        







