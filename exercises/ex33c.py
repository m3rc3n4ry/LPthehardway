numbers = []

i = int(raw_input("Enter the number from which the list starts: "))
n = int(raw_input("Enter the number at which the list ends: "))
for a in range(i, n):
    print "At the top is %d" % a
    numbers.append(a)

    # a = a + 1 ---> adding this line won't make a difference
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
