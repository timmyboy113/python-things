#!/usr/bin/python

import os
a=0
pi = 3.14
b=0
c=""
x=int(raw_input("Enter number of problems: "))        
while a != x:
    a = a+1
    b=raw_input("%i. " % (a))
    b=os.popen("awk 'BEGIN {print %s}'" % (b)).read()
    b=b[:-1]
    c = ("%s. %s\n" % (a, b)) + c
print "\n%s\n" % ('\n'.join( reversed(c.split('\n')) ))  