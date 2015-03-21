import random
import svgwrite

# normal distribution
norm_npoints = 500
mu = 200
sigmas = [10, 20, 50, 100] # std. deviation
offset = 100 # to see points with negative coords

# uniform
uni_npoints = 100
uni_range = 500

def render(sigma, lines, points):
    dwg = svgwrite.Drawing('hull_' + str(sigma) + '.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')

    for f, t in lines:
        dwg.add(dwg.line(f, t, stroke=stroke))

    for p in points:
        dwg.add(dwg.circle(p, r = 3))

    dwg.save()

# See https://docs.python.org/3.4/library/random.html
def norm_rand_point(sigma):
    x = random.normalvariate(mu, sigma) + offset
    y = random.normalvariate(mu, sigma) + offset
    return round(x), round(y)

def uni_rand_point():
    x = random.randint(0, uni_range)
    y = random.randint(0, uni_range)
    return x, y

# Graham scan, http://en.wikipedia.org/wiki/Graham_scan
def orientation(p1, p2, p3):
    # >0    if p1, p2, p3 are cw
    # <0    if ccw
    #  0    if colinear
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

def hull(points):
    points.sort(key=lambda p: p[1])
    top, bottom = [],[]
    for p in points:
        while len(top) > 1 and orientation(top[-2], top[-1], p) <= 0:
            top.pop()
        while len(bottom) > 1 and orientation(bottom[-2], bottom[-1], p) >= 0:
            bottom.pop()
        top.append(p)
        bottom.append(p)
    bottom.reverse()
    return top + bottom

# Run
def compute_and_render(sigma, points):
    h = hull(points)
    lines = []
    for i in range(len(h) - 1):
        lines.append((h[i], h[i+1]))

    render(sigma, lines, points)

for sigma in sigmas:
    points = [norm_rand_point(sigma) for _ in range(norm_npoints)]
    compute_and_render(sigma, points)

points = [uni_rand_point() for _ in range(uni_npoints)]
compute_and_render('uniform', points)
