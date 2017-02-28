from sys import argv

script, filename = argv

print "We are going to erase %r:" % filename
print "If you don't want that hit CTRL + C"
print "If you do want that hit return"

raw_input("?")

print "Opening the file..."

target = open(filename, "w") # open with write permission

print "Truncating the file...Goodbye"

target.truncate()

print "Now I'm going to ask you for 3 lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1 + "\n" + line2 + "\n" + line3)

print "Now let's close it"

target.close()

print "Now let's open it again"

target = open(filename)

print "Now let's read it again"

print target.read()


