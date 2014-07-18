import random as rand
from clustering import clustering
from point import Point
import csv
import sys

geo_locs = []
#loc_ = Point(0.0, 0.0)  #tuples for location
#geo_locs.append(loc_)
#read the fountains location from the csv input file and store each fountain location as a Point(latit,longit) object
if len(sys.argv)>2:
    print "Input CSV file:" + sys.argv[2]
    f=     open(sys.argv[2], 'r')
else:
    print "Input CSV file: it-2004.sites.gpscoords.csv"   
    f = open('it-2004.sites.gpscoords.csv', 'r')
reader = csv.reader(f, delimiter=",")
for line in reader:
    loc_ = Point(float(line[0]), float(line[1]))  #tuples for location
    geo_locs.append(loc_)
#print len(geo_locs)
#for p in geo_locs:
#    print "%f %f" % (p.latit, p.longit)
#let's run k_means clustering. the second parameter is the no of clusters
k_value = sys.argv[1]
print "K_Value: " + k_value
cluster = clustering(geo_locs, int(k_value))
flag = cluster.k_means(False)
if flag == -1:
    print "Error in arguments!"
else:
    #the clustering results is a list of lists where each list represents one cluster
    print "clustering results:"
    cluster.print_clusters(cluster.clusters)