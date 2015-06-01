#!/usr/bin/env python3

import matplotlib.pyplot as plt
from math import sqrt

### I/O
def render(name, clusters):
    plt.figure()

    colors = list('bgrcmyk')

    for i, centre in enumerate(clusters):
        points = clusters[centre]
        xs, ys = [p[0] for p in points], [p[1] for p in points]
        plt.plot(xs, ys, colors[i] + 'o')
        plt.plot(centre[0], centre[1], colors[i] + 'D')
    plt.savefig(name + '.png')

def read_points(filename):
    points = []
    for line in open(filename):
        x,y = line.rstrip().split()
        x,y = float(x), float(y)
        points.append((x,y))

    return points

### Computations

def dist(a, b):
    v = (b[0] - a[0], b[1] - a[1])
    return sqrt(v[0]**2 + v[1]**2)

def mean_point(cluster):
    # I wish Python had Haskell's foldr :- /
    m = lambda i: sum([p[i] for p in cluster]) / len(cluster)
    return (m(0), m(1))


def kmeans(points, k, n_iterations):
    # Start by assigning any points
    centres = [points[i] for i in range(k)]

    for i in range(n_iterations):
        clusters = {c: [] for c in centres}
        for p in points:
            clusters[min(centres, key=lambda c: dist(p, c))].append(p)

        centres = [mean_point(clusters[c]) for c in clusters]

    return clusters


def normalize(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    mx = max(xs)
    my = max(ys)

    xs = [x / mx for x in xs]
    ys = [y / my for y in ys]

    return list(zip(xs, ys))


### Main
if __name__ == "__main__":
    points = read_points('faithful.txt')
    points = normalize(points)
    render('kmeans', kmeans(points, 2, 5))

