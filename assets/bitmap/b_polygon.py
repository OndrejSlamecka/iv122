from PIL import Image
from math import sqrt, sin, cos, pi

def get_dimensions(points):
    x = max(points, key = lambda p: p[0])[0]
    y = max(points, key = lambda p: p[1])[1]
    return x,y

def render(points):
    dim = get_dimensions(points)
    img = Image.new('RGB', dim, 'white')
    pixels = img.load()

    ### Invert y coordinate, PIL's 0,0 is in the upper left corner
    for i in range(len(points)):
        points[i] = points[i][0], dim[1] - points[i][1]
    points = sorted(points, key = lambda p: p[0])
    
    ### Actual drawing

    
    ### Save
    #img = img.resize((side // 2, side // 2), Image.ANTIALIAS)
    img.save('b_polygon.png')

points = [(10, 10), (180, 20), (160, 150), (100, 50), (20, 180)]
render(points)
