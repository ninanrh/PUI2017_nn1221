from __future__ import print_function
import pylab as pl
import json
import os
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

%pylab inline
pl.rc('font', size=15)

url = http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=84576710-519b-4\
f26-9c52-0be20ed6b6ae&VehicleMonitoringDetailLevel=calls&LineRef=B52

print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

