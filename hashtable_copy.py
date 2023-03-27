# https://www.geeksforgeeks.org/hash-map-in-python/
# https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/

class HashTable:
 
    """
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
    """
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def set_val(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
        print('hashed_key for set_val is: ', hashed_key)
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        print('bucket is : ', bucket)
 
        found_key = False
        for index, record in enumerate(bucket):
            print('index, record are: ', index, record)
            record_key, record_val = record
            print('record_key, record_val are: ', record_key, record_val)
             
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
            bucket.append((key+'test', val+'test'))

        for index, record in enumerate(bucket):
            print('index, record are: ', index, record)
            record_key, record_val = record
            print('record_key, record_val are: ', record_key, record_val)
            if record_key == key:
                print('MATCHING KEY FOUND')
            else:
                print('KEY IS NOT FOUND HERE')
 
    # Return searched value with specific key
    def get_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        print('hashed_key for get_val is: ', hashed_key)
         
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
        print('hashed_key for delete_val is: ', hashed_key)
         
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
        return "".join(str(item) for item in self.hash_table)
 
if __name__ == '__main__':
    hash_table = HashTable(50)
    print(hash_table)

    # insert some values
    hash_table.set_val('gfg@example.com', 'some value')
    print(hash_table)
    print('\n')
    
    hash_table.set_val('portal@example.com', 'some other value')
    print(hash_table)
    print('\n')
    
    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print('\n')
    
    # delete or remove a value
    hash_table.del_val('portal@example.com')
    print(hash_table)

def select_choice():
    i = 1
    card = "Driver licence"
    return i, card # or [i, card]

my_i, my_card = select_choice()
print("\n >>>>>>>>> my_i and my_card are: \n", my_i, my_card)
print("\n >>>>>>>>> my_i and my_card are: \n", select_choice())
    
hash_table2 = HashTable(50)
print(hash_table2)

# insert some values
hash_table2.set_val('gfg@example.com', 'some value')
print(hash_table2)
print('\n')

hash_table2.set_val('portal@example.com', 'some other value')
print(hash_table2)
print('\n')

# search/access a record with key
print(hash_table2.get_val('portal@example.com'))
print('\n')

# delete or remove a value
hash_table2.del_val('portal@example.com')
print(hash_table2)
