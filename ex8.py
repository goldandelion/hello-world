# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", #这边显示双引号是因为didn't中已经有'了所以如果单引号的话就不知道到底哪里结束
	"So I said goodnight."
	)
