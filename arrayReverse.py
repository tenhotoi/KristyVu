# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

# Python program for reversal algorithm of array rotation
 
# Function to reverse arr[] from index start to end
 
 
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
 
# Function to left rotate arr[] of size n by d
 
 
def leftRotate(arr, d):
 
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is
    # greater than array length
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
 
# Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i],end=' ')
    print('\n')

# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
 
leftRotate(arr, d)  # Rotate array by 2
printArray(arr)

 
"""
Output
3 4 5 6 7 1 2 
Time Complexity: O(N)
Auxiliary Space: O(1)

Another Method :-  Using C++ STL  reverse
"""
# Function to rotate an array by k elements to the right
def rotateArray(arr, k):
    # Find the size of the array
    n = len(arr)
 
    # Mod k with the size of the array
    # To handle the case where k is greater than the size of the array
    k %= n
 
    # Reverse the entire array
    arr[0:n] = arr[0:n][::-1]
 
    # Reverse the first k elements
    arr[0:k] = arr[0:k][::-1]
 
    # Reverse the remaining n-k elements
    arr[k:n] = arr[k:n][::-1]
 
# Initialize the array
arr = [ 1, 2, 3, 4, 5 ]

 
# Number of elements to rotate to the right
k = 2
 
# Call the rotateArray function to rotate the array
rotateArray(arr, k)
 
# Print the rotated array
for i in range(0,len(arr)):
    print(arr[i], end= " ")
print('\n')

arr = [1, 2, 3, 4, 5, 6, 7]
arr = arr[k:] + arr[0:k]
print(arr)

arr = [ 1, 2, 3, 4, 5 ]
arr = arr[len(arr) - k:] + arr[0:len(arr) - k]
print(arr)

def arrayReverse(array):
    i = 0
    j = len(array) - 1

    while (i < j):
        tmp = array[j]
        array[j] = array[i]
        array[i] = tmp
        i += 1
        j -= 1

    return arr

arr = [ 1, 2, 3, 4, 5 ]
arr = arrayReverse(arr)
print(arr)