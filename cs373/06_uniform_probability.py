#! /usr/local/bin/python

"""
Unit 1, Part 5 - Uniform Probability

Modify your code to create probability vectors, p, of arbitrary
size, n. Use n=5 to verify that your new solution matches
the previous one.

    p=[]
    n=5

    print p
"""

n = 5

p = [1.0 / 5 for i in xrange(0, n)]
print p
print sum(p)
