print('============= PERMUTATIONS =================')
# A Python program to print all 
# permutations using library function 
from itertools import permutations 
  
  
# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 
for i in list(perm): 
    print (i) 

print('============= PERMUTATIONS =================')
# A Python program to print all 
# permutations of given length 
from itertools import permutations 
  
# Get all permutations of length 2 
# and length 2 
perm = permutations([1, 2, 3], 2) 
  
# Print the obtained permutations 
for i in list(perm): 
    print (i) 

print('============= COMBINATION =================')
# A Python program to print all 
# combinations of given length
from itertools import combinations
  
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)
  
# Print the obtained combinations
for i in list(comb):
    print (i)

print('============= COMBINATION WITH REPLACEMENT =================')
# A Python program to print all combinations 
# with an element-to-itself combination is 
# also included 
from itertools import combinations_with_replacement 
  
# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement([1, 2, 3], 2) 
  
# Print the obtained combinations 
for i in list(comb): 
    print (i) 