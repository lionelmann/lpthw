print "Let's practice everything"
print "You\'d need to know \'bout escapes with \\ that do \n new lines and \n\t tabs"
poem =  """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none
"""

print "-" * 10
print poem
print "_" * 10

five = 10 - 2 + 3 - 6

print "This should be five: %d" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/ 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

# Inside the function the variable is temporary. When you return it
# then it can be assigned to a variable for later. Just making a new variable
# named beans to hold the return value.

a, b, c = secret_formula(start_point)

print "With a starting point of %d" % start_point

print "We'd have %d beans, %d jars, and %d crates" % (a, b, c)

start_point = 10

print "-" * 10

print "We can also do it this way"
print "We'd have %d beans, %d jars, %d crates" % secret_formula(start_point)

print "-" * 10
