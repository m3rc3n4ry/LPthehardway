people = 47
cars = 40
trucks = 63

# if there are more cars than people then print this
if cars > people or trucks < cars:
    print "We should take cars."
elif cars < people and trucks > cars: # else, if people are more the cars, then print this
    print "We should not take the cars."
else: # if not any of the above is true, then print this
    print "We can't decide."

if trucks > cars and trucks > people: # if there are more trucks than cars and people then print this
    print "That's too many trucks."
elif trucks < cars and trucks < people: # else, if there are more cars than trucks then print this
    print "Maybe we could take the trucks."
else: # otherwise print this
    print "We still can't decide."

if people > trucks: # if people are more than trucks then print this
    print "Alright, let's just take the trucks."
else: # else, print this
    print "Fine, let's stay home then."
