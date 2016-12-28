# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

from sys import argv

script, filename = argv

txt = open(filename) #打开用户输入的这个文件

prompt = ">>>>>>>"
print "Here's your file %r:" % filename
print txt.read() #打开用户输入的这个文件并显示

print "Type the filename again:"
file_again = raw_input(prompt) #不是真的重新输入啦，就是打开文件的意思,而且不仅打开txt，py也能打开,但不是跑程序，只是看到代码

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
