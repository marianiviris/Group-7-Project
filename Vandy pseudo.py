import googlemaps
import gmaps
#API keys
gm= googlemaps.Client('your key')
gmaps.config(api_key= 'your key')

Dtable= input data table
locations= Dtable[['lat','lng']]
val= Dtable['weight']

#gecode center of contiguous US
gc_result= gm.geocode('Lebanon, Kansas')[0]

#get the center coords
clat= gc_result['geometry']['location']['lat']
clng= gc_result['geometry']['location']['lng']
print('center=',clat,clng)

def drawHmap(location, val, zoom, intensity, radius):
	#set params
	hlayer= gmaps.hlayer(locations, val, dissapating='True')
	hlayer=.max_intensity= intensity
	hlayer.point_radius= radius
	#makes a figure
	fig= gmaps.figure()
	fig= gmaps.figure(center= [clat, clng], zoom_level= zoom)
	fig.add_layer(hlayer)
	return fig

#more params
zoom= 5
intensity= 5
radius= 15

#call dat map BOOOIIIII
drawHeatMap(locations, val,zoom,intensity,radius)
