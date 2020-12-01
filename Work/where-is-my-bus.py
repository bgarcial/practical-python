import urllib.request
from xml.etree.ElementTree import parse

# downloaded a web page
# This service only reports arrival times within the next 30 minutes.
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
# Parsing an xml document
doc = parse(u)

for pt in doc.findall('.//pt'):
    print(pt.text)
    # We extracted some useful information