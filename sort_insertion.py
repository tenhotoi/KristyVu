# Function to do insertion sort
# Time Complexity: O(N^2) 
# Auxiliary Space: O(1)
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
         
# Driver code to test above
arr = [12, 11, 13, 5, 6]
print(arr)
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 
# running worst case running time of O(n^2) 
# This code is contributed by Mohit Kumra
# https://www.geeksforgeeks.org/insertion-sort/