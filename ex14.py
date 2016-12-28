# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

from sys import argv

script, user_name = argv
prompt = 'type here → '#这样后面改起来方便

print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?"% user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """

Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes,lives,computer)
