#!/usr/bin/env python

def triangle(a, b, c):
    out_of_bound = ""
    if a < 0 or a > 200:
        out_of_bound += "a"
    if b < 0 or b > 200:
        out_of_bound += "b"
    if c < 0 or c > 200:
        out_of_bound += "c"

    if out_of_bound:
        return 'Value of {} is not in the range of permitted values'.format(','.join(out_of_bound))

    edge = sorted([a, b, c])

    if edge[2] >= edge[0] + edge[1]:
        return 'Not a triangle'

    count = (a == b) + (a == c) + (b == c)

    if count == 3:
        return 'Equilateral'
    elif count == 1:
        return 'Isosceles'
    else:
        return 'Scalene'

def next_date(month, day, year):
    return '{}/{}/{}'.format(month, day+1, year)
