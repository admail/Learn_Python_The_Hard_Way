x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: '%s'." % x
#The %r is best for debugging, and the other formats are for actually displaying variables to users.
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %s"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
