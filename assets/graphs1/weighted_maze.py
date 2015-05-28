#!/usr/bin/env python3

import sys
import operator
import collections

def read_graph():
    n = int(input())
    g = [[None]*n for i in range(n)]

    for i in range(n):
        line = input().split()
        for j in range(n):
            g[i][j] = int(line[j])

    return g

def dijkstra(n, g, s):
    """
    n -- |V(g)|
    g -- graph, weigh in vertices
    s -- starting node
    """
    Q = []
    d = {}
    pred = {}

    for i in range(n):
        for j in range(n):
            d[(i,j)] = float("inf")
            Q.append((i,j))
            pred[(i,j)] = []

    d[s] = 0

    while Q:
        ui, u = min(enumerate(Q), key=lambda ev: d[ev[1]])
        del Q[ui]

        for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
            v = tuple(map(operator.add, u, direction)) # neighbour's coords
            if not ((0 <= v[0] < n and (0 <= v[1] < n))):
                continue

            alt = d[u] + g[v[0]][v[1]]
            if d[v] >= alt:
                pred[v].append(u)
                d[v] = alt

    return d, pred

def tree2dot_go(n, pred, s):
    point2scalar = lambda p: p[1] * n + p[0]

    print('\t',point2scalar(s),'[label="({}, {})"]'.format(s[0], s[1]))
    for v in pred[s]:
        print('\t',point2scalar(s),'->',point2scalar(v))
        tree2dot_go(n, pred, v)

def tree2dot(n, pred, s):
    print('digraph G {')
    tree2dot_go(n, pred, s)
    print('}')

if __name__ == "__main__":
    g = read_graph()
    d, pred = dijkstra(len(g), g, (0,0))
    tree2dot(len(g), pred, (len(g) - 1, len(g) - 1))

