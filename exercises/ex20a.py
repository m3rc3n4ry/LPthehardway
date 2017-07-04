# import argv from sys
from sys import argv

# give names to two of the variables in argv namely argv[0] = script and
# argv[1] = input_file
script, input_file = argv

# define a function of the name print_all having one argument f which is a file
def print_all(f):
    print f.read() # print whatever's read from the file

# define a function with the name rewind having one argument f which is a file
def rewind(f):
    f.seek(0) # take the cursor back to 0th element in the file

# define a function with the name print_a_line having two two arguments
def print_a_line(line_count, f):
    print line_count, f.readline() # print the line number and that line

# open the input_file and store its contents in current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# function print_all is called to print the contents present in current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# sends the cursor back to the 0th element in the current_file
rewind(current_file)

print "Let's print three lines:"

# initialize current_line with 1 to print the first line from current_file
current_line = 1
print_a_line(current_line, current_file) # call print_a_line

# increse the value of current_line by 1 to change it to 2
current_line += 1 # using shorthand
print_a_line(current_line, current_file) # call print_a_line

# again, increse the value of current_line by 1 to change it to 3
current_line += 1 # using shorthand
print_a_line(current_line, current_file) # call print_a_line
