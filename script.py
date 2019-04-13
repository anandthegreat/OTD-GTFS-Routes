stops_dict={}
#stop_times_dict={} can't be created since no primary key
trips_dict={}
routes_dict={}

#--------stop_dict_init----------
#mapping stopid to stopname				<string-->string mapping>
count=0
stops=open("stops.txt","r")
for line in stops:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")
	stops_dict.setdefault(fields[0],fields[2])
stops.close()

#-----------trips_dict_init-------
#mapping tripid to routeid 		  		<string-->string mapping>
count=0
trips=open("trips.txt","r")
for line in trips:
	count+=1
	if(count==1):
		continue
	fields=line.rstrip('\n').split(",")
	trips_dict.setdefault(fields[2],fields[0])
trips.close()

#-----------routes_dict_init-------
#mapping routeid to routeshortname   	<string-->string mapping>
count=0
routes=open("routes.txt","r")
for line in routes:
	count+=1
	if(count==1):
		continue
	fields=line.rstrip('\n').split(",")
	routes_dict.setdefault(fields[3],fields[1])
routes.close()


source=raw_input("Enter Source:")
dest=raw_input("Enter Destination:")

src_stop_id="-1"
dest_stop_id="-1"

for key, value in stops_dict.iteritems():
	if(src_stop_id=="-1" and value==source):
		src_stop_id=key
	elif(dest_stop_id=="-1" and value==dest):
		dest_stop_id=key
	if(src_stop_id!="-1" and dest_stop_id!="-1"):
		break

if(src_stop_id=="-1"):
	print("Source not found..")
if(dest_stop_id=="-1"):
	print("Destination not found")

# #----------------------------------------
count=0
stoptimes=open("stop_times.txt","r")
src_tripIDs=set()
dest_tripIDs=set()
for line in stoptimes:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")
	if(fields[3]==src_stop_id):
		src_tripIDs.add(fields[0])
	elif(fields[3]==dest_stop_id):
		dest_tripIDs.add(fields[0])

# print(len(src_tripIDs))
# print(len(dest_tripIDs))
stoptimes.close()

# #----------------------------------------
src_routeIDs=set()
dest_routeIDs=set()

for val in src_tripIDs:
	if val in trips_dict.keys():
		src_routeIDs.add(trips_dict[val])

for val in dest_tripIDs:
	if val in trips_dict.keys():
		dest_routeIDs.add(trips_dict[val])

# print(len(src_routeIDs))
# print(len(dest_routeIDs))

# #----------------------------------------

zero_hop_route_IDs=set()

for x in src_routeIDs:
	for y in dest_routeIDs:
		if(x==y):
			# print("0 hop route found!")
			zero_hop_route_IDs.add(x)

# #-----------------------------------------
count=0
if(len(zero_hop_route_IDs)>0):
	# print("You can use any of the following 0-hop routes: ")
	for val in zero_hop_route_IDs:
		print("RouteID: "+ val + " Route Name: "+routes_dict[val])

# #------------------1-Hop------------------
# count=0
# src_reachable_stops={}			#stops reachable from source 	  <"764"=[s1,s2,s3...]>
# dest_reachable_stops={}			#stops reachable from destination <"764"=[s1,s2,s3...]>
# src_route_tripIDs={}			#trip ids of all routes which touch the source
# dest_route_tripIDs={}			#trip ids of all routes which touch the destination
# src_trip_to_route={}
# dest_trip_to_route={}

# trips=open("trips.txt","r")
# for line in trips:
# 	count+=1
# 	if(count==1):
# 		continue
# 	fields=line.split(",")
# 	if(fields[0] in src_routeIDs):
# 		src_route_tripIDs.setdefault(fields[0],[]).append(fields[2])	#save trip id 
# 		src_trip_to_route.setdefault(fields[2],[]).append(fields[0])

# 	if(fields[0] in dest_routeIDs):
# 		dest_route_tripIDs.setdefault(fields[0],[]).append(fields[2])
# 		dest_trip_to_route.setdefault(fields[2],[]).append(fields[0])

# trips.close()
# count=0

# stoptimes=open("stop_times.txt","r")
# for line in stoptimes:
# 	count+=1
# 	if(count==1):
# 		continue
# 	fields=line.split(",")
# 	if(fields[0] in src_trip_to_route.keys()):
# 		if(fields[3]!=src_stop_id and fields[3]!=dest_stop_id):
# 			src_reachable_stops.setdefault(src_trip_to_route.get(fields[0]),[]).append(fields[3])		#save stops which are reachable from source
# 	if(fields[0] in dest_route_tripIDs):	
# 		if(fields[3]!=src_stop_id and fields[3]!=dest_stop_id):
# 			dest_reachable_stops.setdefault(dest_trip_to_route.get(fields[0]),[]).append(fields[3])		#save stops which are reachable from destination

# stoptimes.close()

# one_hop_routes=set()

# for bus_no in src_reachable_stops:
# 	for bus_no_dest in dest_reachable_stops:
# 		if(set(src_reachable_stops.get(bus_no)) & set(dest_reachable_stops.get(bus_no_dest))):
# 			one_hop_routes.add(bus_no+"->"+bus_no_dest)

# print("One Hop Routes are:")
# for x in one_hop_routes:
# 	print(x)




#0 hop:
#Pumposh Enclave (Try both of the 2 stops with this name)
#Masjid Moth

#APS Colony/ Jharera Gaon
#Shankar Vihar/ National Highway 8

#Dwarka Flyover
#Matiyala Xing



#1 hop:
#Shankar Vihar / National Highway 8
#Matiyala Xing

#Shankar Vihar/ National Highway 8
#Pumposh Enclave

#C-Lal Chowk
#Shankar Vihar / National Highway 8

#Shiv Murti
#Jia Sarai

