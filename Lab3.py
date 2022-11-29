from PIL import Image
from math import cos, sin, pi

f = open("DS5.txt", 'r')
img = Image.new('RGB', (960, 960), (255, 255, 255))

alpha = 10*(5+1)*pi/180

s = [[cos(alpha), sin(alpha)],
    [-sin(alpha), cos(alpha)]]

def transform(point):
    pointx = (point[0] - 480)*s[0][0] + (point[1] - 480)*s[1][0]
    pointy = (point[0] - 480)*s[0][1] + (point[1] - 480)*s[1][1]
    return (int(pointx) + 480, int(pointy) + 480)

for line in f:
    x = int(line.split()[0])
    y = int(line.split()[1])
    img.putpixel(transform((y, 960-x)), (0, 0, 255))

img.show()
img.save("result.png", 'PNG')
