# https://realpython.com/lru-cache-python/

def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times.
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 2. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )

print(steps_to(4))          # 7
"""
from timeit import repeat
setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")


Here’s a line-by-line explanation of these additions:

Line 35 imports the name of steps_to() so that timeit.repeat() knows how to call it.
Line 36 prepares the call to the function with the stair number you want to reach, which in this case is 30. This is the statement that will be executed and timed.
Line 37 calls timeit.repeat() with the setup code and the statement. This will call the function 10 times, returning the number of seconds each execution took.
Line 38 identifies and prints the shortest time returned.
Note: A common misconception is that you should find the average time of each run of the function instead of selecting the shortest time.

Time measurements are noisy because the system runs other processes concurrently. The shortest time is always the least noisy, making it the best representation of the function’s runtime.
"""

"""
Note: In Python 3.8 and above, you can use the @lru_cache decorator without parentheses if you’re not specifying any parameters. 
In previous versions, you may need to include the parentheses: @lru_cache().

Remember, behind the scenes, the @lru_cache decorator stores the result of steps_to() for each different input. 
Every time the code calls the function with the same parameters, instead of computing an answer all over again, 
it returns the correct result directly from memory. This explains the massive improvement in performance when using @lru_cache.

determine all the different ways you can reach a specific stair in a staircase by hopping one, two, or three stairs at a time. 
How many paths are there to the fourth stair? Here are all the different combinations:
"""
from functools import lru_cache
from timeit import repeat

@lru_cache                  # CacheInfo(hits=52, misses=30, maxsize=128, currsize=30)
#@lru_cache(maxsize=16)     # CacheInfo(hits=52, misses=30, maxsize=16, currsize=16)
def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times.
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 2. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )

print(steps_to(30))             # 53798080
print(steps_to.cache_info())
"""
from timeit import repeat
setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")
"""
