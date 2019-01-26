import csv
import math
#f = open('test.csv', 'r')
#reader = csv.reader(f)
#for row in reader:
    #print (row)
#f.close()
c = 0

def distance(dx, dy, r):
    return math.sqrt(dx*dx + dy*dy) < r

def OnTrack(long, lat, tupleThing):
    longList = [1,2,3,4]
    latList = [4,3,2,1]
    i = 0
    while i < len(longList):
        if distance(longList[i]-long, latList[i]-lat, 1):
            print("good")
        else:
            print("not good")
        i+=1
    