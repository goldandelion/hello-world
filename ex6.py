# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

x = "There are %d types of people." % 10 # %d是带符号十进制数字
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # %s是字符串 1）

print x # 相当于 print "There are %d types of people." % 10 2）
print y # 3）

print "I said: %r." % x # %r打印时能够重现它所代表的对象 所以相当于 print "I said: "There are %d types of people."." 里面变成单引号 4）
print "I also said: '%s'." % y # %s是字符串 所以如果print里面不加引号打印出来的没有引号 5）

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #相当于 print "Isn't that joke so funny?! %r" % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
