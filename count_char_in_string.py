# https://www.makeuseof.com/count-the-occurrences-of-character-in-string/

# Python program to count occurrences
# of a given character in a string

from collections import Counter

# Function to count the occurrences of
# the given character in the string
def countOccurrences(str, ch):
# Counter variable
    countNum = 0

    for char in str:
        # check if the given character matches
        # with the character in the string
        if char == ch:
        # if the given character matches with
        # the character in the string,
        # increment the counter variable
            countNum += 1
    
    return countNum

# Driver code
str1 = "she sells seashells by the seashore"
ch1 = 's'
print("Input string 1:", str1)
print("Character", ch1, "has occured",
countOccurrences(str1, ch1),"times in the given string.")

print(count := Counter(str1))
print(count[ch1])
print(set(str1))
print(list(dict.fromkeys(str1)))

str2 = "peter piper picked a peck of pickled peppers"
ch2 = 'p'
print("Input string 2:", str2)
print("Character", ch2, "has occured",
countOccurrences(str2, ch2),"times in the given string.")

str3 = "I saw Susie sitting in a shoeshine shop"
ch3 = 'a'
print("Input string 3:", str3)
print("Character", ch3, "has occured",
countOccurrences(str3, ch3),"times in the given string.")

str4 = "Near an ear, a nearer ear, a nearly eerie ear"
ch4 = 'r'
print("Input string 4:", str4)
print("Character", ch4, "has occured",
countOccurrences(str4, ch4),"times in the given string.")

str5 = "He threw three free throws"
ch5 = 'e'
print("Input string 5:", str5)
print("Character", ch5, "has occured",
countOccurrences(str5, ch5),"times in the given string.")

"""
Output:

Input string 1: she sells seashells by the seashore
Character s has occured 8 times in the given string.
Counter({'s': 8, 'e': 7, ' ': 5, 'h': 4, 'l': 4, 'a': 2, 'b': 1, 'y': 1, 't': 1, 'o': 1, 'r': 1})
8
Input string 2: peter piper picked a peck of pickled peppers
Character p has occured 9 times in the given string.
Input string 3: I saw Susie sitting in a shoeshine shop
Character a has occured 2 times in the given string.
Input string 4: Near an ear, a nearer ear, a nearly eerie ear
Character r has occured 8 times in the given string.
Input string 5: He threw three free throws
Character e has occured 6 times in the given string.
"""