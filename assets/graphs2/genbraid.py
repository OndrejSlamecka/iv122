#!/usr/bin/env python3
from random import randint
import svgwrite

class Maze:
    def __init__(self, n):
        self.n = n
        self.grid = [[1 for _ in range(n)] for _ in range(n)]

class Braid(Maze):
    def add_walls(self):
        grid = self.grid
        n = len(grid)
        for i in range(n*n):
            for direction in [ ... ]:
                r = randint(0,100)
                if r < 30:
                    grid[i][j] = 0
                    grid[j][i] = 0



def render(filename, grid):
    cellside = 30
    dwg = svgwrite.Drawing('filename.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')

    scale = lambda x,y: tuple(n*cellside for n in (x,y))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            f = scale(x,y)
            if grid[]

            t_horizontal = scale(x+1,y)
            if grid[x][y]:
                dwg.add(dwg.line(f, t_horizontal, stroke=stroke))

            t_vertical = scale(x,y+1)
            if :
                dwg.add(dwg.line(f, t_vertical, stroke=stroke))

    dwg.save()

if __name__ == "__main__":
    braid = Braid(20)
    braid.add_walls()

    render("test.svg", braid.grid)

