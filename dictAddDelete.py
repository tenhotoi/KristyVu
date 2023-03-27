class Dictionary():
    def appendDictVal(key,val,dictionary):
        if key not in dictionary:
            dictionary[key] = val
        elif type(val) not in [str, list, dict]:
            raise ValueError('Value type not supported.')
        elif isinstance(val, list):
            dictionary[key].extend(val) # <<<< this would append the new values 
            # dictionary[key].append(val) # <<<< this would append the new list 
        elif isinstance(val, dict):
            dictionary[key].update(val)
        else:
            dictionary[key] = dictionary[key] + val

        return dictionary
    
    def checkAndAppendDictVal(key,val,dictionary):
        if key not in dictionary:
            dictionary[key] = val
        elif type(val) not in [str, list, dict]:
            raise ValueError('Value type not supported.')     
        elif isinstance(val, list) and isinstance(dictionary[key], list):
            dictionary[key].extend(val) # <<<< this would append the new values 
            # dictionary[key].append(val) # <<<< this would append the new list 
        elif isinstance(val, dict) and isinstance(dictionary[key], dict):
            dictionary[key].update(val)
        elif isinstance(val, str) and isinstance(dictionary[key], str):
            dictionary[key] = dictionary[key] + val   
        else:
            raise ValueError('Input value and dictionary value are mismatched types.') 
        
        return dictionary

if __name__ == '__main__':
    # initializing dictionary
    test_dict = {'gfg' : "geekfor", 'is' : {'a' : 5, 'b' : 6}, 'best' : [1, 2, 3]}
    
    # printing original dictionary
    print("The original dictionary is : " + str(test_dict))
    
    # initializing dict, string and append
    up_dict = {'c' : 7}
    up_str = 'geeks'
    up_list = [4, 5]
    
    # Append Multitype Values in Dictionary
    # Using isinstance() + update() + extend()
    res = Dictionary.appendDictVal('gfg', up_str, test_dict)
    res = Dictionary.appendDictVal('is', up_dict, res)
    res = Dictionary.appendDictVal('best', up_list, res)
    
    # printing result 
    print("The update dictionary : " + str(res)) 
    """
    Output:
    The original dictionary is : {'gfg': 'geekfor', 'is': {'a': 5, 'b': 6}, 'best': [1, 2, 3]}
    The update dictionary : {'gfg': 'geekforgeeks', 'is': {'a': 5, 'b': 6, 'c': 7}, 'best': [1, 2, 3, 4, 5]}
    """

    # initializing dict, string and append
    up_str = {'c' : 7}  # this is mistmatch value type
    up_dict = 'geeks'   # this is mistmatch value type
    up_list = [4, 5]
    
    # Append Multitype Values in Dictionary
    # Using isinstance() + update() + extend()
    res = Dictionary.checkAndAppendDictVal('gfg', up_str, test_dict)
    res = Dictionary.checkAndAppendDictVal('is', up_dict, res)
    res = Dictionary.checkAndAppendDictVal('best', up_list, res)
    
    # printing result 
    print("The update dictionary : " + str(res)) 

    # https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
    my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
    print(my_dict)
    del my_dict['Dave']  #removes key-value pair of 'Dave'
    print(my_dict)
    my_dict.pop('Ava')   #removes the value of 'Ava'
    print(my_dict)
    my_dict.popitem()    #removes the last inserted item
    print(my_dict)

    """
    Output:
    {'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
    {'Ava': '002', 'Joe': '003', 'Chris': '005'}
    {'Joe': '003', 'Chris': '005'}
    {'Joe': '003'}
    """
