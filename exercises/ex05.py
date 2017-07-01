my_name = 'Ashutosh Pathak'
my_age = 20
my_height = 169 # cms
my_iheight = 169 * 0.393 # inches
my_weight = 58 # kgs
my_pweight = 58 * 2.204 # pounds
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'


print "Let's talk about %s." % my_name
print "He's %d cms or %d inches tall." % (my_height, my_iheight)
print "He's %d kgs or %d pounds heavy." % (my_weight, my_pweight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
