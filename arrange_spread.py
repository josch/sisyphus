import svg
import random

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
        #if width%2 != 0:
        #    width += 1
        #if height%2 != 0:
        #    height +=1

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

abin = [{'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (172, 111, 210), 'pos': (0, 0), 'size': (103, 65)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (12, 155, 145), 'pos': (0, 0), 'size': (123, 97)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}, {'color': (253, 124, 189), 'pos': (0, 0), 'size': (118, 29)}]

#pwidth, pheight = 400,600
pwidth, pheight = 800, 600
abin = sorted(abin, key=lambda article: article['size'][0]*article['size'][1], reverse=True)
root, layer, rest = arrange_in_layer(abin, pwidth, pheight)

if rest:
    print "rest!"

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
        gap = (node['height']-leftnodes[0]['article']['size'][1])/2
        move_tree_down(node, gap)
    else:
        sumleftnodes = sum([n['article']['size'][1] for n in leftnodes])
        d, m = divmod(node['height']-sumleftnodes, len(leftnodes)-1)
        gaps = (m)*[d+1]+((len(leftnodes)-1)-m)*[d]
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
        gap = (node['width']-rightnodes[0]['article']['size'][0])/2
        pos = rightnodes[0]['article']['pos']
        rightnodes[0]['article']['pos'] = pos[0]+gap, pos[1]
    else:
        # TODO: the uppermost row might not be the longest
        sumrightnodes = sum([n['article']['size'][0] for n in rightnodes])
        d, m = divmod(node['width']-sumrightnodes, len(rightnodes)-1)
        gaps = (m)*[d+1]+((len(rightnodes)-1)-m)*[d]
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

# sanity checks
for article1 in layer:
    for article2 in layer:
        if article1 == article2:
            continue
        if intersects(article1, article2):
            print "intersects"
    if (article1['pos'][0] < 0
     or article1['pos'][1] < 0
     or article1['pos'][0]+article1['size'][0] > pwidth
     or article1['pos'][1]+article1['size'][1] > pheight):
        print "overhang"

scene = svg.Scene('test2', (pwidth, pheight))
for a in layer:
    scene.add(svg.Rectangle(a['pos'],a['size'],a['color']))
scene.write()
