# https://www.geeksforgeeks.org/shellsort/
# Python3 program for implementation of Shell Sort
# Python3 program for implementation of Shell Sort
  
def shellSort(arr, n):
    # code here
    gap=n//2
      
      
    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap # This will keep help in maintain gap value
              
            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i+gap]>arr[i]:
  
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
  
                i=i-gap # To check left side also
                            # If the element present is greater than current element 
            j+=1
        gap=gap//2
  
  
  
  
  
# driver to check the code
arr2 = [12, 34, 54, 2, 3]
print("input array:",arr2)
  
shellSort(arr2,len(arr2))
print("sorted array",arr2)
  
# This code is contributed by Illion
""" Worst Case Complexity
The worst-case complexity for shell sort is  O(n2)
Best Case Complexity
When the given array list is already sorted the total count of comparisons of each interval is equal to the size of the given array.
So best case complexity is Ω(n log(n))
Average Case Complexity

The shell sort Average Case Complexity depends on the interval selected by the programmer. 
θ(n log(n)2).

THE Average Case Complexity: O(n*log n)~O(n1.25)
Space Complexity
The space complexity of the shell sort is O(1).
"""