print("hello!")

# put unsafe operation in try block
try:
     print("code start")
          
     # unsafe operation perform
     print(1 / 0)
  
# if error occur the it goes in except block
except:
     print("an error occurs")
  
# final code in finally block
finally:
     print("GeeksForGeeks")

# try for unsafe code
try:
    amount = 1999
    if amount < 2999:
          
        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")
              
# if false then raise the value error
except ValueError as e:
        print(e)

# https://leetcode.com/problems/find-pivot-index/
def PilotIndex(array):
     print(sum(array[:]))

     if (1 <= len(array) <= 10^4):
          for i in range(len(array)):
               if (-1000 <= array[i] <= 1000):
                    if sum(array[:i]) == sum(array[i+1:]):
                         print(f'pilot index is {i}; content is {array[i]}')
                         return i
                    else:
                         print(f"location {i} this is not pilot index")
                         
     return -1

array = [13, 2002, 3, 4, 5, 2006]
print(array)
print("array at location -1 is: ", array[-1])
print("array at location -2 is: ", array[-2])
print("array at location -3 is: ", array[-3])
print("array at location -4 is: ", array[-4])
print("array at location -5 is: ", array[-5])
print("array at location -6 is: ", array[-6])
arr = PilotIndex(array)
print(f'PILOT INDEX is {arr}')