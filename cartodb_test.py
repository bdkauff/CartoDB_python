import urllib
import urllib2
import json

print 'beginning test script'

username = 'ah3200'
apikey = 'e884d266bea87d377e2020b9a4bbb1f52be2260c'
query = 'SELECT * FROM map_census_acs2012_ct LIMIT 1'

url = "https://ah3200.cartodb.com/api/v1/sql"

# prams object that holds our api key and query.
params = {
    'api_key' : apikey,
    'q'       : query  
}

req = urllib2.Request(url, urllib.urlencode(params))
res = urllib2.urlopen(req)

response = res.read()

# saving response as json and pretty-ifying it while we're at it
json_response = json.dumps(json.loads(response), sort_keys=True, indent=4, separators=(',', ': '))

print(json_response)

with open('data.json', 'w') as outfile:
	outfile.write(json_response)

with open('data.json', 'r') as data_file:    
    json_data = json.load(data_file) 

print(json_data)
