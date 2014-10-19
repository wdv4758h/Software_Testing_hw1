#!/usr/bin/env python

def triangle(a, b, c):
    if a < 0 or a > 200:
        return 'Value of a is not in the range of permitted values'
    if b < 0 or b > 200:
        return 'Value of b is not in the range of permitted values'
    if c < 0 or c > 200:
        return 'Value of c is not in the range of permitted values'

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
