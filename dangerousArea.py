import math
def DangerousAreaCheck(lat, long):
    with open("HighRiskPlaces.txt") as f:
        coors = f.read().splitlines() 
        f.close()
    for coor in coors:
        coor = coor.split(",")
        dx = lat - (float)(coor[0])
        dy = long - (float)(coor[1])
        if distance(dx, dy, (float)(coor[2])):
            print("Heh, I'm in danger")
            return True
    return False
        
def distance(dx, dy, r):
    return math.sqrt(dx*dx + dy*dy) < r
    
    
def addDangerousArea(lat, long, r):
    if(type(lat) is float and type(long) is float and type(r) is float):
        with open("HighRiskPlaces.txt", "a") as myfile:
            myfile.write("\n" + (str)(lat) + ", " + (str)(long) +  ", " + (str)(r)) 
        
