## @file Route.py
#  @author Christopher Vishnu, Mostafa Mohsen, Ather Hassan, Ryan Woodard
#  @brief This module Consists of the route class which is used to hold a route, improve knowledge about the route, and get data from the routes
#  @date Jan 26 2019

## @brief each route is an instance of this class
#  @param DeviceSerial This is the parameter that represents each truck
#  @param lat This variable is the list of latitude values of each point on the route
#  @param long This variable is the list of longitude values of each point on the route
#  @param weight This variable holds the number of routes that have been averaged together so far
#  @param lat This variable is the list of longitude values of each point on the route
#  @param routnum This variable indicates which route is to be created as an object and updated
class route:

    ## @brief this is the initializer method
    def __init__(self, DeviceSerial, lat, long, weight, time, routnum):
        self.id = DeviceSerial
        self.lat = lat
        self.long = long
        self.weight = weight
        self.routnum = routnum

    ## @brief this method is used to get the longitude and latitude pooints of a route
    # @return (self.lat, self.long) the return is a tuples consisting of the list of lat values and list of long values
    def getdata(self):
        return (self.lat, self.long)

    ## @brief this method updates a route
    #  @details the method updates a route every time a route has been driven on
    #  @details the route is updated by taking an average between the current representation of the route and a recently recorded version
    #  @details the idea behind this is that the representation of a certain route gets more accurate every time it is driven on
    def avg(self, fname, recentRout):
        lat = ""
        long = ""
        weight = ""

        ratio = len(self.lat) / len(recentRout.lat)
        if ratio < 1:
            ratio = 1/ratio
            longLength = len(recentRout.lat)

        else:
            longLength = len(self.lat)

        for i in range(0, longLength, int(ratio)):
            self.lat[i] = str((float(self.lat[i])*self.weight + float(recentRout.lat[i]))/(self.weight + 1))
            self.long[i] = str((float(self.long[i])*self.weight + float(recentRout.long[i]))/(self.weight + 1))
            lat = lat + self.lat[i] + " "
            long = long + self.long[i] + " "

        lat = lat + "\n"
        long = long + "\n"
        weight = weight + str(self.weight + 1) + "\n"
        self.write(fname, lat, long, weight)


    ## @brief this method is called to write the route back into the text file which stores it, once it's been updated
    def write(self, fname, lat, long, weight):
        f = open(fname, "r")
        lines = f.readlines()
        f.close()
        f = open(fname, "w")
        lines[self.routnum] = lat
        lines[self.routnum + 1] = long
        lines[self.routnum + 2] = weight
        f.writelines(lines)
        f.close()


def main():
    fname = "masterRoutes.txt"
    f = open(fname, "r")
    lines = f.readlines()
    froute = 0
    time = 0
    id = 0
    r1 = route(id, (lines[froute]).split(), (lines[froute + 1]).split(), int(lines[froute + 2]), time, froute)
    recentRout = route(id, [1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1], 1, time, 0)
    r1.avg(fname, recentRout)
    print(r1.getdata())
    f.close()

#main()
