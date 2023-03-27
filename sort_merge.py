# https://www.geeksforgeeks.org/merge-sort/
# advantages of merge sort is that it has a time complexity of O(n log n)

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            print("i, j, k :", i, j, k)
            if L[i] <= R[j]:
                arr[k] = L[i]
                print("arr after adding L i into arr k : ", arr)
                i += 1
            else:
                arr[k] = R[j]
                print("arr after adding R j into arr k : ", arr)
                j += 1
            k += 1
            
  
        # Checking if any element was left
        while i < len(L):
            print("i, j, k :", i, j, k)
            arr[k] = L[i]
            print("arr after adding element L i into arr k : ", arr)
            i += 1
            k += 1
            
              
        while j < len(R):
            print("i, j, k :", i, j, k)
            arr[k] = R[j]
            print("arr after adding element R j into arr k : ", arr)
            j += 1
            k += 1
            
  
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        # print("just curious, i is: ", i)
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 5, 5, 0]
    print("Given array is", end="\n")
    # print("just trying normal print: ", arr)
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
  
# This code is contributed by Mayank Khanna

def sortMerge(array):
    if len(array) <= 1:
        return
    middle = len(array) // 2
    leftArray = array[:middle]
    print(leftArray)
    rightArray = array[middle:]
    print(rightArray)
    sortMerge(leftArray)
    sortMerge(rightArray)
    
    print('ARRAY is now: ', array)
    print('STARTING TO MERGE/SORT ARRAY: ')
    i = j = k = 0
    print('leftArray is: ', leftArray)
    print('rightArray is: ', rightArray)
    # setting smaller values to the left side of the array
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            print('i is now: ', i)
            array[k] = leftArray[i]
            i += 1
            print('array after adding left element is now: ', array)
        else: 
            print('j is now: ', j)
            array[k] = rightArray[j]
            j += 1
            print('array after adding right element is now: ', array)
        print('k is now: ', k)
        k += 1

    # setting the rest/larger values to the right side of the array
    while i < len(leftArray):
        print('i is now: ', i)
        array[k] = leftArray[i]
        i += 1
        print('array with leftover on the left is now: ', array)
        print('k is now: ', k)
        k += 1

    # setting the rest/larger values to the right side of the array
    while j < len(rightArray):
        print('j is now: ', j)
        array[k] = rightArray[j]
        j += 1
        print('array with leftover on the right is now: ', array)
        print('k is now: ', k)
        k += 1

arr = [12, 11, 13, 5, 6, 7, 5, 5, 0]
print('arr BEFORE: ', arr)
sortMerge(arr)
print('arr AFTER: ', arr)
