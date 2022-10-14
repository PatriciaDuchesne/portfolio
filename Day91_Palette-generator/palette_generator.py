import extcolors


def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)


def get_img_colors(image):
    colors, pixel_count = extcolors.extract_from_image(image, limit=8)
    hex_colors = []
    for color in colors:
        r = int(color[0][0])
        g = int(color[0][1])
        b = int(color[0][2])
        if all(c >= 245 for c in (r, g, b)):
            pass
        else:
            hex_color = rgb_to_hex(r, g, b)
            hex_colors.append(hex_color)

    if not hex_colors:
        return "No colors to display. Pick another image."
    else:
        return hex_colors
