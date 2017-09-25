from __future__ import print_function
import pylab as pl
import json
import os
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

noofbus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in noofbus:
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    stop = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    fout.write("{},{},{},{}\n".format(longitude,latitude,stop,status))