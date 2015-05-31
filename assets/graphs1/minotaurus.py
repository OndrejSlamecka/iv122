#!/usr/bin/env python3

from collections import deque
from random import randint, shuffle
import svgwrite

# TODO: Refactor maze renderer and put it in a separate file
class SvgMazeRenderer:
    def __init__(self, filename, n, cellside):
        self.cellside = cellside
        side = n*cellside

        self.dwg = svgwrite.Drawing(filename, size=(side,side), profile='tiny')
        self.stroke = svgwrite.rgb(10,10,16,'%')
        self.lines = []

        # Add border lines
        for i in range(n):
            self.lines.append(((i * cellside,0),((i+1) * cellside,0)))
            self.lines.append(((0, i * cellside),(0, (i+1) * cellside)))
            self.lines.append(((i * cellside,n*cellside),((i+1) * cellside,n*cellside)))
            self.lines.append(((n*cellside, i * cellside),(n*cellside, (i+1) * cellside)))

    def add_line(self, f, t):
        # The border is on the south or east side
        f = tuple(map(lambda x: x+1, f))

        # svgwriter doesn't use flipped coordinates like we do
        f = (f[1], f[0])
        t = (t[1], t[0])

        # scale to pixels
        scale = lambda p: tuple(n*self.cellside for n in p)
        f = scale(f)
        t = scale(t)

        self.lines.append((f,t))

    def render(self):
        for f,t in self.lines:
            self.dwg.add(self.dwg.line(f, t, stroke=self.stroke))
        self.dwg.save()

class Maze:
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    directions_south_east = [(1,0),(0,1)]

    def __init__(self, n):
        self.n = n
        self.grid = {}

        # Add edges between a vertex and its potential neighbours
        for x in range(n):
            for y in range(n):
                self.grid[(x,y)] = {}
                for v in self.PN((x,y)):
                    self.grid[(x,y)][v] = 1

    def PN(self, p, directions = None):
        """
        The potential neighbourhood function returns all possible neighbours
        PN : V -> 2^V
        """
        x,y = p

        # Define admissible coordinate
        ac = lambda x: x >= 0 and x < self.n

        # Get all the neighbours
        if directions == None:
            directions = self.directions
        ns = [(p[0] + d[0], p[1] + d[1]) for d in directions]

        # Only admissible neighbours
        ans = filter(lambda p: ac(p[0]) and ac(p[1]), ns)

        return list(ans)

    def N(self, p, directions = None):
        """
        Returns neighbours
        N : V -> 2^V, forall v in V . N(v) is a subset PN(v)
        """
        return list(filter(lambda n: self.grid[p][n] == 1, self.PN(p, directions)))

    def deg(self, p):
        return sum(self.grid[p].values())

    def add_wall(self, f, t):
        self.grid[f][t] = self.grid[t][f] = 0

    def is_bridge(self, f, t):
        """
        Performs BFS to check if edge with ends f and t is a bridge
        """
        if self.grid[f][t] == 0 or self.grid[t][f] == 0:
            raise Exception('Calling is_bridge for nonexistent edge')

        # hide the edge
        self.grid[f][t] = self.grid[t][f] = 0

        Q = deque()
        visited = {p: False for p in self.grid.keys()}

        Q.append(f)
        visited[f] = True

        while Q:
            u = Q.pop()

            if u == t:
                self.grid[f][t] = self.grid[t][f] = 1
                return False

            for v in self.N(u):
                if not visited[v]:
                    Q.append(v)
                    visited[v] = True

        self.grid[f][t] = self.grid[t][f] = 1
        return True


    def render(self, drawer):
        for x in range(self.n):
            for y in range(self.n):
                N = self.N((x,y), self.directions_south_east)
                PN = self.PN((x,y), self.directions_south_east)
                for v in [u for u in PN if u not in N]:
                    f = (x,y)
                    drawer.add_line(f,v)


def parseMaze():
    maze = Maze()

if __name__ == "__main__":
    maze = parseMaze()


    drawer = SvgMazeRenderer('minotaurus.svg', maze.n, 30)
    maze.render(drawer)
    drawer.render()

