# https://medium.com/@sarperismetmakas/pythons-counter-efficient-data-counting-a77b168f4c8 

from collections import Counter

my_list = [1, 2, 3, 2, 1, 2, 3, 1, 1, 2]
my_counter = Counter(my_list)

print(my_counter)

my_string = "Python is awesome"
my_counter = Counter(my_string)
print(my_counter)

most_common = my_counter.most_common(2)
print(most_common)

my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = [2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6]
counter1 = Counter(my_list1)
counter2 = Counter(my_list2)
print(counter1 + counter2)

