def countingSort(vec, n):
    #for (int i = 0; i<n; cin>> vec[i], i++)
    count=dict();
     
    # Here we are initializing every element of count to 0
    # from 1 to n
    for i in range(0,n):
        count[i] = 0;
         
    # Here we are storing count of every element
    for i in range(0,n):
        if vec[i] in count.keys():
            count[vec[i]] += 1;
        else:
            count[vec[i]] = 1;
 
         
    sortedArr = [];
    i = 0;
    while (n > 0):
        # Here we are checking if the count[element] = 0
        # then incrementing for the next Element
        if (count[i] == 0) :
            i += 1;
         
        # Here we are inserting the element into the
        # sortedArr decrementing count[element] and n by 1
        else:
            sortedArr.append(i);
            count[i] -= 1;
            n = n - 1;
         
    return sortedArr;
 
 
def printArr(vec, n):
    print("Sorted Array: ");
    for i in range(0,n):
        print(vec[i], " ");
 
vec1 = [ 6, 0, 7, 8, 7, 2, 0 ];
sortedArr1 = countingSort(vec1, len(vec1));
printArr(sortedArr1, len(sortedArr1));
 
vec2 = [ 4, 8, 1, 0, 1, 1, 0, 0 ];
sortedArr2 = countingSort(vec2, len(vec2));
printArr(sortedArr2, len(sortedArr2));
 
# This code is contributed by ritaagarwal.