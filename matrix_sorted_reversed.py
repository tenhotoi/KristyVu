# https://www.geeksforgeeks.org/python-reverse-row-sort-in-lists-of-list/

# Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using loop
 
# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Reverse Row sort in Lists of List
# using loop
res=[]
for ele in test_list:
    ele.sort()
    res.append(ele[::-1])
 
print(ele)
# printing result
print("The reverse sorted Matrix is : " + str(res))


"""
Output
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
Time Complexity: O(n log n)
Auxiliary Space: O(n)
"""
print([sorted(item, reverse=True) for item in test_list])
# [[6, 4, 1], [8, 7], [10, 8, 4]]