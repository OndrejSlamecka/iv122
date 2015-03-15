import math
import random

def leibniz(n):
    s = 0
    for i in range(n):
        s += ((-1)**i) / (2*i + 1.0)

    return s

def archimedes(n):
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2

    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2

"""
 Imagine throwing n darts to (r/2)*(r/2) square which is has circle with radius r
 inside. Square area is 4*r^2, circle area is pi*r^2. Ratio of this areas * 4 = pi
"""
def monte_carlo(n):
    inside_circle = 0
    for _ in range(0, n):
        r1 = random.random()
        r2 = random.random()
        if (r1*r1 + r2*r2) < 1:
            inside_circle += 1

    return 4.0 * inside_circle / n

l1000 = leibniz(1000) * 4
print(l1000, l1000 - math.pi)
print(archimedes(16))
print(monte_carlo(100000))
