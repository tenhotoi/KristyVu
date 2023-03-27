def toy(toy_name):
    print("Play with", toy_name)
toy

def toy(toy_name):
    print("Play with", toy_name)

toy("Chess")

first_toy = toy
print(callable(first_toy))

print(type(first_toy))

# variables are not callable because it doesn't return anything

sum1 = 2 + 2
print(callable(sum1))

# 1. With Arguments
dict_arg = dict(arg1 = 2, arg2 = 1)

# 2. With iterable by using the zip method
dict_iter = dict(zip(['i1', 'i2', 'i3'], [23,43,56]))

# 3. With Mapping
dict_map = {'pincode':2352, 'state':'city_name'}

print(callable(dict))

print(type(dict))

# num1 is a numerator and num2 is a denominator
print(divmod(42, 2))
print(divmod(15, 3))

print(callable(divmod))

#1. Enumerate with list

list_name = ['HP', 'Apple', 'Tesla']

# define the object of enumerating
enum = enumerate(list_name) 
print(list(enum))

# change the start argument value
# define the object of enumerating
enum = enumerate(list_name, start = 2) 
print(list(enum))

# We can use enumerate with for loop to iterate sequence items one-by-one
for index, company_name in enumerate(list_name):
    print(index, company_name)

# All method examples

# 1. If all items in a sequence are integer

all_list = [7, 23, 45,-34, 9]
print(all(all_list))

# 2. If one of the items in a list is a string

all_list = [7, 23, 'Amit',-34, 9]
print(all(all_list))

# 3. If one of the items is zero or False

all_list = [7, 23, 'Amit',-34, 0]
print(all(all_list))

# 4. If the sequence is empty

all_list = []
print(all(all_list))

# Any method examples

# 1. If all items in a sequence are integer

all_list = [7, 23, 45,-34, 9]
print(any(all_list))

# 2. If one of the items in a list is a string and others are False or zero

all_list = [0, 0, 'Amit', False, 0]
print(any(all_list))

# 3. If only one item is zero or False

all_list = [0]
print(any(all_list))

# 4. If the sequence is empty

all_list = []
print(any(all_list))

# 1. When we use a filter with a custom function

def equal_func(x):
    if x == 89:
        return True
    else:
        return False

mylist = [34, 67, 56, 89, 90]
result = filter(equal_func, mylist)
num_list = list(result)
print(num_list)

# 2. When we use None in the filter method

mylist = [34, 0, 56, 89, 90, False]
result = filter(None, mylist)
num_list = list(result)
print(num_list)

# 3. When using a filter with a lambda function

mylist = [34, 67, 56, 89, 90]
result = list(filter(lambda x: x==89, mylist))
print(result)

mylist = [34, 0, 56, 89, 90, False]
result = filter(None, mylist)
num_list = list(result)
print(num_list)

# 1. Zipping two iterator

lakes = ['Victoria', 'Baikal', 'Huron']
Ocean = ['Pacific', 'Artic', 'Indian']

result = zip(lakes, Ocean)
ziplist = list(result)
print(ziplist)

# 2. Zipping two iterators to make a dictionary

lakes = ['Victoria', 'Baikal', 'Huron']
Ocean = ['Pacific', 'Artic', 'Indian']

result = zip(lakes, Ocean)
zipdict1 = dict(result)

print(zipdict1)

