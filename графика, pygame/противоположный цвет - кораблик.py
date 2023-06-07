from PIL import Image, ImageDraw

'''
# противоположный цвет
r, g, b = list(map(int, input().split()))
im = Image.new("RGB", (500, 500), (255 - r, 255 - g, 255 - b))
print(im.size)
#im.save("5.jpg")
print(255 - r, 255 - g, 255 - b)
'''

'''
# средний цвет фото
im = Image.open("Рианна.jpg")
pixels = im.load() 
x, y = im.size 
count = x * y 
r1 = 0
b1 = 0
g1 = 0
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        r1 = r + r1
        g1 = g + g1
        b1 = b + b1
r = r1 // count
g = g1 // count
b = b1 // count

print(r, b, g)

#im.save("Рианна2.jpg")
'''


'''
# Вертикальное отражение
def mirror(im):
    pixels = im.load() 
    x, y = im.size 
    for i in range(x//2):
        for j in range(y):
            pixels[i, j], pixels[x - i -1, j] = pixels[x - i - 1, j], pixels[i, j]


def mirror_diagonal(im):
    pixels = im.load() 
    x, y = im.size 
    for i in range(x):
        for j in range(y - i):
            pixels[j, i], pixels[x - i -1, y - 1 - j] = pixels[x - i - 1,y - 1 - j], pixels[j, i]          
    im.save('res_mirror_diagonal.jpg')


im = Image.open("Рианна1.jpg")
mirror_diagonal(im)
'''


# зисуем парусник
def picture(file_name, width = 100, height = 100, sky_color = '#87CEEB', ocean_color = '#017B92', boat_color = '#874535', sail_color = '#FFFFFF', sun_color = '#FFCF40'):
    im = Image.new("RGB", (width, height), (sky_color))
    drawer = ImageDraw.Draw(im)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)), ocean_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)), (int(1.2 * width), int(0.2 * height))),sun_color)
    drawer.polygon(((int(0.25 * width), int(height * 0.65)),\
    (int(0.75 * width), int(height * 0.65)),\
    (int(0.7 * width), int(height * 0.85)),\
    (int(0.3 * width), int(height * 0.85)),\
    (int(0.25 * width), int(height * 0.65))), boat_color)
    drawer.rectangle(((int(0.49 * width), int(height * 0.3)), (width * 0.51, height * 0.65)), boat_color)
    drawer.polygon(((int(0.51 * width), int(height * 0.3)),\
    (int(0.75 * width), int(height * 0.45)),\
    (int(0.51 * width), int(height * 0.6)),\
    (int(0.51 * width), int(height * 0.3))), sail_color)
    
    im.save(file_name)

picture('test.jpg', 1000, 1000)

