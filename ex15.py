from sys import argv

script, filename = argv
prompt = '> '
txt = open(filename) #need to open before you can read

print "Here's your file %r." % filename
print txt.read() #just reading from the filename

txt.close()

print "Type the filename again"

file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()
