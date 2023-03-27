# https://www.geeksforgeeks.org/replace-every-array-element-with-maximum-of-k-next-and-k-previous-elements/?ref=rp

def maxK(arr, K):
    tmpArr = [ ]*len(arr) # https://www.geeksforgeeks.org/python-initialize-empty-array-of-given-length/
    print(tmpArr)
    for i in range(0, len(arr)):
        print('i is now: ', i)
        if (i >= K) and (i < (len(arr) - K)):
            tmpMax = 0
            print('tmpMax is now: ', tmpMax)                
            for j in range(i - K, i):
                if arr[j] > tmpMax:
                    tmpMax = arr[j]
                    print('On the left - tmpMax is: ', tmpMax)

            for j in range(i + 1, i + K + 1):
                if arr[j] > tmpMax:
                    tmpMax = arr[j]  
                    print('On the right - tmpMax is: ', tmpMax)              
            tmpArr[i] = tmpMax
        elif i < K:
            tmpMax = 0
            print('tmpMax is now: ', tmpMax)                
            for j in range(0, i):
                print('arr j in the left is: ', arr[j])
                if arr[j] > tmpMax:
                    tmpMax = arr[j]
                    print('On the left - tmpMax is: ', tmpMax)

            for j in range(i + 1, i + K + 1):
                print('arr j on the right is: ', arr[j])
                if arr[j] > tmpMax:
                    tmpMax = arr[j]  
                    print('On the right - tmpMax is: ', tmpMax)              
            tmpArr[i] = tmpMax
        else: 
            tmpMax = 0
            print('tmpMax is now: ', tmpMax)                
            for j in range(i - K, i):
                if arr[j] > tmpMax:
                    tmpMax = arr[j]
                    print('On the left - tmpMax is: ', tmpMax)

            for j in range(i + 1, len(arr)):
                if arr[j] > tmpMax:
                    tmpMax = arr[j]  
                    print('On the right - tmpMax is: ', tmpMax)              
            tmpArr[i] = tmpMax

    return  tmpArr

def betterMaxK(arr, K):
    tmpArr = []
    for i in range(len(arr)):
        start = max(0, (i - K))
        end = min((i + K + 1), len(arr))

        tmpMax = float('-inf')
        for j in range(start, end):
            if i == j:
                continue
            print(f"i is {i} and j is {j}")
            tmpMax = max(arr[j], tmpMax)
            print('tmpMax is: ', tmpMax)

        tmpArr.append(tmpMax)
    return tmpArr

if __name__ == '__main__':
    print(betterMaxK([12, 5, 3, 9, 21, 36, 17], 2))
    # Input: arr[] = {12, 5, 3, 9, 21, 36, 17}, K=2
    # Expected Output: 5 12 21 36 36 21 36

    print(betterMaxK([13, 21, 19], 1))
    # Input: arr[] = { 13, 21, 19}, K=1
    # Expected Output: 21, 19, 21 

    print(betterMaxK([-13, -21, 19], 1))
    # Output