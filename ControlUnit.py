import accelerator
import dangerousArea
import datetime
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
            print("BIG UHOH")
        # do a dangerous area check
        if (dangerousArea.DangerousAreaCheck(long,lat)):
            print("Warning, entering dangerous area")
        # on route check
        pass
    
    #just for show
    def triggerAccelerometer(self, long, lat):
        print(accelerator.triggered(long, lat, self.lastLong, self.lastLat))
        if (currentDay == 'Sat' or currentDay == 'Sun' or punchedOut):
            print("GPS now turned on, getting location every 5 minutes")        
        
    def setRouteNumber(self, num):
        self.routeNumber = num
