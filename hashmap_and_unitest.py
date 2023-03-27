# https://khalilstemmler.com/blogs/data-structures-algorithms/hash-tables/
# https://www.geeksforgeeks.org/hash-map-in-python/ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class HashTable:
 
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def set_val(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 
    # Return searched value with specific key
    def get_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
 
    # Remove a value with specific key
    def delete_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)
    
#https://www.geeksforgeeks.org/hash-map-in-python/ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Many hash table implementations found in programming languages (such as Java's HashMap or Python's dict) dynamically increase the size of the hash table once the number of items reaches a certain threshold.
# increase hash table size by two if the table is filled more than half
class HashTable_Enhanced:
 
    # Create empty bucket list of given size
    def __init__(self, size=10):
        self.size = size
        self.hash_table = self.create_buckets()
        self.count = 0

    def __len__(self):
        return self.count
    
    def __resize__(self):
        if self.count >= (self.size // 2):
            self.size = self.size * 2
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def set_val(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

        self.count += 1
 
    # Return searched value with specific key
    def get_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
 
    # Remove a value with specific key
    def del_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
            self.count -= 1
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

# https://techcolleague.com/hashmap-in-python/ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class HashMap_Advanced:

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        # self.buckets = [None] * self.capacity
        self.buckets = [[] for _ in range(self.capacity)]
    
    def hash_function(self, key):
        # Custom hash function to generate hash codes
        hash_code = 0
        for char in key:
            hash_code += ord(char)
        return hash_code % self.capacity
    
    def put(self, key, value):
        # Insert a key-value pair into the hash map
        # index = self.hash_function(key)
        index = hash(key) % self.capacity                           # !!!!!!!!! DOESN'T WORK HERE EITHER !!!!!!!!!!!
        if self.buckets[index] is None:
            self.buckets[index] = []
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
        self.size += 1
    
    def get(self, key):
        # Get the value associated with a key in the hash map
        # index = self.hash_function(key)
        index = hash(key) % self.capacity
        if self.buckets[index] is None:
            return None
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        # Remove a key-value pair from the hash map
        # index = self.hash_function(key)
        index = hash(key) % self.capacity
        if self.buckets[index] is None:
            return
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                self.size -= 1
                return
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        pairs = []
        for bucket in self.buckets:
            if bucket is None:
                continue
            for k, v in bucket:
                pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"
     
# https://algodaily.com/challenges/implement-a-hash-map/python <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Hashmap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for _ in range(capacity)]
        self.size = 0

    def hashStr(self, key):
        if isinstance(key, int):
            return key

        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result

    def position(self, key_hash):
        return key_hash % self.capacity

    def set_working(self, key, val):
        p = Node(key, val)
        # key_hash = self.hashStr(key)
        key_hash = hash(key) % self.capacity
        index = self.position(key_hash)

        if not self.storage[index]:
            self.storage[index] = [p]
            self.size += 1
            print(' the bucket is empty '.center(60, '~'))
        else:
            list_at_index = self.storage[index]
            if p not in list_at_index:
                print('p not in list_at_index'.center(60,'!'))
                self.storage[index] = [p]
                # self.size += 1
            else:
                for i in self.storage[index]:
                    print('p in list_at_index'.center(60,'!'))
                    if i == p:
                        i.value = val
                        break

    def set(self, key, val):
        # key_hash = self.hashStr(key)
        #index = self.position(key_hash)        
        index = hash(key) % self.capacity

        if not self.storage[index]:
            self.storage[index] = Node(key, val)
            self.size += 1
            print(' the bucket is empty '.center(60, '~'))
        else:
            node = self.storage[index]
            prev = None
            key_found = 0
            tmp = 0
            while node is not None: 
                tmp += 1
                print(f' key_found is {key_found}, loop {tmp} '.center(60, '@'))
                print(' this is for in while node is not None '.center(60, '*'))
                if node.key == key:
                    print(' key is found here '.center(60,'!'))                        
                    node.value = val
                    key_found += 1
                    break
                else:
                    prev = node
                    node = node.next

            if key_found == 0:
                print(' key was NOT found '.center(60,'!'))
                node.next = Node(key, val)
                # self.size += 1

    def get(self, key):
        # key_hash = self.hashStr(key)
        # index = self.position(key_hash)
        index = hash(key) % self.capacity

        if not self.storage[index]:
            print(' WHEN TRYING TO GET THE VALUE: the bucket is empty '.center(60, '~'))
            return None
        else:
            node = self.storage[index]
            prev = None
            while node is not None:
                if node.key == key:
                    return node.value
                else:
                    prev = node
                    node = node.next
        return None

    def __str__(self) -> str:
        return "".join([str(item) for item in self.storage])
    
# https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
class Node_LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable_LinkedNode:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets = [None for _ in range(capacity)]
        
    def hash_local(self, key):
        hashsum = 0
        # For each character in the key

        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)

            hashsum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]

            hashsum = hashsum % self.capacity
        return hashsum
    
    def insert(self, key, value):
        # 2. Compute index of key

        index = self.hash_local(key)
        index = hash(key) % self.capacity         # !!! WARNING: !!! not sure why this doesn't work!!!!!!!!!! (new notes: it works after adding same hash method in all functions in the class)
        ############# Might want to check out this link again: https://www.geeksforgeeks.org/python-hash-method/
        # Go to the node corresponding to the hash

        node = self.buckets[index]
        # 3. If bucket is empty:

        if node is None:
            # Create node, add it, return

            self.buckets[index] = Node(key, value)
            print(' the bucket is empty '.center(60, '='))
            # 1. Increment size
            self.size += 1            
            return
        # 4. Collision! Iterate to the end of the linked list at provided index

        key_found = 0
        prev = None
        while node is not None:
            print(f' key_found is {key_found} '.center(60, '@'))
            if node.key == key:
                print(' i found key here '.center(60, '+'))
                node.value = value
                key_found += 1
                break
            else:
                print(' node is not seen in the bucket '.center(60, '-'))
                prev = node
                node = node.next
        # Add a new node at the end of the list with provided key/value

        if key_found == 0:
            prev.next = Node(key, value)


    def find(self, key):
        # 1. Compute hash

        # index = self.hash_local(key)
        index = hash(key) % self.capacity
        # 2. Go to first node in list at bucket

        node = self.buckets[index]
        # 3. Traverse the linked list at this node

        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None

        if node is None:
            # Not found

            return None
        else:
            # Found - return the data value

            return node.value
        
    def remove(self, key):
        # 1. Compute hash

        # index = self.hash_local(key)
        index = hash(key) % self.capacity
        node = self.buckets[index]
        prev = None
        # 2. Iterate to the requested node

        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none

        if node is None:
            # 3. Key not found

            return None
        else:
            # 4. The key was found.

            self.size -= 1
            result = node.value
            # Delete this element in linked list

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            # Return the deleted language

            return result
        
    def __str__(self) -> str:
        return ''.join([str(bucket) for bucket in self.buckets])
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TESTING <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

import unittest

class Test(unittest.TestCase):

    def test_hashmap(self):
        hash_table = HashTable(10)
        
        # insert some values
        hash_table.set_val('gfg@example.com', 'some value')
        print(hash_table)
        
        hash_table.set_val('portal@example.com', 'some other value')
        print(hash_table)
        
        # search/access a record with key
        assert hash_table.get_val('portal@example.com') == 'some other value'
        
        # delete or remove a value
        hash_table.delete_val('portal@example.com')
        assert hash_table.get_val('portal@example.com') == 'No record found'
        print(hash_table)

    def test_hashmap_enhanced(self):
        hash_table = HashTable_Enhanced(10)
        
        # insert some values
        hash_table.set_val('gfg@example.com', 'some value')
        assert hash_table.count == 1
        print(hash_table)
        
        hash_table.set_val('portal@example.com', 'some other value')
        assert hash_table.count == 2
        print(hash_table)
        
        # search/access a record with key
        assert hash_table.get_val('portal@example.com') == 'some other value'
        
        # delete or remove a value
        hash_table.del_val('portal@example.com')
        assert hash_table.get_val('portal@example.com') == 'No record found'
        assert hash_table.count == 1
        print(hash_table)
        
    def test_hashmap_Advanced(self):
        hash_table = HashMap_Advanced(10)
        
        # insert some values
        hash_table.put('gfg@example.com', 'some value')
        assert hash_table.size == 1
        print(hash_table)
        
        hash_table.put('portal@example.com', 'some other value')
        assert hash_table.size == 2
        print(hash_table)
        
        # search/access a record with key
        assert hash_table.get('portal@example.com') == 'some other value'
        
        # delete or remove a value
        hash_table.remove('portal@example.com')
        assert hash_table.get('portal@example.com') == None
        assert hash_table.size == 1
        print(hash_table)

    def test_hashtable_linkednode(self):
        dict = HashTable_LinkedNode(20)
        dict.insert("jess", "213-559-6840")
        dict.insert("jess", "213-559-0000")
        dict.insert("jess", "213-559-1111")
        assert dict.size == 1
        dict.insert("james", "123-456-7890")
        dict.insert("james", "123-456-0000")
        dict.insert("james", "123-456-1111")
        assert dict.size == 2
        assert dict.find("james") == "123-456-1111"
        dict.remove("james")
        assert dict.size == 1
        print("PASSED: Instantiate a `HashTable_LinkedNode`, and set keys.")
        dict.insert("jess", "213-559-6840")
        print('dict.size is now: {:9}'.format(dict.size))
        assert dict.size == 1
        assert callable(dict.insert) == True
        assert dict.find("jess") == "213-559-6840"
        print("PASSED: Hashmap class has a `get` method")
        # print(dict)

    def test_1(self):
        dict = Hashmap(16)
        dict.set("jess", "213-559-6840")
        dict.set("jess", "213-559-0000")
        dict.set("jess", "213-559-1111")
        assert dict.size == 1
        dict.set("james", "123-456-7890")
        dict.set("james", "123-456-0000")
        dict.set("james", "123-456-1111")
        assert dict.size == 2
        assert dict.get("james") == "123-456-1111"
        print("PASSED: Instantiate a `Hashmap`, and set keys.")
        # print(dict)

    def test_2(self):
        dict = Hashmap(16)
        dict.set("jess", "213-559-6840")
        assert dict.size == 1
        dict.set("james", "123-456-7890")
        assert dict.size == 2
        assert dict.get("jake") == None
        print("PASSED: `Hashmap` will return `None` if nothing found")
        # print(dict)

    def test_3(self):
        dict = Hashmap(16)
        assert callable(dict.set) == True
        print("PASSED: Hashmap class has a `set` method")
        # print(dict)

    def test_4(self):
        dict = Hashmap(16)
        dict.set("jess", "213-559-6840")
        assert dict.size == 1
        assert callable(dict.get) == True
        assert dict.get("jess") == "213-559-6840"
        print("PASSED: Hashmap class has a `get` method")
        # print(dict)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 8/8 tests passed!")

"""
https://www.scaler.com/topics/hashmap-in-python/
https://iq.opengenus.org/different-collision-resolution-techniques-in-hashing/

Following are the collision resolution techniques used:

1. Open Hashing (Separate chaining): Collisions are resolved using a list of elements to store objects with the same hashed key (hash(key) % size) together.
    Append the colliding keys:values to a list being pointed by their hash keys to buckets = hashtable[hash(key) % size]
    Say, for a load factor:
    λ=number of objects stored in table/size of the table (can be >1)
    a good hash function would guarantee that the maximum length of list associated with each key is close to the load factor.
2. Closed Hashing (Open Addressing): This collision resolution technique requires a hash table with fixed and known size. 
    During insertion, if a collision is encountered, alternative cells are tried until an empty bucket is found. 
    These techniques require the size of the hash table to be supposedly larger than the number of objects to be stored (something with a load factor < 1 is ideal).
    There are various methods to find these empty buckets:
        a/ Liner Probing:  H(x, i) = (H(x) + i)%N
            where N is the size of the table and i represents the linearly increasing variable which starts from 1 (until empty bucket is found).
        b/ Quadratic probing: H(x, i) = (H(x) + i^2)%N
            In general, H(x, i) = (H(x) + ((c1\*i^2 + c2\*i + c3)))%N, for some choice of constants c1, c2, and c3
        c/ Double hashing: H(x, i) = (H1(x) + i*H2(x))%N
            Typically for H1(x) = x%N a good H2 is H2(x) = P - (x%P), where P is a prime number smaller than N.

https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
"""