from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),


current_file = open(input_file)

print "First let's print the whole file \n"

print_all(current_file) #uses the print_all function to print all contents from file

print "Now let's rewind, kinda like a tape"

rewind(current_file) #uses the rewind function to rewind the contents using seek function

print "Let's print 3 lines"

current_line = 1 #set current line to 1

print_a_line(current_line, current_file)

current_line = current_line + 1 #add 1 to the line number

print_a_line(current_line, current_file)

current_line = current_line + 1 # add another 1 to the line number

print_a_line(current_line, current_file)

