# https://www.geeksforgeeks.org/hash-map-in-python/
 
class HashTable:   
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            print(record)
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]
        print(bucket)

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found."

    def del_val(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        return
    
    # To print the items of hash map 
    # (without this section, print(hashtable) would only shows: <__main__.HashTable object at 0x000002ADB9213CD0>)
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)

def solution3(config_file, port_mappings):
    # Creating dictionaries from port_mappings, and store them in hash table    
    hashtable = HashTable(50)
    print(hashtable)
    value = {}

    for item in port_mappings[::-1]:
        if item.count('__'):
            hashtable.set_val(item, value)
            value = {}                   
        elif item.count(':'):
            # print('item is: ', item, item.split(":"))
            # splititem = item.split(":")
            # value[splititem[0]] = splititem[1]              # one way to update the dictionary for value
            # value.update({splititem[0]:splititem[1]})       # another way to update value dictionary
            # https://stackoverflow.com/questions/65415958/valueerror-dictionary-update-sequence-element-0-has-length-1-2-is-required-py
            value.update(dict([item.split(":")]))
        else:
            return ["invalid_arguments_given"]
    print('\n Created hash_table is: ', hashtable)
    print(hashtable)

    import json

    with open('hashtable_file.txt', 'w+') as f:
        # print(json.load(f))               # raise JSONDecodeError("Expecting value", s, err.value) from None
        # json.dump(hashtable, f)           # TypeError: Object of type HashTable is not JSON serializable
        # print(json.load(f))
        f.write(hashtable)                # TypeError: write() argument must be str, not HashTable
        print(f'FILE CONTENTS: {f.read()}. END OF FILE.')

    # Merge arrays
    mergearr = []
    for each in config_file:
        if each.count('__'):
            mapvalues = hashtable.get_val(each)
            print('mapvalues are: ', mapvalues)
            mergearr.append(each)
        elif each.count(':'):
            spliteach = each.split(':')
            if mapvalues[spliteach[0]]:
                    mergearr.append(mapvalues[spliteach[0]]+':'+spliteach[1])
                    # print('current mergearr is: ', mergearr)
            else:
                return ["invalid_arguments_given"]
        else:
            return ["invalid_arguments_given"]
    # print('FINAL MERGEARR BEFORE BEING RETURNED IS: ', mergearr)
    return mergearr

if __name__ == '__main__':

    hash_table_new = HashTable(50)
    
    # insert some values
    hash_table_new.set_val('gfg@example.com', 'some value')
    print(hash_table_new)
    print()
    
    hash_table_new.set_val('portal@example.com', 'some other value')
    print(hash_table_new)
    print()
    
    # search/access a record with key
    print(hash_table_new.get_val('portal@example.com'))
    print()
    
    # delete or remove a value
    hash_table_new.del_val('portal@example.com')
    print(hash_table_new)

    config_file = ["1","2","3"]
    port_mappings = ["4","5","6"]
    mergeArray = solution3(config_file, port_mappings)
    print('\n FINAL 1ST MERGEARR IS: ', mergeArray)


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
    mergeArray = solution3(config_file, port_mappings)
    print('\n FINAL 2ND MERGEARR IS: ', mergeArray)



    """
    # https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU
    import time
    for i in range(1):
        start = time.time()
        for i in range(1):
            mergeArray = solution(config_file, port_mappings)
        timetaken = time.time() - start
        print("Time taken: ", timetaken)

    def timetrials(trials = 1):
        totaltime = 0
        #start = time.time()
        for i in range(trials):
            start = time.time() # it should be here
            for i in range(1):
                mergeArray = solution(config_file, port_mappings)        
            totaltime += time.time() - start
        print("average =%10.7f " % (totaltime/trials))

    timetrials()

    https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
    """
