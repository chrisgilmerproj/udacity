#! /usr/local/bin/python

"""
Unit 1, Part 5 - Uniform Probability

Modify the empty list, p, so that it becomes a UNIFORM probability
distribution over five grid cells, as expressed in a list of
five probabilities.

    p = []
    print p

"""

size = 5

p = [1.0 / 5 for i in xrange(0, size)]
print p
print sum(p)
