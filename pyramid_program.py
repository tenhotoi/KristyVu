# https://www.javatpoint.com/pyramid-programs-in-vb
# https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
# https://www.w3schools.in/python/examples/print-half-pyramid-using-alphabets

# Python 3.x code to demonstrate star pattern
  
# Function to demonstrate printing pattern
def pypart(n):
      
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
      
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
          
            # printing stars
            print("* ",end="")
       
        # ending line after each row
        print("\r")
  
# Driver Code
n = 5
pypart(n)
# Time Complexity: O(n2),This algorithm has a time complexity of O(n2). 

# Python 3.x code to demonstrate star pattern
  
# Function to demonstrate printing pattern
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
  
# Driver Code
n = 5
pypart(n)
# Time Complexity: O(n) 

#python3 code to print pyramid pattern using recursion
def pypart(n):
    if n==0:
        return
    else:
        pypart(n-1)
        print("* "*n)
   
# Driver Code
n = 5
pypart(n)

# python3 code to print pyramid pattern using while loop
  
# input
n=5 
  
i=1;j=0
# while loop check the condition until the
# condition become false. if it is true then 
# enter in to loop and print the pattern
while(i<=n):
    while(j<=i-1):
        print("* ",end="") 
        j+=1 
     # printing next line for each row
    print("\r") 
    j=0;i+=1 

# After 180 degrees rotation
# Python 3.x code to demonstrate star pattern  
# Function to demonstrate printing pattern
def pypart2(n):
      
    # number of spaces
    k = 2*n - 2
  
    # outer loop to handle number of rows
    for i in range(0, n):
      
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
      
        # decrementing k after each loop
        k = k - 2
      
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
          
            # printing stars
            print("* ", end="")
      
        # ending line after each row
        print("\r")
  
# Driver Code
n = 5
pypart2(n)

"""
* 
* *
* * *
* * * *
* * * * *
*
**
***
****
*****
*
* *
* * *
* * * *
* * * * *
*
* *
* * *
* * * *
* * * * *
        *
      * *
    * * *
  * * * *
* * * * *
"""

def paramid():
    for i in range(n):
        print((f'{i + 1} '*(i+1)).rjust(length))

    """
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
    """

    for i in range(n):
        # print(' '.join([str((j + 1)) for j in range(i + 1)]))
        print((' '.join([str((j + 1)) for j in range(i + 1)])).ljust(length))

    """
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """

    for i in range(n):
        # print(' '.join([str((j + 1)) for j in range(i + 1)]))
        print((' '.join([str((j + 1)) for j in reversed(range(i + 1))])).rjust(length))

    """
    1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1
    """

    for i in range(n):
        # print(' '.join([str((j + 1)) for j in range(i + 1)]))
        str1 = ' '.join([str((j + 1)) for j in range((i + 2) // 2)])
        str2 = ' '.join([str((j + 1)) for j in reversed(range((i + 1) // 2))])
        print((str1 + ' ' + str2).center(length_double))
        # print()
        # print((' '.join([str((j + 1)) for j in reversed(range(i // 2))])).center(2*n))

    """
    1
    1 1
    1 2 1
    1 2 2 1
    1 2 3 2 1
    """

    for i in range(n):
        print((f'{chr(65 + i)} '*(i+1)).center(length_double))

    """
    A
   B B
  C C C
 D D D D
E E E E E
    """

    for i in reversed(range(n)):
        print((' '.join([f'{chr(65 + j)} ' for j in reversed(range(i + 1))])).rjust(length))

    """
 E  D  C  B  A
    D  C  B  A
       C  B  A
          B  A
             A
    """

    for i in reversed(range(n)):
        print((' '. join(f'{chr(65 + j)} ' for j in range(i + 1))).rjust(length))

    """
 A  B  C  D  E
    A  B  C  D
       A  B  C
          A  B
             A
    """

    for i in range(n):
        str1 = ' '.join([f'{chr(65 + j)}' for j in range((i + 2) // 2)])
        str2 = ' '.join([f'{chr(65 + j)}' for j in reversed(range((i + 1) // 2))])
        print((str1 + ' ' + str2).center(length_double))

    """ 
    A
   A A
  A B A
 A B B A
A B C B A
    """

    for i in reversed(range(n)):
        str1 = ' '.join([f'{chr(65 + j)}' for j in range((i + 2) // 2)])
        str2 = ' '.join([f'{chr(65 + j)}' for j in reversed(range((i + 1) // 2))])
        print((str1 + ' ' + str2).center(length_double))

    """
A B C B A
 A B B A
  A B A
   A A
    A
    """

    for i in range(n):
        str1 = ' '.join([f'{chr(65 + j)}' for j in range((i + 2) // 2)])
        str2 = ' '.join([f'{chr(65 + j)}' for j in reversed(range((i + 1) // 2))])
        print((str1 + ' ' + str2).center(length_double))

    """
    A
   A A
  A B A
 A B B A
A B C B A
    """

    x = 1
    for i in range(n):
        print(' '.join(f'{x + j}' for j in range(i + 1)))
        x += i + 1

    """
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """

    x = 1
    for i in range(n):
        print((' '.join(f'{x + j}' for j in range(i + 1))).rjust(length))
        x += i + 1
    
    """
              1
            2 3
          4 5 6
       7 8 9 10
 11 12 13 14 15    
    """

    x = 1
    for i in range(n):
        print((' '.join(f'{x + j}' for j in range(i + 1))).center(length_double))
        x += i + 1
    
    """
       1
     12 13
    24 25 26
  37 38 39 40
 51 52 53 54 55    
    """

if __name__ == '__main__':
    while True:
        print("Range number should be greater than 1 and less than 27.")
        n = input("Please enter range number (enter 'q' to quit): ")
        # print(length := len([*n]))

        if n.lower() == 'q':
            print("Existing...")
            break    
        elif not n.isdigit():
            print("Invalid input. Please try again.")        
        else:
            digitNum = len([*n])
            n = int(n)

            length = n*(digitNum + 2)  # plus 1 for each space after each entry
            length_double = n*(digitNum + 2)  # plus 1 for each space after each entry
            if n <= 1 or n > 26:
                print("Range number should be greater than 1 and less than 27. Please try again.")
            else:
                paramid()