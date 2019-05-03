import location, time, math

def distanceFromCoords(long1, lat1, long2, lat2):  #calculate distance between two coordinates
	#convert latitude and longitude to spherical coordinates in radians
	degrees_to_radians = math.pi / 180.0

	'''#phi = 90 - latitude
	phi1 = (90.0 - lat1) * degrees_to_radians
	phi2 = (90.0 - lat2) * degrees_to_radians

	# theta = longitude
	theta1 = long1 * degrees_to_radians
	theta2 = long2 * degrees_to_radians

	#calculate spherical distance from spherical coordinates.
	cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
								math.cos(phi1) * math.cos(phi2))
	arc = math.acos(cos)'''

	'''haversine form ref http://en.wikipedia.org/wiki/Great-circle-distance'''
	
	#phi = latitude
	phi1 = (lat1) * degrees_to_radians
	phi2 = (lat2) * degrees_to_radians

	# theta = longitude
	theta1 = long1 * degrees_to_radians
	theta2 = long2 * degrees_to_radians

	#calculate spherical distance from haversine function.
	arc=2.*math.asin( math.sqrt( math.sin((phi1-phi2)/2.)**2 + math.cos(phi1) * math.cos(phi2) * math.sin((theta1-theta2)/2.)**2 ))
	
	# multiply arc by the radius of the earth (3960 miles or 6371 kilometers)
	return round(arc * 6371 * 1000)  #multiplied with 1000 to get meters

location.start_updates()  #start location updates

if True:
	distance = 0  #total distance travelled
	startTime = time.time()  #set starting time of timer

	#to calculate distances two coordinates are needed. coord1 is the coordinate I was at, and coord2 is the coordinate I am at now

	coord2 = (location.get_location()['longitude'], location.get_location()['latitude'])
	now=time.time()
	while now-startTime<10.:		
		coord1 = coord2  #set coord1 to coord2 from previous loop repetition
		coord2 = (location.get_location()['longitude'], location.get_location()['latitude'])  #get current coordinates
		distance += distanceFromCoords(coord1[0], coord1[1], coord2[0], coord2[1])  #add distance between coord1 and coord2 to the total distance travelled

		print('\n', round(now - startTime), ' dist=', distance, ' lat/long= ',coord2[0],',',coord2[1])

		if now-startTime < 1.:
			#time.sleep(.1)
			time.sleep(1)
		else:
			time.sleep(1)
		now=time.time()

location.stop_updates()  #I know, this never gets executed :D

