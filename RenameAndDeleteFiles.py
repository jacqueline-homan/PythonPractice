#!/usr/bin/python3
import os

# Python's os module provides methods that help with file processing
# operations, such as renaming and deleting files.

fo = open("test1.txt", "w")
fo.write("Now for more cool stuff...\n")

# Close the file
fo.close()

# Re-open the file created and read from it
fo = open("test1.txt", "r+")
str = fo.read()
print(" ", str)
fo.close()

# Renaming the file
os.rename("test1.txt", "test2.txt")

# Copying the contents of one file to another file
os.popen('cp test2.txt oops.txt')