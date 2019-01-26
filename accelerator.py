import math
def triggered(long, lat, lastLong, lastLat):
    dx = lastLong - long
    dy = lastLat - lat
    if distance(dx, dy, 0.5):
        print("good")
    else:
        print("not good")
    
def distance(dx, dy, r):
    return math.sqrt(dx*dx + dy*dy) < r