from geopy.geocoders import Nominatim
import pandas as pd
import sys

#'./data/train_for_map.csv'
train_location = pd.read_csv(sys.argv[1])

from_row = int(sys.argv[2])
to_row = int(sys.argv[3])

geolocator = Nominatim()

def geocode(cord):
	return_loc = geolocator.reverse(cord)
	return return_loc.raw['address']

batch = 10

for row in range(from_row,to_row,batch):
	source = train_location.ix[row:row+batch-1,:]
	source['address'] = source[['latitude','longitude']].apply(lambda x: geocode([x[0],x[1]]), axis=1)
	source.to_csv('./data/location_zipcode.csv', index=False, header=False, encoding='utf-8', mode='a')
	print "completed row " + str(row) + " to row " + str(row+batch-1)
