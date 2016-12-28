# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

print "How old are you?",
age = raw_input()

print "How tall are you? (give me cm)",
height = raw_input()

print "How much do you weight? (give me kg)",
weight = raw_input()

# so raw_input is a string because when I try to work out BMI, it doesn't work
# BMI = "%d/(%d*%d)" % (weight,height,height) this doesn't work

print "So, you're %r old, %r tall and %r heavy." % (age,height,weight),
