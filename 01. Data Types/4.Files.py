# Creating a variable based on an external file
myfile = open('notes.txt');
myfile.close();		# Closing a file once we’re done using it

# Using a file with no need to close it after we’re done, because it closes by itself
with open('notes.txt') as my_new_file:
	contents = my_new_file.read();

# Creating a text file 
%%writefile mynote.txt
Hello this is a text file
This is the second line
This is the third line

writing mynote.txt


# METHODS:
open()
read()
readlines()
seek()
close()


# refer to this
# https://www.geeksforgeeks.org/file-objects-python/