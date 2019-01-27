## @file ControlUnit.py
#  @author Ather Hassan, Chris Vishnu, Mostafa Mohsen, Ryan Woodard
#  @brief This unit controls all functions to ensure safety of the vehicles
#  @date 2019/01/27
import csv
import dangerousArea
import datetime
import math
import Route
## @brief Runs all the checks that are needed to ensure that a truck is on the correct route and only operating during the correct times
# @details If a truck is moving during the weekend or when the driver is not in the truck, it will alert the authorities and call for the gps to stay on. If a truck is moving too far outside the
# normalized route, it will send an alert to the company operators. If a truck is moving 
class gps():
    def __init__(self):
        # should read this from file
        self.route = Route.main()
        self.lastLong = 0.0
        self.lastLat = 0.0
        self.routNumber = 0
    def coordinatesRecieved(self, long, lat,punchedOut):
        # check time
        now = datetime.datetime.now()
        currentDay = now.strftime("%a")
        
        if (currentDay == 'Sat' or currentDay == 'Sun' or punchedOut):
            print("Warning, truck started on day off")
        else:
            print(self.OnTrack(self.route.getdata(), long, lat))
        # do a dangerous area check
        if (dangerousArea.DangerousAreaCheck(long,lat)):
            print("Warning, entering dangerous area")
        # on route check
    def OnTrack(self, coors, long, lat):
        status = ""
        for i in range (len(coors[0])):
            print(i)
            if distance((float)(coors[1][i])-long, (float)(coors[0][i])-lat, 1):
                status = "Truck is enroute, no visible issues"
                break
            else:
                status = "Truck is off route, authorities on stand by" 
        return status
    def triggered(long, lat, lastLong, lastLat):
        dx = lastLong - long
        dy = lastLat - lat
        if distance(dx, dy, 0.5):
            print("good")
        else:
            print("not good")


    
    def distance(dx, dy, r):
        return math.sqrt(dx*dx + dy*dy) < r


    #just for show
    def triggerAccelerometer(self, long, lat):
        print(triggered(long, lat, self.lastLong, self.lastLat))
        if (currentDay == 'Sat' or currentDay == 'Sun' or punchedOut):
            print("GPS now turned on, getting location every 5 minutes")        
        
    def setRouteNumber(self, num):
        self.routeNumber = num
def distance(dx, dy, r):
    return math.sqrt(dx*dx + dy*dy) < r
#YEEEET