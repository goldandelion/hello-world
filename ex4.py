# -*- coding:utf-8 -*-
# 每个程序媛都有把程序写优雅的义务

cars = 100 #100赋值给变量cars
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "car_pool_capacity was not defined because on line 10 the variable used to define cars_driven * space_in_a_car is called carpool_capacity" #drill

print "it shows we can transport 120 instead of 120.0 people today if it's just 4 for space_in_a_car"
