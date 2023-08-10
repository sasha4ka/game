import math

g = 90
jump_force = 40
horizontal_speed = 200

def dist(x1, y1, x2, y2):
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

def link_parser(link, start):
    obj = start
    link = link.split('.')
    for stage in link:
        try:
            index = int(stage)
            obj = obj[index]
        except:            
            obj = vars(obj)[stage]
    
    return obj