# https://stackoverflow.com/questions/61048297/google-codejam-2020-qualification-round-problem-3 

num_test_cases = int(input())


def notOverlap(activity, arr):
    # returns true if we have no overlapping activity in arr
    for act in arr:
        if not (act[0] >= activity[1] or act[1] <= activity[0]):
            return False
    return True


def decide(act, num_act):
    C, J = [], []
    result = [None]*num_act
    for i in range(num_act):
        if notOverlap(act[i], C):
            C.append(act[i])
            result[i] = "C"
        elif notOverlap(act[i], J):
            J.append(act[i])
            result[i] = "J"
        else:
            return "IMPOSSIBLE"
    return "".join(result)

for testcasei in range(1, 1 + int(input())):
    n = int(input())
    acts = []
    for index in range(n):
        start, end = map(int, input().split())
        acts.append((start, end, index)) # store also the index

    acts.sort(reverse=True) # sort by starting time reversed
    # so the first activity go to the last

    d = ['']*n # construct the array for the answer
    cnow = jnow = 0 # next time C or J are available
    impossible = False # not impossible for now

    while acts: # while there is an activity
        start_time, end_time, index = acts.pop()
        if cnow <= start_time: # C is available to do the activity
            cnow = end_time
            d[index] = 'C'
        elif jnow <= start_time:
            jnow = end_time
            d[index] = 'J'
        else: # both are'nt available
            impossible = True
            break

    if impossible:
        d = 'IMPOSSIBLE'
    else:
        d = ''.join(d) # convert the array to string
    print("Case #%d: %s" % (testcasei, d))

