from PIL import Image

f = open("DS5.txt", 'r')
img = Image.new('RGB', (960, 540), (255, 255, 255))

for line in f:
    x = int(line.split()[0])
    y = int(line.split()[1])
    img.putpixel((y, 540-x), (0, 0, 0))

img.show()
img.save("result.png", 'PNG')