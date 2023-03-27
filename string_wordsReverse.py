def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

def my_function2(x):
  return list(reversed(x))

mytxt = my_function2("I wonder how this text looks like backwards")

print(mytxt)
print(''.join(mytxt[::-1]))

# Python code
# To reverse words in a given string
 
print('==================================== METHOD 1 ===================================')
# input string
string = "geeks quiz practice code"
print(string)
# reversing words in a given string
s = string.split()[::-1]
print(s)
l = []
for i in s:
    # apending reversed words to l
    l.append(i)
# printing reverse words
print(l)
print(" ".join(l))

print('==================================== METHOD 2 ===================================')
# Function to reverse words of string
 
def rev_sentence(sentence):
 
    # first split the string into words
    words = sentence.split(' ')
    print(words)
 
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
    print(reverse_sentence)
 
    # finally return the joined string
    return reverse_sentence
 
if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print (rev_sentence(input))

print('==================================== METHOD 3 ===================================')
# Function to reverse words of string
import re
def rev_sentence(sentence):
 
    # find all the words in sentence
    words = re.findall('\w+', sentence)
 
    # Backward iterate over list of words and join using space
    reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
 
    # finally return the joined string
    return reverse_sentence
 
if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print (rev_sentence(input))

# https://www.geeksforgeeks.org/reverse-words-given-string-python/

print('==================================== METHOD 4 ===================================')
# initializing string
string = "geeks quiz practice code"
 
# creating an empty stack
stack = []
 
# pushing words onto the stack
for word in string.split():
    stack.append(word)
    
print(stack)
 
# creating an empty list to store the reversed words
reversed_words = []
 
# popping words off the stack and appending them to the list
while stack:
    reversed_words.append(stack.pop())

print(reversed_words)

# joining the reversed words with a space
reversed_string = " ".join(reversed_words)
 
# printing the reversed string
print(reversed_string)
 
#This code is contributed by Edula Vinay Kumar Reddy

print('==================================== MY METHOD ===================================')

string = "geeks quiz practice code"
print(string)
print(''.join(string[::-1]))
# reversing words in a given string
print(" ".join(string.split()[::-1]))

print(string.split()[::-1])
words = string.split()[::-1]
for word in words:
    print('Word count for word', word, 'is', words.count(word))

print('Number of words in reverse string is: ', len(string.split()[::-1]))

from collections import Counter
print(Counter(string.split()[::-1]))



