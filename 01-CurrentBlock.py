## Importing required modules
import json
import urllib2

## api url
url = "http://api.maxcoinhub.io/Blockchain/GetBlockCount"

## Connecting to the url
s = urllib2.urlopen(url)

## reading the contents of the url
contents = s.read()

## Converting to json
j = json.loads(contents)

# Printing
print 'Blocks: ', j['result']
