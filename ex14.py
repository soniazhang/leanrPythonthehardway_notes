from sys import argv

script, user_name=argv
prompt = '>' # use the prompt rather than typing it over and over
# you can use other formats


print "Hi %s, I'm the %s script." % (user_name, script)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. No sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
