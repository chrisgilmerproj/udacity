#! /usr/local/bin/python

"""
Unit 1, Part 4 - Uniform Probability

Create an array where the probability that a car is in any place in the array
is uniform.
"""

size = 5

p = [1.0 / 5 for i in xrange(0, size)]
print p
print sum(p)
