class route:
    def __init__(self, id, lat, long, weight, time, routnum):

        self.id = id
        self.lat = lat
        self.long = long
        self.weight = weight
        self.time = time
        self.routnum = routnum

    def getdata(self):
        return (self.lat, self.long)


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

    f.close()

main()
