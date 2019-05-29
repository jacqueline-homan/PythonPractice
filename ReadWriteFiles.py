#!/usr/bin/python3

# Create and open a text file and write to it
fo = open("sample.txt", "w")
fo.write("My first text file R/W program in Python.\nThis is cool!\n")

# Close the file
fo.close()

# Re-open the file created and read from it
fo = open("sample.txt", "r+")

# Read the first 36 characters in the file
str = fo.read(36)
print ("Reading String is: ", str)

# Check current position in file
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning 
position = fo.seek(0, 0)
str = fo.read(10)
print("Again, read String is: ", str)

# Close the file
fo.close()

fo = open("sample.txt", "r+")
str = fo.read()
print("Now reading string is: ", str)
fo.close()