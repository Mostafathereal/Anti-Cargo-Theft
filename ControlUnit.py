import csv
import dangerousArea
import datetime
import math
#import route.py
class gps():
    def __init__(self):
        # should read this from file
        self.lastLong = 0
        self.lastLat = 0
        self.routNumber = 0
    def coordinatesRecieved(self, long, lat,punchedOut):
        # check time
        now = datetime.datetime.now()
        currentDay = now.strftime("%a")
        if (currentDay == 'Sat' or currentDay == 'Sun' or punchedOut):
            self.triggerAccelerometer(long,lat)
        # do a dangerous area check
        if (dangerousArea.DangerousAreaCheck(long,lat)):
            print("Warning, entering dangerous area")
        # on route check
    def OnTrack(tupleThing):
        longList = [1,2,3,4]
        latList = [4,3,2,1]
        i = 0
        while i < len(longList):
            if distance(longList[i]-long, latList[i]-lat, 1):
                print("good")
            else:
                print("not good")
            i+=1
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
