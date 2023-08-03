import colorgram

colors_extract = colorgram.extract('img.png',10)

def color_list_extract_rgb(colors_extract):
    color_rgb = []
    for color in colors_extract:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        color_rgb.append((r,g,b))

    return color_rgb

color_list = color_list_extract_rgb(colors_extract)

print(color_list)