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
    error = []

    if month > 12 or month < 1:
        error.append('month not in 1 ... 12')
    if day > 31 or day < 1:
        error.append('day not in 1 ... 31')
    if year > 2012 or year < 1812:
        error.append('year not in 1812 ... 2012')

    if error:
        return '\n'.join(error)

    day += 1

    if day > 31:
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return '{}/{}/{}'.format(month, day, year)

def commision(locks, stocks, barrels):

    if locks == -1:
        return 'Program terminates'

    error = []

    if locks < 0 or locks > 70:
        error.append('locks not in 1 ... 70')
    if stocks < 0 or stocks > 80:
        error.append('stocks not in 1 ... 80')
    if barrels < 0 or barrels > 80:
        error.append('barrels not in 1 ... 90')

    if error:
        return '\n'.join(error)

    total = 45 * locks + 30 * stocks + 25 * barrels

    com = 0.1 * min(1000, total)

    if total > 1000:
        com += 0.15 * min(800, total - 1000)

    if total > 1800:
        com += 0.2 * (total - 1800)

    if com.is_integer():
        com = int(com)

    return '${}'.format(com)
