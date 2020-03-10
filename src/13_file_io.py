"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('src/foo.txt') as f:
    print(f.read())
print(f.closed)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('src/bar.txt', 'w+') as f:
    f.write("Fubar was a bar in Orlando that allowed underage drinking\r\n")
    f.write("Significantly different words were used to describe it's meaning \r\n")
    f.write("it has since been demolished and turned into a parking lot for new condos\r\n")
print(f.closed)

with open('src/bar.txt') as f:
    print(f.read())
print(f.closed)