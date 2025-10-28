import colorgram

colors = colorgram.extract('image.jpg', 30)

colorlist=[]
for color in colors:
    # colour=colors[0].rgb
    # colorlist.append(colour)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb=(r,g,b)
    colorlist.append(rgb)
print(colorlist)
