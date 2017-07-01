# using raw_input() to get the filename
filename = raw_input("Enter the file to be opened: ")

# opening the file ex15_sample.txt using the open() function
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read() # printing the contents read from the txt file ex15_sample.txt
txt.close() # closing the file filename (ex15_sample.txt)

print "Type the filename again:"
file_again = raw_input("> ") # getting the filename again

# again opening the file file_again (ex15_sample.txt)
txt_again = open(file_again)

# again printing the contents of the file
print txt_again.read()
txt.close() # closing the file file_again (ex15_sample.txt)
