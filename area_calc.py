"""
This is a sample project. It calculate area for given shape and inputs.
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Started sample project"
print "Start time %s - %s - %s" % (now.day, now.month, now.year)

sleep(2)

hint = "Don't forget to include the correct units! \nExiting..."

shape = raw_input("Enter C for Circle or T for Triangle:")
shape = shape.upper()

if shape == 'C':
  radius = float(raw_input("What is the radius?:"))
  area = pi * radius ** 2
  print 'Calculating ... '
  sleep(1)
  print "Area of Circle is %.2f, \n%s" % (area, hint)
elif shape == 'T':
  base = float(raw_input("What is the base?:"))
  height  = float(raw_input("What is the height?:"))
  area = base * height * 0.5
  print 'Calculating ... '
  sleep(1)
  print "Area of Triangle is %.2f, \n%s" % (area, hint)
else:
   print "No such figure!"

exit(1)
