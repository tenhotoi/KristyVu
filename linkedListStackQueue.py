# https://medium.com/@sarperismetmakas/linked-list-with-tail-implementation-beeb4dd6b8b8 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
    else:
        self.tail.next = new_node
    self.tail = new_node
    length += 1

def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node

def insert(self, index, data):
    if index < 0 or index > self.length:
        raise IndexError("Index out of range")
    if index == 0:
        self.prepend(data)
    elif index == self.length - 1:
        self.append(data)
    else:
        current_node = self.head
        for i in range(index - 1):
            if current_node is None:
                return
            current_node = current_node.next
        if current_node is None:
            return
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
        if new_node.next is None:
            self.tail = new_node
    self.length += 1

def pop(self, index):
    if index < 0 or index > self.length:
        raise IndexError("Index out of range")
    if index == 0:
        if self.head is None:
            self.length -= 1
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return removed_node.data
    
    if index == self.length-1:
        self.length -= 1
        self.tail = None


    current_node = self.head
    for i in range(index - 1):
        if current_node.next is None:
            self.length -= 1
            return None
        current_node = current_node.next

    if current_node.next is None:
        self.length -= 1
        return None

    removed_node = current_node.next
    current_node.next = removed_node.next
    if current_node.next is None:
        self.tail = current_node
    
    self.length -= 1
    return removed_node.value

def reverse(self):
    prev_node = None
    current_node = self.head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    self.head, self.tail = self.tail, self.head

def __len__(self):
    return self.length

def __str__(self):
    nodes = []
    current_node = self.head
    while current_node is not None:
        nodes.append(str(current_node.value))
        current_node = current_node.next
    return ' -> '.join(nodes)

def __getitem__(self, index):
    if index < 0 or index >= len(self):
        raise IndexError('Index out of range')
    current_node = self.head
    for i in range(index):
        current_node = current_node.next
    return current_node.data

def __setitem__(self, index, data):
    if index < 0 or index >= len(self):
        raise IndexError('Index out of range')
    current_node = self.head
    for i in range(index):
        current_node = current_node.next
    current_node.data = data

# https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU

class ListNode:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self._head = None
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        return item

class LinkedList:
    def __init__(self):
        self._head = None
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            currentnode = self._head
        while currentnode.link is not None:
            currentnode = currentnode.link
            currentnode.link = ListNode(item)
    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        return item
    def removelast(self):
        if self._head.link is None:
            return self.removefirst()
        else:
            currentnode = self._head
        while currentnode.link.link is not None:
            currentnode = currentnode.link
            item = currentnode.link.data
            currentnode.link = None
        return item

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None: self._tail = self._head
    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None: self._tail = None
        return item
    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
        while currentnode.link is not self._tail:
            currentnode = currentnode.link
            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
        return item

class LinkedQueue:
    def __init__(self):
        self._L = LinkedList()
    def enqueue(self, item):
        self._L.addlast(item)
    def dequeue(self):
        return self._L.removefirst()
    def peek(self):
        item = self._L.removefirst()
        self._L.addfirst(item)
        return item
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self) == 0

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None: self._tail = self._head
        self._length += 1
    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1
    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None: self._tail = None
        self._length -= 1
        return item
    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
        while currentnode.link is not self._tail:
            currentnode = currentnode.link
            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
        return item
    def __len__(self):
        return self._length

