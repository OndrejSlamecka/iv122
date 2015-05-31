#!/usr/bin/env python3
import sys
sys.path.append('../turtle')
from Turtle import Turtle

### L-systems production
class Rules:
    def __init__(self, rules):
        self.rules = rules

    def _do_char(self, c):
        if c in self.rules:
            return self.rules[c]
        else:
            return c


    def __call__(self, i):
        """
        Performs single rewrite step on input string i
        """
        return ''.join([ self._do_char(c) for c in i])


def rewrite(rules, i, n):
    for _ in range(n):
        i = rules(i)

    return i

###
def guideTurtleThroughString(turtle, dist, angle, string, ignore = None):
    """
    @param turtle The turtle to guide
    @param dist   Distance to be made with each 'forward'
    @param angle  Angle for 'left' and 'right'
    """
    if ignore == None: ignore = []
    stack = []

    for c in string:
        if c == '+':
            turtle.right(angle)
        elif c == '-':
            turtle.left(angle)
        elif c == '[':
            stack.append(turtle.serialize())
        elif c == ']':
            turtle.deserialize(stack.pop())
        elif c not in ignore:
            turtle.forward(dist)


###

def koch():
    koch = Rules({'F': 'F+F--F+F'})
    s = rewrite(koch, 'F--F--F', 4)
    t = Turtle('koch')
    guideTurtleThroughString(t, 10, 60, s)
    t.save()

def pentaflake():
    r = Rules({'F': 'F----F----F----------F++F----F'})
    s = rewrite(r, 'F----F----F----F----F', 3)
    t = Turtle('pentaflake')
    guideTurtleThroughString(t, 20, 18, s)
    t.save()

def sierpinsky():
    r = Rules({'A': 'B-A-B',
               'B': 'A+B+A'})
    s = rewrite(r, 'A', 8)
    t = Turtle('sierpinsky')
    guideTurtleThroughString(t, 3, 60, s)
    t.save()

def hilbert():
    r = Rules({'A': '-BF+AFA+FB-',
               'B': '+AF-BFB-FA+'})
    s = rewrite(r, 'A', 5)
    t = Turtle('hilbert')
    guideTurtleThroughString(t, 10, 90, s, ['A', 'B'])
    t.save()

def tree1():
    r = Rules({'A': 'F[+A]-A',
               'F': 'FF'})
    s = rewrite(r, 'A', 6)
    t = Turtle('tree')
    guideTurtleThroughString(t, 10, 25, s)
    t.save()

def tree2():
    r = Rules({'A': 'F-[[A]+A]+F[+FA]-A',
               'F': 'FF'})
    s = rewrite(r, 'A', 6)
    t = Turtle('tree2')
    guideTurtleThroughString(t, 10, 25, s)
    t.save()

def koch_island():
    r = Rules({'F': 'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'})
    s = rewrite(r, 'F-F-F-F', 2)
    t = Turtle('koch_island')
    guideTurtleThroughString(t, 10, 90, s)
    t.save()

def gosper():
    r = Rules({'A': 'A-B--B+A++AA+B-',
               'B': '+A-BB--B-A++A+B'})
    s = rewrite(r, 'A', 4)
    t = Turtle('gosper')
    guideTurtleThroughString(t, 14, 60, s)
    t.save()

tree1()
