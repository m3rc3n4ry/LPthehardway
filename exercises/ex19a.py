# defining a function cheese_and_crackers with arguments cheese_count and
# boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give functions numbers directly:"
# calling the function cheese_and_crackers giving initial values to
# cheese_count and boxes_of_crackers 20 and 30 respectively
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# explicitly providing variables (arguments) during function call
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# doing addition in the arguments to get required values into the function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# doing addition on two variables and passing it to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
