#! /usr/local/bin/python

"""
Unit 1, Part 10 - pHit and pMiss

Write a code that outputs p after multiplying each entry 
by pHit or pMiss at the appropriate places. Remember that
the red cells 1 and 2 are hits and the other green cells
are misses

    p=[0.2,0.2,0.2,0.2,0.2]
    pHit = 0.6
    pMiss = 0.2

    #Enter code here
    
    print p

"""

p = [0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

pHit_list = [0, 1, 1, 0, 0]
pMiss_list = [1, 0, 0, 1, 1]

for i in xrange(len(p)):
    if pHit_list[i]:
        p[i] = p[i] * pHit
    elif pMiss_list[i]:
        p[i] = p[i] * pMiss

print p
