"""
Sets are similar to lists or dictionaries.
They are created using curly braces, and are unordered, which means that they can't be indexed.
Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, 
rather than part of a list.
"""
num_set = {1, 2, 3, 4, 5} 
print(3 in num_set)

"""
Sets cannot contain duplicate elements.
You can use the add() function to add new items to the set, and remove() to delete a specific element:
"""
nums = {1, 2, 1, 3, 1, 4, 5, 6} 
print(nums) 
nums.add(-7) 
nums.remove(3) 
print(nums)

"""
Duplicate elements will automatically get removed from the set.
The len() function can be used to return the number of elements of a set.
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
"""
first = {1, 2, 3, 4, 5, 6} 
second = {4, 5, 6, 7, 8, 9} 
print(first | second) 
print(first & second) 
print(first - second) 
print(second - first) 
print(first ^ second)
 
"""
Problem
You are working on a recruitment platform, which should match the available jobs and the candidates 
based on their skills.
The skills required for the job, and the candidate's skills are stored in sets.
Complete the program to output the matched skill.
You can use the intersect operator to get the values present in both sets.
"""
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(list(skills & job_skills)[0])