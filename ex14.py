from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % (user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
So you said %s about liking me.
You live in %s. I don't know where that is
and you use a %s computer""" % (likes, lives, computer)
