## @file ControlUnit.py
#  @author Ather Hassan, Chris Vishnu, Mostafa Mohsen, Ryan Woodard
#  @brief This unit controls all functions to ensure safety of the vehicles
#  @date 2019/01/27
import csv
import dangerousArea
import datetime
import math
import route
## @brief Runs all the checks that are needed to ensure that a truck is on the correct route and only operating during the correct times
# @details If a truck is moving during incorrect hours, without a driver, or too far out of the route it alerts an operator/ the police. Also warns the driver to avoid stops if they are entering 
# a high risk area.
class gps():
    def __init__(self):
        # should read this from file
        self.lastLong = 0
        self.lastLat = 0
        self.routNumber = 0

    ##@brief Runs when any gps coordinates are sent out from the truck.
    # @details Checks that the truck should be operating (it's not a weekend), that the driver is in the truck, and that the latest coordinates are on the path the truck should be on. If any of
    # these checks fail, it sends an appropriate alert.
    # @param long The incoming longitude
    # @param lat The incoming latitude
    # @param punchedOut Check for if the driver is currently on break
    def coordinatesRecieved(self, long, lat,punchedOut):
        # check time
        now = datetime.datetime.now()
        currentDay = now.strftime("%a")
        if (currentDay == 'Sat' or currentDay == 'Sun' or punchedOut):
            print("Warning, truck started on day off")
        # do a dangerous area check
        if (dangerousArea.DangerousAreaCheck(long,lat)):
            print("Warning, entering dangerous area")
        # on route check
    ##@brief Calculates if the vehicle has strayed far off the average route, and gives approporiate alerts if it has
    # @param routeNumber The number identifying which route the truck is on
    # @return status The output of whether or not the truck has passed the comparison with average and is currently on route 
    def OnTrack(self, routeNumber):
        longList = [1,2,3,4]
        latList = [4,3,2,1]
        i = 0
        for i in range (len(longList)):
            if distance(longList[i]-long, latList[i]-lat, 1):
                print("good")
            else:
                print("not good")
    def triggered(long, lat, lastLong, lastLat):
        dx = lastLong - long
        dy = lastLat - lat
        if distance(dx, dy, 0.5):
            print("good")
        else:
            print("not good")


    ## @brief returns if a point is within r distance away from another
    # @param dx difference in horizontal distance
    # @param dy difference in vertical distance
    # @param r the maximum distance 
    # @return bool returns True if the point is within the distance False if not
    def distance(dx, dy, r):
        return math.sqrt(dx*dx + dy*dy) < r


    #just for show
    def triggerAccelerometer(self, long, lat):
        print(triggered(long, lat, self.lastLong, self.lastLat))
        if (currentDay == 'Sat' or currentDay == 'Sun' or punchedOut):
            print("GPS now turned on, getting location every 5 minutes")        
    
    def setRouteNumber(self, num):
        self.routeNumber = num
#YEEEET