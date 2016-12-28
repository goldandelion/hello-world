# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."#Pressing Ctrl + c while a python program is running will cause python to raise a KeyboardInterupt exception.
print "If you do want that, hit RETURN."# go on with this program

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') #If you use 'w' then you're saying "open this file in 'write' mode," thus the 'w' character. There's also 'r' for "read," 'a' for append, and modifiers on these.

print "Truncating the file.  Goodbye!"
target.truncate() #you need to open the file before truncating it

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
