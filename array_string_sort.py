# https://datagy.io/python-sort-string/

# 1. METHOD 1: Sort a Python String with Sorted

# Sort a Python String with sorted()
word = 'datagy'

sorted_word = sorted(word)
print(sorted_word)

# Returns: ['a', 'a', 'd', 'g', 't', 'y']

# >>>>>>> How can we turn this list back into a string? We can use the str.join() method, as shown below:
sorted_word = ''.join(sorted_word)
print(sorted_word)

# Returns: aadgty

# We can see that the string is now sorted (and is back to being a string). We can actually combine this into a single line by writing:
# Sort a Python String with sorted()
word = 'datagy'

sorted_word = ''.join(sorted(word))
print(sorted_word)

# Returns: aadgty

#Now, what happens when we include some capitals in our string? Let’s capitalize the first letter and see what happens:

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(word))
print(sorted_word)

# Returns: Daagty
# We can see that now the capital D appears before the lowercase a. Why does this happen? Python interprets the sorting explicitly, when we don’t apply a key, forcing the values to be sorted based on their ASCII values. In this, capital letters are sorted prior to the lowercase values.

# 2. METHOD 2: Sort a Python String with Sorted without Case Sensitivity

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(word, key=str.lower))
print(sorted_word)

# Returns: aaDgty

# If you don’t care about the capitalization, you can always convert the string to lowercase. This way, you don’t need to apply the key= parameter. Let’s see what this looks like:

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(word.lower()))
print(sorted_word)

# Returns: aadgty

# METHOD 3: Sort a Python String with Unique Characters Only

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(set(word)))
print(sorted_word)

# Returns: Dagty

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(set(word), key=str.lower))
print(sorted_word)

# Returns: aDgty

# 4. METHOD 4: Sort a Python String and Remove White Space and Punctuation

# Sort a Python String with sorted()
word = 'da ta ?gy!'

sorted_word = ''.join(filter(lambda x:x.isalpha(), sorted(word,key=lambda x:x.lower())))

print(sorted_word)

# Returns: aadgty

# Sort a Python String with sorted()
word = 'da ta ?gy!'

sorted_word = ''.join(filter(lambda x:x.isalpha(), sorted(word,key=lambda x:x.lower())))

print(sorted_word)

# Returns: aadgty

"""
Let’s see what we’ve done here:

We first sort the word using case insensitivity
We then use the filter function to keep only alphabetical characters
Finally, we join our list of characters back into a single string
"""

# >>>>>>>>>>> How to correctly sort a string with a number inside in Python? <<<<<<<<<<<<<<<<<<

# https://www.tutorialspoint.com/How-to-correctly-sort-a-string-with-a-number-inside-in-Python

# This type of sort in which you want to sort on the basis of numbers within string is called natural sort or human sort. For example, if you have the text:

['Hello1','Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']

# Then you want the sorted list to be:

['Hello1', 'Hello2','Hello12', 'Hello17', 'Hello25', 'Hello29']

# and not:

['Hello1','Hello12', 'Hello17', 'Hello2', 'Hello25', 'Hello29']

# To do this we can use the extra parameter that sort() uses. This is a function that is called to calculate the key from the entry in the list. We use regex to extract the number from the string and sort on both text and number. 

import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    # print(re.split('(\d+)',text))
    # print([ int(c) if c.isdigit() else c for c in re.split('(\d+)',text) ])
    # print([ atoi(c) for c in re.split('(\d+)',text) ])
    return [ atoi(c) for c in re.split('(\d+)',text) ]
"""
['Hello', '1', '']
['Hello', 1, '']     # <=============== after atoi
['Hello', '12', '']
['Hello', 12, '']     # <=============== after atoi
['Hello', '29', '']
['Hello', 29, '']     # <=============== after atoi
['Hello', '2', '']
['Hello', 2, '']     # <=============== after atoi
['Hello', '17', '']
['Hello', 17, '']     # <=============== after atoi
['Hello', '25', '']
['Hello', 25, '']     # <=============== after atoi
['', '1234', 'testing']
['', 1234, 'testing']     # <=============== after atoi
"""
 
if __name__ == '__main__':
    my_list = ['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25', '1234testing']
    print(new_list := sorted(my_list, key= natural_keys))   
    print(my_list) 
    print(new_list := sorted(my_list, key= lambda x: [int(c) if c.isdigit() else c for c in re.split('(\d+)', x)]))  # <============== this works now!!!
    """
    Output:
    ['1234testing', 'Hello1', 'Hello2', 'Hello12', 'Hello17', 'Hello25', 'Hello29']
    ['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25', '1234testing']
    """

    my_list.sort(key=natural_keys)
    print(my_list)
    """ 
    Output:  
    ['1234testing', 'Hello1','Hello2', 'Hello12', 'Hello17', 'Hello25', 'Hello29']
    """

    text = ['hello:hello', ':hello', 'hello:']
    print([re.split(':', x) for x in text])
    """
   [['hello', 'hello'], ['', 'hello'], ['hello', '']]
    """

    my_list = ['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
    print(sorted(my_list))

    """
    Output: ['Hello1', 'Hello12', 'Hello17', 'Hello2', 'Hello25', 'Hello29']
    """

    """
https://stackoverflow.com/questions/53958419/sort-an-array-which-contains-number-and-strings

arr.sort((a, b) => ((typeof b === "number") - (typeof a === "number")) || (a > b ? 1 : -1));

const arr = [9, 5, '2', 'ab', '3', -1];

const nums = arr.filter(n => typeof n == "number").sort((a, b) => a - b); // If the data type of a given element is a number store it in this array (and then sort numerically)
const non_nums = arr.filter(x => typeof x != "number").sort(); // Store everything that is not a number in an array (and then sort lexicographically)

const res = [...nums, ...non_nums]; // combine the two arrays
console.log(res); // [-1, 5, 9, "2", "3", "ab"]
"""

    arr = [9, 5, '2', 'ab', '3', -1, -8.8888]
    # print(sorted(arr))   # TypeError: '<' not supported between instances of 'str' and 'int'
    print(a := sorted([x for x in arr if not isinstance(x, str)]))    
    print(b := sorted(x for x in arr if isinstance(x, str)))    
    # print(c := sorted([atoi(x) for x in arr if isinstance(x, str)]))  # TypeError: '<' not supported between instances of 'str' and 'int'
    print(sortedArr := a + b)

    """
    Output:
    [-8.8888, -1, 5, 9]
    ['2', '3', 'ab']
    [-8.8888, -1, 5, 9, '2', '3', 'ab']
    """
    print([type(x) for x in arr])
    print(testing := [str(x) for x in arr if not isinstance(x, str)])
    # Output: ['9', '5', '-1', '-8.8888']
    print(testing := ['test%d' % x for x in arr if not isinstance(x, str)])
    # Output: ['test9', 'test5', 'test-1', 'test-8']
    print(atoi_strsub := [atoi(s) for s in arr if isinstance(s, str)])
    print(substr_atoi := [int(s) if s.isdigit() else s for s in arr if isinstance(s, str)])
    print(subint := [x for x in arr if not isinstance(x, str)])
    print(newarr := substr_atoi + subint)

    print(e := sorted([x for x in newarr if not isinstance(x, str)]))    
    print(f := sorted(x for x in newarr if isinstance(x, str)))    
    print(sortedArr := e + f)

    """
    Output:
    [2, 'ab', 3]
    [9, 5, -1, -8.8888]
    [2, 'ab', 3, 9, 5, -1, -8.8888]
    [-8.8888, -1, 2, 3, 5, 9]
    ['ab']
    [-8.8888, -1, 2, 3, 5, 9, 'ab']
    """

# https://betterprogramming.pub/sorting-a-python-pandas-dataframes-by-index-and-value-7306ac754014
# https://realpython.com/python-sort/

"""
>>> # Python 3
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
"""
numbers_tuple = (6, 9, 3, 1)
numbers_set = {5, 5, 10, 1, 0}
numbers_tuple_sorted = sorted(numbers_tuple, reverse=True)
numbers_set_sorted = sorted(numbers_set)
print(numbers_tuple_sorted)
# [1, 3, 6, 9]
print(numbers_set_sorted)
# [0, 1, 5, 10]

string_number_value = '34521'
string_value = 'I like to sort'
sorted_string_number = sorted(string_number_value)
sorted_string = sorted(string_value)
print(sorted_string_number)
# ['1', '2', '3', '4', '5']
print(sorted_string)
# [' ', ' ', ' ', 'I', 'e', 'i', 'k', 'l', 'o', 'o', 'r', 's', 't', 't']

string_value = 'I like to sort'
sorted_string = sorted(string_value.split())
print(sorted_string)
# ['I', 'like', 'sort', 'to']
print(' '.join(sorted_string))
# 'I like sort to'

mixed_numbers = [5, "1", 100, "34"]
"""
sorted(mixed_numbers)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
"""
# List comprehension to convert all values to integers
print([int(x) for x in mixed_numbers])
# [5, 1, 100, 34]
print(sorted([int(x) for x in mixed_numbers]))
# [1, 5, 34, 100]