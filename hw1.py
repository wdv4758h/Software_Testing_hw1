#!/usr/bin/env python

def triangle(a, b, c):
    edge = sorted([a, b, c])

    if edge[2] > edge[0] + edge[1]:
        return 'Not a triangle'

    count = (a == b) + (a == c) + (b == c)

    if count == 3:
        return 'Equilateral'
    elif count == 1:
        return 'Isosceles'
    else:
        return 'Scalene'
