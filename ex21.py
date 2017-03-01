def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "Subtracting %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "Multiplying %d * %d" % (a,b)
    return a * b

def divide(a,b):
    print "Dividing %d / %d" % (a,b)
    return a / b

print "Let's do some math functions"

age = add(30, 20)
height = subtract(40, 10)
weight = multiply(10, 50)
iq = divide(1000, 10)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "that becomes", what, "?"
