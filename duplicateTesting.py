# https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU
import time

def timetrials(func, n, trials = 10):
    totaltime = 0
    #start = time.time()
    for i in range(trials):
        start = time.time() # it should be here
        func(list(range(n)))
        totaltime += time.time() - start
    print("average =%10.7f for n = %d" % (totaltime/trials, n))

def duplicates1(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i != j and L[i] == L[j]:
                return True
    return False

def duplicates2(L):
    n = len(L)
    for i in range(1,n):
        for j in range(i):
            if L[i] == L[j]:
                return True
    return False

def duplicates3(L):
    n = len(L)
    return any(L[i] == L[j] for i in range(1,n) for j in range(i))

assert(duplicates1([1,2,6,3,4,5,6,7,8]))
assert(not duplicates1([1,2,3,4]))

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates1, n)

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates2, n)

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates3, n)

def duplicates4(L):
    n = len(L)
    L.sort()
    for i in range(n-1):
        if L[i] == L[i+1]:
            return True
    return False

def duplicates5(L):
    n = len(L)
    L.sort()
    return any(L[i] == L[i+1] for i in range(n-1))

def duplicates6(L):
    s = set()
    for e in L:
        if e in s:
            return True
        s.add(e)
    return False

def duplicates7(L):
    return len(L) != len(set(L))

def duplicates8(L):
    s = set()
    return any(e in s or s.add(e) for e in L)

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    print("Quadratic: ", end="")
    timetrials(duplicates3, n)
    print("Sorting: ", end="")
    timetrials(duplicates5, n)
    print("Sets: ", end="")
    timetrials(duplicates7, n)
    print('--------------------------')

# Remove Duplicates and Keep the Order:
# https://blog.finxter.com/python-list-remove-duplicates-and-keep-the-order/
initial = [1, 1, 9, 1, 9, 6, 9, 7]
result = list(dict.fromkeys(initial))
result




