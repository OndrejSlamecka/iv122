from math import sin, cos, pi
import numpy as np
import svgwrite

# Rendering
def render(lines, name):
    dwg = svgwrite.Drawing('transformations_' + name + '.svg', profile='tiny')
    stroke = svgwrite.rgb(10,10,16,'%')

    # Preprocess
    xo, yo = 0,0 # offset
    for i, line in enumerate(lines): 
        f, t = line[0], line[1]
        f, t = f, t
        f[1], t[1] = -1 * f[1], -1 * t[1]
        f[0], t[0] = -1 * f[0], -1 * t[0]

        xo = min(xo, f[0], t[0])
        yo = min(yo, f[1], t[1])

        lines[i] = [f, t]
    # Draw
    for line in lines:
        f, t = line[0], line[1]
        fr = (int(f[0] - xo), int(f[1] - yo))
        to = (int(t[0] - xo), int(t[1] - yo))

        dwg.add(dwg.line(fr, to, stroke=stroke))

    dwg.save()

# Linear operations
def square(x):
    l1 = np.array([0, 0]), np.array([x, 0])
    l2 = np.array([x, 0]), np.array([x, x])
    l3 = np.array([x, x]), np.array([0, x])
    l4 = np.array([0, x]), np.array([0, 0])
    return [l1, l2, l3, l4]

def rotate(angle):
    a = angle
    a = a / 180 * pi;
    r = np.array([
        [cos(a), -sin(a), 0], 
        [sin(a),  cos(a), 0], 
        [0,       0     , 1]
    ])
    return r

def scale(x, y):
    return np.array([
        [x, 0, 0],
        [0, y, 0],
        [0, 0, 1],
    ])

def translate(x, y):
    return np.array([
        [1,0,x],
        [0,1,y],
        [0,0,1],
    ])

def apply(m, lines):
    for i, line in enumerate(lines):
        f, t = lines[i]
        f, t = np.append(f, 1), np.append(t, 1)
        f, t = f.reshape(-1,1), t.reshape(-1,1)
        f = np.dot(m, f)
        t = np.dot(m, t)
        lines[i] = f[:2, 0], t[:2, 0] 
    return lines

# Examples

def ex1():
    # Repeat 10: rotation(20), scaling(1.1, 1.1), translation(5, 10)
    lines = square(50)
    thing = square(50)
    for i in range(10):
        apply(translate(5,10), thing)
        apply(scale(1.1,1.1), thing)
        apply(rotate(20), thing)
        #thing = apply(translate(5,10), apply(scale(1.1, 1.1), apply(rotate(20), thing)))
    
        for line in thing:
            lines.append(line[:])

    render(lines, 'ex1')

ex1()
