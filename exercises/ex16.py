# importing argv feature from sys module
from sys import argv

# giving filename (test.txt) before running the script
script, filename = argv

# telling the user that its going to erase the contents of the file (test.txt)
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

# taking input after the '?' prompt
raw_input("?")

print "Opening the file..."
# opeining the file in write mode and storing it in the file object 'target'
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()
# using truncate() function to erase the contents of the file via its object

print "Now I'm going to ask you for three lines."

# entering three lines one by one
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) # writing line1 into target (file)
target.write("\n") # writing a newline character at the end of line1
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() # closing te file
