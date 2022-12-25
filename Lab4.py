from PIL import Image, ImageDraw
from scipy.spatial import Voronoi

f = open("DS5.txt", 'r')
img = Image.new('RGB', (960, 540), (255, 255, 255))
m = []

for line in f:
    x = int(line.split()[0])
    y = int(line.split()[1])
    m.append((y, 540-x))
    
step = [(0, 1), (0, -1), (1, 0), (-1, 0)]


verticles = []

draw = ImageDraw.Draw(img)

for l in m:   
    print(l)
    if(img.getpixel((l[0], l[1])) != (0, 0, 0)):
        q = []
        sumx = 0
        sumy = 0
        num = 0
        img.putpixel((l[0], l[1]), (0, 0, 0))
        q.append((l[0], l[1]))
        for ll in q:
            sumx += ll[0]
            sumy += ll[1]
            num += 1
            for s in step:
                next = (ll[0] + s[0], ll[1] + s[1])
                if(next in m and img.getpixel(next) != (0, 0, 0)):
                    img.putpixel(next, (0, 0, 0))
                    q.append(next)
                    m.remove(next)
        pair = (int(sumx/num), int(sumy/num))
        verticles.append(pair)
        draw.ellipse([(pair[0] - 5, pair[1] - 5), (pair[0] + 5, pair[1] + 5)], fill = (0, 0, 255))

verticles.append((480, 10000))
verticles.append((-10000, -10000))
verticles.append((10000, -10000))

vor = Voronoi(verticles)
for v in vor.ridge_vertices:
    if(v[0] != -1 and v[1] != -1):
        draw.line([vor.vertices[v[0]][0], vor.vertices[v[0]][1], vor.vertices[v[1]][0], vor.vertices[v[1]][1]], fill=(255, 0, 0), width=1)

img.show()
img.save("result.png", 'PNG')