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

print ('Bus Line : {}'.format(sys.argv[2]))
print ('Number of Active Buses : {}'.format(len(noofbus)))
for i in range(len(noofbus)):
    longitude = noofbus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = noofbus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print("Bus {} is at latitude {} and longitude {}".format(i, latitude, longitude))