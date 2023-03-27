# https://www.geeksforgeeks.org/count-array-elements-exceeding-all-previous-elements-as-well-as-the-next-array-element/?ref=rp

"""
Given an array arr[], the task is to find the count of array elements satisfying the following conditions:

The array elements should be strictly greater than all the previously occurring array elements.
Either it is the last array element or the integer should be strictly larger than the next array element.
Note: The first integer of the array can also be considered.

Examples:

Input: arr[] = {1, 2, 0, 7, 2, 0, 2, 0}
Output: 2
Explanation: arr[1] (= 2) and arr[3] ( = 7) are the array elements satisfying the given condition.

Input: arr[] = {4, 8, 15, 16, 23, 42}
Output: 1

"""

# Python program for the above approach
 
# Function to count array elements
# satisfying the given condition
def numberOfIntegers(arr, N) :  
    cur_max = 0
    count = 0
 
    # If there is only one
    # array element
    if (N == 1) :
        count = 1   
    else :
 
        # Traverse the array
        for i in range(N - 1):
 
            # Update the maximum element
            # encountered so far
            if (arr[i] > cur_max) :
                cur_max = arr[i]
 
                # Count the number of array elements
                # strictly greater than all previous
                # and immediately next elements
                if (arr[i] > arr[i + 1]) :
                    count += 1                  
        if (arr[N - 1] > cur_max) :
            count += 1
     
    # Print the count
    print(count)
 
def kristy_solution(arr): 
    if len(arr) == 1:
        return 1
    
    sol = []
    count = 0
    tmpMax = float('-inf')
    for i in range(len(arr) - 1):
        if (arr[i] > tmpMax):
            if(arr[i] > arr[i + 1]):
                tmpMax = arr[i]
                print(f"arr[i] is {arr[i]} and tmpMax is {tmpMax}, arr[i+1] is {arr[i+1]}")
                sol.append(arr[i])
                count += 1
    if(arr[len(arr) - 1] > tmpMax):
        sol.append(arr[i])
        count += 1
    print(sol)
    return count    




# Driver Code
if __name__ == "__main__":
    # Given array
    arr = [ 1, 2, 0, 7, 2, 0, 2, 0 ]
    # arr = [3]
    
    # Size of the array
    N = len(arr)
    numberOfIntegers(arr, N)
    print(sol := kristy_solution(arr))
    
    # This code is contributed by sanjoy_62.

    """
    Output: 
    2
    """

