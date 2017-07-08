numbers = []

def create_list(i, n):
    increment = int(raw_input("""Enter the value by which the
    list is to be incremented: """)) # only integer increment allowed
    while i < n:
        print "At the top is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

start = int(raw_input("Enter the number from which the list starts: "))
stop = int(raw_input("Enter the number at which the list ends: "))
create_list(start, stop)

print "The list: "

for num in numbers:
    print num
