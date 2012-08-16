#! /usr/local/bin/python

"""
Unit 1, Part 26 - Sense and Move 2

Modify the previous code so that the robot senses red twice.

"""

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = p[(i - U) % len(p)] * pExact
        s += p[(i - U + 1) % len(p)] * pOvershoot
        s += p[(i - U - 1) % len(p)] * pUndershoot
        q.append(s)
    return q
    

for i in xrange(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])
print p

