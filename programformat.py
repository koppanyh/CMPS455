#!/usr/bin/env python
import sys

n = raw_input("File Name: ")
f = open(n, "r")
l = f.readlines()
f.close()
c = 1
for x in l:
	sys.stdout.write(str(c) + "\t" + x)
	c += 1
print

"""
Font formatting guidelines:

Courier 10 font

Gray 6 for line numbers
Green 4 for comments
Blue 2 for strings
Black for everything else
"""
