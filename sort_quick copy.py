# https://www.geeksforgeeks.org/python-program-for-quicksort/

# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
# Time Complexity: Worst case time complexity is O(N2) and average case time complexity is O(N log N) Auxiliary Space: O(1)
 
# Function to find the partition position
def partition(array, low, high):
    print("low is: ", low, "high is: ", high)
    # choose the rightmost element as pivot
    pivot = array[high]
    print("pivot is: ", pivot)
 
    # pointer for greater element
    i = low
     
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            print(array)
            # Swapping element at i with element at j
            print("low is: ", low, "high is: ", high, "i is: ", i, "; j is: ", j)
            (array[i], array[j]) = (array[j], array[i])
            print("low is: ", low, "high is: ", high, "i is: ", i, "; j is: ", j)
            print(array)
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
    # Swap the pivot element with the greater element specified by i
    (array[i], array[high]) = (array[high], array[i])
    print("array before return pivot is: ", array)

    # Return the position from where partition is done
    print("returned partition is: ", i)
    return i
 
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        print("low is: ", low, " high is: ", high)
        pi = partition(array, low, high)
        print("low is: ", low, " high is: ", high)
        print("current partition is: ", pi)

        # Recursive call on the left of pivot
        print("quickSort low is: ", low, "quickSort pi - 1 is: ", pi - 1)
        quickSort(array, low, pi - 1)
        print("quickSort low is: ", low, "quickSort pi - 1 is: ", pi - 1)
        print(array)
 
        # Recursive call on the right of pivot
        print("quickSort pi + 1 is: ", pi + 1, "quickSort high is: ", high)
        quickSort(array, pi + 1, high)
        print("quickSort pi + 1 is: ", pi + 1, "quickSort high is: ", high)
        print(array)
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
print("size is: ", size)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

for a in range(0,len(data)):
    
    for b in range (a + 1, len(data)):
        if data[b] < data[a]:
            data[a],data[b] = data[b],data[a]

print(data)


