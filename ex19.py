def cheese_and_crackers(a, b):
    print "You have %d cheese!" % a
    print "You have %d boxes of cheese" % b
    print "Man that is enough for a party!"
    print "Get a blanket \n"

print "We can just give the function numbers directly"
cheese_and_crackers(30, 10)

print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too"
cheese_and_crackers(10-5, 100 * 2)

print "And we can combine variables and math"
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers - 40)
