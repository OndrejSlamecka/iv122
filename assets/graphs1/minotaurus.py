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

    def extend(self):
        """
        Adds one row and column
        """

        # Row
        for x in range(self.n):
            self.grid[(x, self.n)] = {}

        # Column
        for y in range(self.n):
            self.grid[(self.n, y)] = {}

        # Corner cell
        self.grid[(self.n, self.n)] = {}

        self.n += 1

        # Add edges
        for x in range(self.n):
            for y in range(self.n):
                for v in self.PN((x,y)):
                    if v not in self.grid[(x,y)]:
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

    def has_wall(self, f, t):
        return self.grid[f][t] == 0 or self.grid[t][f] == 0

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


def parse_maze(fname):
    maze = Maze(0)

    for line in open(fname):
        line = line.rstrip('\n')
        if line:
            f,t = line.split()

            f = tuple(map(int, f.split(',')))
            t = tuple(map(int, t.split(',')))

            while f[0] >= maze.n or f[1] >= maze.n or t[0] >= maze.n or t[1] >= maze.n:
                maze.extend()

            maze.add_wall(f, t)

    return maze


def play_game(maze, exit, minotaurus, theseus):
    q = deque()
    visited = {}
    pred = {}

    s = (minotaurus, theseus)
    visited[s] = 1
    q.append(s)

    while q:
        u = q.pop()

        if u[1] == exit:
            q = u
            sol = [q]
            while q in pred:
                sol.append(pred[q])
                q = pred[q]
            return sol


        # Add options to queue
        for t_n in maze.N(u[1]):
            rm, N = minotaurus_turn(maze, u)
            if t_n in N:
                continue

            v = (rm, t_n)

            if v not in visited:
                q.append(v)
                pred[v] = u
                visited[v] = 1

    return None


def minotaurus_turn(maze, u):
    t = u[1]
    rm = u[0] # resulting move

    # Calculate minotaurus' movement
    n = maze.n
    m_n = u[0]  # the default is stay where you are
    vd = 1 if m_n[1] - t[1] < 0 else -1
    hd = 1 if m_n[0] - t[0] < 0 else -1
    d = (hd, vd)
    N = []

    # One horizontal step of the mintaurus
    one_h = (m_n[0] + d[0], m_n[1])

    if one_h[0] < n and one_h[0] >= 0 and one_h[1] < n and one_h[1] >= 0 \
        and not maze.has_wall(m_n, one_h):
        rm = one_h
        N.append(one_h)

    # Do another horizontal if possible
    two_h = (one_h[0] + d[0], one_h[1])

    if two_h[0] < n and two_h[0] >= 0 and two_h[1] < n and two_h[1] >= 0 \
        and not maze.has_wall(one_h, two_h):
        rm = one_h
        N.append(two_h)

    # Just horizontal was possible, add one vertical from it
    if len(N) == 1:
        one_v = (one_h[0], one_h[1] + d[1])

        if one_v[0] < n and one_v[0] >= 0 and one_v[1] < n and one_v[1] >= 0 \
            and not maze.has_wall(one_h, one_v):
            rm = one_h
            N.append(one_v)

    # If no horizontal were possible, do vertical
    if len(N) == 1:
        # from m_n
        one_v = (m_n[0], m_n[1] + d[1])

        if one_v[0] < n and one_v[0] >= 0 and one_v[1] < n and one_v[1] >= 0 \
            and not maze.has_wall(m_n, one_v):
            rm = one_h
            N.append(one_v)

    if len(N) == 1:
        two_v = (one_v[0], one_v[1] + d[1])

        if two_v[0] < n and two_v[0] >= 0 and two_v[1] < n and two_v[1] >= 0 \
            and not maze.has_wall(one_v, two_v):
            rm = one_h
            N.append(two_v)

    return (rm, N)



if __name__ == "__main__":
    maze = parse_maze('minotaurus_maze.txt')
    n = maze.n  # For Theseus' position
    sol = play_game(maze, (1,0), (0,0), (n-1, n-1))
    print(sol)

    drawer = SvgMazeRenderer('minotaurus.svg', maze.n, 30)
    maze.render(drawer)
    drawer.render()

