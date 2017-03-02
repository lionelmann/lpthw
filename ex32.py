the_count = [1,2,3,4,5]
fruits = ["apples", "bananas", "oranges", "pears", "grapes"]
change = ["dimes", 1, "pennies", 10, "quarters"]

for n in the_count:
    print "Here are the numbers: %d" % n

for fruit in fruits:
    print "Here is the fruit: %s" % fruit

for money in change:
    print "Here's the money: %r" % money

#building lists with an empty array
#first create an empty array

element = []

for i in range(0,6):
    print "Adding %d to the element array" % i
    element.append(i) #appends the element to the list
    print element

#now we can print out the elements array like before

for i in element:
    print "This is element: %d" % i
