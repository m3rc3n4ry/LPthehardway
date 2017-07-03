def add(first, second):
    ans = first + second
    return ans
    # using return keyword to give an integer answer whereever its called

print "We need two numbers to add:"
# asking for both arguments
print add(int(raw_input()), int(raw_input()))


print "Enter a number to add with 56:"
# asking only one argument
print add(int(raw_input()), 56)


print "Performing predefined addition:",
# both variables (arguments/parameters) already given
print add(23, 87.59)

# 4th type
print "I ate %d burgers last night." % add(2, 3)

# 5th type. Using UI to get variables.
print "How many pizza do you want sir?"; no3 = int(raw_input())
print "And how many burgers sir?"; no4 = int(raw_input())
print "Total %d quantities sir!" % add(no3, no4)
