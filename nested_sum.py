import numpy

def nested_sum(t):
    return sum(t[0]) + sum(t[1])

def cumsum(t):
    return numpy.cumsum(t)

def middle(t):
    return t[:1]