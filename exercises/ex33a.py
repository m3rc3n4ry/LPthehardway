i = 0
numbers = []

def create_list(n):
    global i
    while i < n:
        print "At the top is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

num = int(raw_input("Enter the number at which the list ends: "))
create_list(num)

print "The list: "

for num in numbers:
    print num
