# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

print "I am 6'2\" tall."  # escape double-quote inside string 就是说\后面的引号不算引号
print 'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

rule =  """

(在行尾时)续行符\
\\反斜杠符号
\'单引号
\"双引号
\a响铃
\b退格(Backspace)
\e转义
\000空
\n换行
\v纵向制表符
\t横向制表符
\r回车
\f换页

"""

print "rule=", rule

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i, #这个暂时没懂
