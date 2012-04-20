import svg
import random

def roundeven(num):
    return (num+1)/2*2

def arrange_in_layer(abin, pwidth, pheight):
    # articles are longer than wider
    # default rotation: width: x-direction
    #                   height:  y-direction

    layer = list()
    rest = list()
    root = {'x': 0, 'y': 0, 'width': pwidth, 'height': pheight, 'article': None, 'down': None, 'right': None}

    def find_node(root, width, height):
        if root['article']:
            return find_node(root['right'], width, height) or find_node(root['down'], width, height)
        elif width <= root['width'] and height <= root['height']:
            return root
        else:
            return None

    def split_node(node, width, height, article):
        node['article'] = article
        node['article']['pos'] = node['x'], node['y']
        node['down'] =    {'x': node['x'], 'y': node['y']+height, 'width': node['width'], 'height': node['height']-height, 'article': None, 'down': None, 'right': None}
        node['right'] = {'x': node['x']+width, 'y': node['y'], 'width': node['width']-width, 'height': height, 'article': None, 'down': None, 'right': None}
        return node

    for article in abin:
        # output format only accepts integer positions, round package sizes up to even numbers
        width, height = article['size']
        width, height = roundeven(width), roundeven(height)

        node = find_node(root, width, height)
        if (node):
            node = split_node(node, width, height, article)
        else:
            # rotate article
            article['size'] = height, width
            width, height = article['size']
            node = find_node(root, width, height)
            if (node):
                node = split_node(node, width, height, article)
            else:
                rest.append(article)

    # traverse tree to find articles
    def find_articles(node):
        if not node['article']:
            return
        layer.append(node['article'])
        if node['right']:
            find_articles(node['right'])
        if node['down']:
            find_articles(node['down'])

    find_articles(root)

    return root, layer, rest

def generate_bin():
    abin = []
    for i in 1,2,3:
        w, h = random.randint(20,150), random.randint(20,150)
        if h > w:
            w, h = h, w
        color = random.randint(0,255), random.randint(0,255), random.randint(0,255)
        for j in range(200000/(w*h)):
            abin.append({'pos':(0,0), 'size':(w,h), 'color':color})
    return abin


#print abin

abin = generate_bin()

#abin = [{'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}]
#abin = [{'color': (32, 64, 32), 'pos': (0, 0), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (144, 0), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (286, 0), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (428, 0), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (570, 0), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (0, 120), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (144, 120), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (286, 120), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (428, 120), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (570, 120), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (0, 238), 'size': (133, 117)}, {'color': (32, 64, 32), 'pos': (136, 238), 'size': (133, 117)}, {'color': (62, 226, 228), 'pos': (712, 0), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 48), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 120), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 168), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (272, 238), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (360, 238), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (448, 238), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (536, 238), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (624, 238), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 238), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (272, 286), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (360, 286), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (448, 286), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (536, 286), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (624, 286), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 286), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (0, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (90, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (180, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (270, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (360, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (448, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (536, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (624, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 356), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (0, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (90, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (180, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (270, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (360, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (448, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (536, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (624, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 396), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (0, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (90, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (180, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (270, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (360, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (448, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (536, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (624, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 436), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (0, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (90, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (180, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (270, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (360, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (448, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (536, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (624, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (712, 476), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (0, 516), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (94, 516), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (188, 516), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (282, 516), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (376, 516), 'size': (87, 39)}, {'color': (62, 226, 228), 'pos': (470, 516), 'size': (87, 39)}, {'color': (12, 175, 0), 'pos': (712, 96), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (712, 216), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (272, 334), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (410, 334), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (548, 334), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (684, 334), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (564, 524), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (684, 524), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (0, 556), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (138, 556), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (276, 556), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (412, 556), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (548, 556), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (684, 556), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (0, 578), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (138, 578), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (276, 578), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (412, 578), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (548, 578), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (684, 578), 'size': (115, 22)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}, {'color': (12, 175, 0), 'pos': (0, 0), 'size': (22, 116)}]
#abin = [{'color': (10, 42, 199), 'pos': (0, 0), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (164, 0), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (328, 0), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (490, 0), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (652, 0), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (0, 94), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (164, 94), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (328, 94), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (490, 94), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (652, 94), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (0, 188), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (152, 188), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (304, 188), 'size': (147, 92)}, {'color': (10, 42, 199), 'pos': (456, 188), 'size': (147, 92)}, {'color': (81, 151, 58), 'pos': (606, 194), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (704, 194), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (0, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (102, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (204, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (304, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (404, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (504, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (604, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (704, 282), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (0, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (102, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (204, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (304, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (404, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (504, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (604, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (704, 362), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (0, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (102, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (204, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (304, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (404, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (504, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (604, 442), 'size': (96, 78)}, {'color': (81, 151, 58), 'pos': (704, 442), 'size': (96, 78)}, {'color': (58, 217, 71), 'pos': (0, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (102, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (204, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (306, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (406, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (506, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (606, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (706, 520), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (0, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (102, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (204, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (306, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (406, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (506, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (606, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (706, 560), 'size': (94, 39)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}, {'color': (58, 217, 71), 'pos': (0, 0), 'size': (40, 94)}]

#pwidth, pheight = 400,600
pwidth, pheight = 800, 600
abin = sorted(abin, key=lambda article: article['size'][0]*article['size'][1], reverse=True)
root, layer, rest = arrange_in_layer(abin, pwidth, pheight)

#if rest:
#    print "rest!"

scene = svg.Scene('test1', (pwidth, pheight))
for a in layer:
    scene.add(svg.Rectangle(a['pos'],a['size'],a['color']))
scene.write()

# spread vertically

def get_left_children(node):
    if not node['article']:
        return []
    else:
        return [node] + get_left_children(node['down'])

def move_tree_down(node, y):
    if not node['article']:
        return
    pos = node['article']['pos']
    node['article']['pos'] = pos[0], pos[1]+y
    #if node['down']: # only increase height if not the last node
    #    node['height'] += y
    if node['right']:
        move_tree_down(node['right'], y)
    if node['down']:
        move_tree_down(node['down'], y)

# for each child on the very left, spread vertically and adjust subtree y accordingly

# calculate gap size:

def spread_vertically(node):
    leftnodes = get_left_children(node)
    for n in leftnodes:
        if n['right']:
            spread_vertically(n['right'])
    if len(leftnodes) == 0:
        return
    elif len(leftnodes) == 1:
        # arrange them in the center of parent
        gap = (node['height']-roundeven(leftnodes[0]['article']['size'][1]))/4*2
        move_tree_down(node, gap)
    else:
        sumleftnodes = sum([roundeven(n['article']['size'][1]) for n in leftnodes])
        d, m = divmod((node['height']-sumleftnodes)/2, len(leftnodes)-1)
        gaps = (m)*[(d+1)*2]+((len(leftnodes)-1)-m)*[d*2]
        #vgap = max(0, vgap-1)

        #leftnodes[0]['height'] += vgap
        # iteratively move trees down by vgap except for first row
        for node, gap in zip(leftnodes[1:], gaps):
            move_tree_down(node, gap)

spread_vertically(root)

#spread horizontically

def get_right_children(node):
    if not node['article']:
        return []
    else:
        return [node] + get_right_children(node['right'])

def move_tree_right(node, x):
    if not node['article']:
        return
    pos = node['article']['pos']
    node['article']['pos'] = pos[0]+x, pos[1]
    #if node['right']: # only increase width if not the last node
    #    node['width'] += x
    node['width'] -= x
    if node['right']:
        move_tree_right(node['right'], x)
    if node['down']:
        move_tree_right(node['down'], x)

# for each child on the very right, spread horizontically and adjust subtree y accordingly

# calculate gap size:

def spread_horizontically(node):
    rightnodes = get_right_children(node)
    if len(rightnodes) == 0:
        return
    elif len(rightnodes) == 1:
        # arrange them in the center of parent
        gap = (node['width']-roundeven(rightnodes[0]['article']['size'][0]))/4*2
        pos = rightnodes[0]['article']['pos']
        rightnodes[0]['article']['pos'] = pos[0]+gap, pos[1]
    else:
        # TODO: the uppermost row might not be the longest
        sumrightnodes = sum([roundeven(n['article']['size'][0]) for n in rightnodes])
        d, m = divmod((node['width']-sumrightnodes)/2, len(rightnodes)-1)
        gaps = (m)*[(d+1)*2]+((len(rightnodes)-1)-m)*[d*2]
        #hgap = max(0, hgap-1)

        #rightnodes[0]['width'] += hgap
        # iteratively move trees right by hgap except for first
        for node, gap in zip(rightnodes[1:], gaps):
            move_tree_right(node, gap)

        # process inner nodes as well
        for n in rightnodes:
            if n['down']:
                spread_horizontically(n['down'])

spread_horizontically(root)

layer = list()

def find_articles(node):
    if not node['article']:
        return
    layer.append(node['article'])
    if node['right']:
        find_articles(node['right'])
    if node['down']:
        find_articles(node['down'])

find_articles(root)

def intersects(a1, a2):
    return (
            a1['pos'][0]               <= a2['pos'][0]+a2['size'][0]
        and a1['pos'][0]+a1['size'][0] >= a2['pos'][0]
        and a1['pos'][1]               <= a2['pos'][1]+a2['size'][1]
        and a1['pos'][1]+a1['size'][1] >= a2['pos'][1]
    )

scene = svg.Scene('test2', (pwidth, pheight))
for a in layer:
    scene.add(svg.Rectangle(a['pos'],a['size'],a['color']))
scene.write()

# sanity checks
odds = list()
overhangs = list()
inters = list()
for article1 in layer:
    if (article1['pos'][0]%2 != 0
     or article1['pos'][1]%2 != 0):
        odds.append((article1['pos'][0], article1['pos'][1]))
    if (article1['pos'][0] < 0
     or article1['pos'][1] < 0
     or article1['pos'][0]+article1['size'][0] > pwidth
     or article1['pos'][1]+article1['size'][1] > pheight):
        overhangs.append((article1['pos'][0], article1['pos'][1]))
    for article2 in layer:
        if article1 == article2:
            continue
        if intersects(article1, article2):
            inters.append((article1['pos'][0], article1['pos'][1]))
for odd in odds:
    print "odd:", odd
for overhang in overhangs:
    print "overhang:", overhang
for inter in inters:
    print "intersect:", inter
if len(odds) or len(overhangs) or len(inters):
    print abin
    exit(1)
