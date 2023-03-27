# https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
# https://www.geeksforgeeks.org/writing-to-file-in-python/

# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and
file1 = open("testfile.txt", "r")
   
# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"C:\Users\tenho\OneDrive\Desktop\INTERVIEW\testing.txt", "r+")

file1.close()
file2.close()

# Program to show various ways to
# read data from a file.
 
# Creating a file
file1 = open("testfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes
 
file1 = open("myfile.txt", "r+")
 
print("Output of Read function is ")
print(file1.read())
print()
 
# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)
 
print("Output of Readline function is ")
print(file1.readline())
print()
 
file1.seek(0)
 
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
 
file1.seek(0)
 
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
 
file1.seek(0)
 
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

# Program to show various ways to
# read data from a file.
 
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Creating a file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes
 
with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())

# https://www.pragmaticlinux.com/2022/04/read-a-file-line-by-line-using-python/
def main1():
    # Opening the source file in read-only mode
    source_file = open('testfile.txt', 'r')
    # Loop through the file one line at a time
    for line in source_file:
        # Display the line on the standard output
        print(line.rstrip())
    # Close the source file
    source_file.close()

def main2():
    # Opening the source file in read-only mode
    source_file = open('testfile.txt', 'r')
    # Opening the destination for in write mode
    destination_file = open('newfile.txt', 'w')
    # Loop through the file one line at a time
    for line in source_file:
        # Store the line in the destination file
        destination_file.write(line)
    # Close the destination file
    destination_file.close()
    # Close the source file
    source_file.close()

# https://www.tutorialspoint.com/How-to-merge-multiple-files-into-a-new-file-using-Python
"""
Example - 1
Following is an example to merge multiple files nto a single file using for loop −
"""
import os
nameOfFiles = ["testfile", "myfile.txt", "testfile.txt"]
if not os.path.isfile('test.txt'):
    with open("test.txt", "w") as new_created_file:
        for name in nameOfFiles:
            try:
                with open(name) as file:
                    for line in file:
                        new_created_file.write(line)
                        
                    new_created_file.write("\n")
            except IOError as io:
                print(io)
else:
    print('Please try another file name since this file this file already exist')

"""
Example - 2
In the following code we opened the existing file in read mode and the new created file i.e. advanced_file in write mode. After that we read the that frm both the files and added it in a string and wrote the data from string to the new created file. Finally, closed the files −
"""
info1 = info2 = ""
# Reading information from the first file
try:
    with open('testfile') as file:
        info1 = file.read()
except IOError as io:
    print(io)

# Reading information from the second file
try:
    with open('testfile.txt') as file:
        info2 = file.read()
except IOError as io:
    print(io)

# Merge two files for adding the data of first file from next lin
info1 += "\n"
info1 += info2

if not os.path.isfile('myfile.txt'):
    with open ('myfile.txt', 'w') as file:
        file.write(info1)
else:
    print('Please try another file name since this file already exists.')

"""
https://www.tutorialspoint.com/How-to-copy-files-to-a-new-directory-using-Python
The shutil module provides functions for copying files, as well as entire folders. For copying multiple files at once, you'll have to have a list of all files you want to copy and loop over them to copy them.
Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. (Both source and destination are strings.) If destination is a filename, it will be used as the new name of the copied file. This function returns a string of the path of the copied file. For example,
"""
import shutil, os
files = ['test.txt', 'testfile', 'testfile.txt']

if not os.path.exists('my_new_folder'):
    os.mkdir('my_new_folder')

for f in files:
    try:
        shutil.copy(f, 'my_new_folder')
    except IOError as io:
        print(io)
    
"""
If you have a list of files you want to rename and corresponding new file name, You can use os module's rename method.

https://www.tutorialspoint.com/How-to-rename-multiple-files-in-a-directory-in-Python
For example
"""
import os

files = {'test.txt': 'testing.txt', 'testfile': 'testfile.txt'}
for old, new in files.items(): # files.items() in Python 3
    if not os.path.isfile(new):
        os.rename(old, new)
    else: 
        print(new, ': this file already exist.  Please use another name for new file.')

"""
You can also use the shutil (or shell utilities) module. Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.
For example
"""
import shutil
for old, new in files.items(): # files.items() in Python 3
    try:
        shutil.move(old, new)
    except IOError as io:
        print(io)

# How to rename multiple files recursively using Python?
# https://www.tutorialspoint.com/How-to-rename-multiple-files-recursively-using-Python
import os
def replace(folder_path, old, new):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if(old.lower() in name.lower()):
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,name.lower().replace(old,new))
                os.rename(file_path, new_name)


# https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and
file1 = open("MyFile.txt", "r")
   
# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2
# file2 = open(r"D:\Text\MyFile2.txt", "r+")


# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt", "r")
file1.close()

# Program to show various ways to
# read data from a file.
 
# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes
 
file1 = open("myfile.txt", "r+")
 
print("Output of Read function is ")
print(file1.read())
print()
 
# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)
 
print("Output of Readline function is ")
print(file1.readline())
print()
 
file1.seek(0)
 
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
 
file1.seek(0)
 
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
 
file1.seek(0)
 
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

# Program to show various ways to
# read data from a file.
 
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Creating a file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes
 
with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())

# https://media.licdn.com/dms/document/C561FAQEJx0ldqomlFg/feedshare-document-pdf-analyzed/0/1678350857950?e=1679529600&v=beta&t=e6OTy2CQhrOZ5M_VSeATiBV5sJBiZUUiyeIM92qqzs0

filename = 'myfileNONE.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print('SHOW CONTENTS WITHIN try: ', contents)

        for line in f_obj:
            print(line.rstrip())
except IOError as io:
    print(io)

if not os.path.isfile(filename):
    with open(filename, 'w') as f:
        f.write("I love programming!")
else:
    print("File already exists. Please try another name.")

with open(filename, 'w') as f:
    f.write("I love programming very much!")

with open('nonexistain.txt', 'a') as f: 
    f.write("\nTesting file append: I love programming very much!")

try:
    with open(filename, 'x') as f:
        f.write("TESTING x OPTION WHEN OPENING FILE.")
except IOError as io:
    print(io, "Please try another name.")
    with open(filename, 'a') as f:
        f.write("\nTesting file append again, within exception: I love programming very much!")

# https://www.makeuseof.com/check-if-a-file-exists-using-python/

try:
    f = open('testfileNOTEXIST.txt')
    print("File is available for use")
    f.close()
except IOError as io:
    print(io, "\nFile is not accessible. Please check again.")

# Check if file exist or not: os.path.isfile(path)
"""
os.path.isfile()
os.path.isdir()
os.path.exists()
"""
# https://www.pythonpool.com/ioerror-errno-2-no-such-file-or-directory-solved/
import os

path_name = "filename.txt"
 
if os.path.isfile(path_name):
  print("File exists")
  f = open(path_name)
  #Execute other file operations here
  f.close()
else:
  print("File does not exist! IOError has occured")

# https://www.w3schools.com/python/python_file_handling.asp
"""
File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.

"""
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
try:
    os.remove("weirdname.txt")
except IOError as io:
    print(io)

# Check if File exist:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Delete Folder
# Note: You can only remove empty folders.
import os
try:
    os.rmdir("my_new_folder")
except IOError as io:
    print(io)

"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

with open('nonexistain.txt', 'a+') as f: 
    f.seek(0)
    print(f.read())    
    f.write("\nTesting file append after f seek 0: I love programming very much!")
    f.seek(0)
    print(f.read()) 
    f.close()

with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print("\nRead file with r+ BEFORE writing: ", file1.read())
    file1.write("\nTesting r+ : I love programming very much!")
    file1.seek(0)
    print('Read file with r+ AFTER writing: ', file1.read())
    file1.close()

with open('nonexistain.txt', 'w+') as f: 
    print("\nRead file with w+ BEFORE writing: ", f.read())    
    f.write("\nTesting w+ : I love programming very much!")
    f.seek(0)
    print("\nRead file with w+ AFTER writing: ", f.read()) 
    f.close()

# https://www.makeuseof.com/check-if-a-file-exists-using-python/
# 8 Ways to Check if a File Exists Using Python

# Handling the FileNotFoundError exception
f_name = 'siddhartha.txt'
try:
    with open(f_name) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    print("Can't find file {}.".format(f_name))
    print(msg := "Can't find file {0}.".format(f_name))
    print(msg)

f_path = "my_new_folder/test.txt"
with open(f_path) as f_obj:
    lines = f_obj.readlines()
for line in lines:
    print(line.rstrip())

for line in open(f_path).readlines():
    print(line.rstrip())
"""
Output:
Hello
This is Delhi
This is Paris
This is London

Hello
This is Delhi
This is Paris
This is London
"""

print(open(f_path).readlines())
"""
Output:
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n', '\n', 'Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n', '\n']
"""

"""
https://docs.python.org/3/tutorial/inputoutput.html

Warning: Calling f.write() without using the with keyword or calling f.close() 
might result in the arguments of f.write() not being completely written to the disk, 
even if the program exits successfully.
"""

import json
import re

# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4, 'CS' : 5}

with open('eye.txt', 'a+', encoding='utf-8') as f:
    json.dump(test_dict, f)
    # f.write(f'{test_dict}')  # <====== doesn't work
    # f.seek(0)
    # print('CONTENTS FROM READ(): ', f.read())
    # f.seek(0)
    # print('CONTENTS FROM READLINES(): ', f.readlines())
    # f.seek(0)
    # f.readlines()
    value = ('testing tuple', 42)
    f.write(f'\n{str(value)}')   # s = str(value)  # convert the tuple to string
    value = ['testing list', 42]
    f.write(f'\n{str(value)}')
    # json.dump(value,f)  # <====== doesn't work
    f.seek(0)
    contents = f.readlines()
    #contents = f.read().splitlines()
    print('CONTENTS FROM READ(): ', contents)
    # f.seek(0)
    # print(list(f))
    last = contents[-1].strip()
    second_last = contents[-2].strip()
    print(f'checking the last value {last} which of type {type(last)} when obtained from the file')
    print('checking the last value {0} is of type {1} after eval(), where the key is \'{0[0]}\' and value is {0[1]}.'.format(eval(last), type(eval(last))))

    print(f'checking the second last value {second_last} which of type {type(second_last)} when obtained from the file')
    print('checking the second last value {0} is of type {1} after eval(), where the key is \'{0[0]}\' and value is {0[1]}.'.format(eval(second_last), type(eval(second_last)))) 
    # for each in contents:
    #    print(f'testing {each}')
    """
    Output:
    
    checking the last value ['testing list', 42] which of type <class 'str'> when obtained from the file
    checking the last value ['testing list', 42] is of type <class 'list'> after eval(), where the key is 'testing list' and value is 42.
    checking the second last value ('testing tuple', 42) which of type <class 'str'> when obtained from the file
    checking the second last value ('testing tuple', 42) is of type <class 'tuple'> after eval(), where the key is 'testing tuple' and value is 42.
    """

    # https://docs.python.org/3/tutorial/inputoutput.html

