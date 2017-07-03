from sys import argv
from os.path import exists

script, from_file, to_file = argv

# removed the line telling us "The script is copying from one file to another"

# converted to one line
indata = open(from_file).read()

# size of the file is irrelevant here, hence removed

# no need to know about existence of a file, script's gonna create it anyway
# why were we even doing "Hit RETURN or CTRL-C"?!

# no need for a file object, in this case, out_file
# using append mode to see difference in file content
open(to_file, 'a').write(indata)

print "Alright, all done."
