# https://www.geeksforgeeks.org/create-linked-list-from-a-given-array/

# Python3 implementation of the approach 
import math

# Time Complexity : O(n*n)
# Representation of a node
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# Function to insert node
def insert(root, item):
    temp = Node(item)
      
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
      
    return root
  
def display(root):
    while (root.next != None) :
        print(root.data, end = "->")
        root = root.next
    print(root.data,'\n')
          
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
      
    return root
  
# Driver code
if __name__=='__main__': 
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)

# Python3 program to print level order traversal 
# in spiral form using one queue and one stack.   Time Complexity : O(n)
  
# Representation of a Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = next
  
# Function to insert Node 
def insert(root, item): 
    temp = Node(0) 
    temp.data = item 
    temp.next = root 
    root = temp
    return root 
  
def display(root): 
    while (root.next != None): 
        print(root.data, end="->") 
        root = root.next 
    print(root.data, '\n')
  
def arrayToList(arr, n): 
    root = None 
    for i in range(n - 1, -1, -1): 
        print('i is currently: ', i)
        root = insert(root, arr[i])
        # display(root)
    return root 
  
# Driver code 
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5]; 
    n = len(arr) 
    root = arrayToList(arr, n); 
    display(root) 

    port_mappings = [
    "__10.1.1.1|10.2.2.2__",
    "portA:member1_port3",
    "portB:member2_port27",
    "portC:member1_port14",
    "__10.3.3.3__",
    "portA:port4",
    "portB:port15",
    "__10.3.3.4__",
    "portA:port4",
    "portB:port15",
    "__Switch1A|Switch1B__",
    "portA:member2_port30",
    "portB:member1_port270",
    "portC:member2_port140"
    ]
    n = len(port_mappings) 
    print('size of port_mappings is: ', n)
    root = arrayToList(port_mappings, n); 
    display(root) 

    def makeLinkedLists(arr):
        root = None
        arrInvert = arr[:-1]
        print('arrInvert is: ', arrInvert)
        for item in arr[::-1]:
            root = insert(root, item)
                
            if item.count('__'):
                display(root)                 
                root = None
     
    makeLinkedLists(port_mappings)

    port_mappings = [
    "__10.1.1.1|10.2.2.2__",
    "portA:member1_port3",
    "portB:member2_port27",
    "portC:member1_port14",
    "__10.3.3.3__",
    "portA:port4",
    "portB:port15",
    "__10.3.3.4__",
    "portA:port40",
    "portB:port150",
    "__Switch1A|Switch1B__",
    "portA:member2_port30",
    "portB:member1_port270",
    "portC:member2_port140"
    ]

    config_file = [
    "__10.1.1.1|10.2.2.2__",
    "portA:enabled=true",
    "portB:vlan=10",
    "portC:vlan=200",
    "__10.3.3.4__",
    "portA:enabled=true",
    "portA:poe=false",
    "portA:speed=100mbps",
    "portB:vlan=15",
    "__10.3.3.3__",
    "portA:enabled=true",
    "portA:poe=false",
    "portA:speed=100mbps",
    "portB:vlan=15",
    "__Switch1A|Switch1B__",
    "portA:enabled=true",
    "portA:poe=false",
    "portA:speed=100mbps",
    "portB:vlan=15"
    ]

    class Dict:
        def mergeArrays(arrmerge, arr):
            value = [] 
            dic = {}
            headers = []
            # arrInvert = arr[::-1]         
            # print('arrInvert is: ', arrInvert)
            for item in arr[::-1]:
                if item.count('__'):
                    headers.append(item)
                    dic.update({item:value})
                    print(dic,'\n')
                    value = []                   
                elif item.count(':'):
                    value.append(item)
                else:
                    return 'Invalid inputs.'

            for header in headers:
                print('The value of header ', header, 'in the dictionary is: ', dic[header])

            tmparr = []
            for each in arrmerge:
                if each.count('__'):
                    mapvalues = dic[each]
                    tmparr.append(each)
                elif each.count(':'):
                    spliteach = each.split(':')
                    for val in mapvalues:
                        splitval = val.split(':')
                        if spliteach[0] == splitval[0]:
                            tmparr.append(splitval[1]+':'+spliteach[1])
                else:
                    return 'Invalid inputs.'
            return tmparr

    def solution(config_file, port_mappings):
        value = [] 
        dic = {}
        for item in port_mappings[::-1]:
            if item.count('__'):
                dic.update({item:value})
                print(dic,'\n')
                value = []                   
            elif item.count(':'):
                value.append(item)
            else:
                return 'Invalid inputs.'

        mergearr = []
        for each in config_file:
            if each.count('__'):
                mapvalues = dic[each]
                mergearr.append(each)
            elif each.count(':'):
                spliteach = each.split(':')
                for val in mapvalues:
                    splitval = val.split(':')
                    if spliteach[0] == splitval[0]:
                        mergearr.append(splitval[1]+':'+spliteach[1])
            else:
                return 'Invalid inputs.'
        return mergearr

    # config_file = ["1","2","3"]
    # port_mappings = ["4","5","6"]
    mergeArray = solution(config_file, port_mappings)
    print(mergeArray)
        