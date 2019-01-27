## @file dangerousArea.py
# @author Ryan, Ather, Chris and Mostafa
# @brief A file that checks if a truck is in 
# @date 2019/01/26

import math
## @brief checks if coordinates are in any of the dangerous areas
# @param lat a float that stores the latitude of the truck
# @param long a float that strores the longitude of a truck
# @return bool True if truck is in a dangerous location False if it is not 
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
## @brief returns if a point is within r distance away from another
# @param dx difference in horizontal distance
# @param dy difference in vertical distance
# @param r the maximum distance 
# @return bool returns True if the point is within the distance False if not
def distance(dx, dy, r):
    return math.sqrt(dx*dx + dy*dy) < r
    
## @brief adds a dangerous area to the file of dangerous areas
# @param lat latitude of dangerous area
# @param long longitude of dangerous area
# @param r radius of the dangerous area
def addDangerousArea(lat, long, r):
    if(type(lat) is float and type(long) is float and type(r) is float):
        with open("HighRiskPlaces.txt", "a") as myfile:
            myfile.write("\n" + (str)(lat) + ", " + (str)(long) +  ", " + (str)(r)) 
        
