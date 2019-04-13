source=raw_input("Enter Source:")
dest=raw_input("Enter Destination:")
stops=open("stops.txt","r")
count=0
src_dest_found=0
src_stop_id="-1"
dest_stop_id="-1"

for line in stops:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")

	if (fields[2] == source):
		src_stop_id=fields[0]
		print("Source Stop ID is: " + src_stop_id)
		src_dest_found+=1

	elif (fields[2]==dest):
		dest_stop_id=fields[0]
		print("Destination Stop ID is: " + dest_stop_id)
		src_dest_found+=1

	if(src_dest_found==2):
		break

stops.close()

if(src_stop_id=="-1"):
	print("Source not found..")
if(dest_stop_id=="-1"):
	print("Destination not found")

#----------------------------------------
count=0
stoptimes=open("stop_times.txt","r")
src_tripIDs=[]
dest_tripIDs=[]
for line in stoptimes:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")
	if(fields[3]==src_stop_id):
		src_tripIDs.append(fields[0])
	elif(fields[3]==dest_stop_id):
		dest_tripIDs.append(fields[0])

src_tripIDs.sort()
dest_tripIDs.sort()
print(len(src_tripIDs))
print(len(dest_tripIDs))
print(src_tripIDs[0])
stoptimes.close()
#----------------------------------------
count2=0
count=0
trips=open("trips.txt","r")
src_routeIDs=[]
dest_routeIDs=[]
for line in trips:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")
	
	for i in range(len(src_tripIDs)):
		count2+=1
		print(count2)
		#print("tripid is: "+src_tripIDs[i])
		# if(src_tripIDs[i]==fields[2]):	
		# 	src_routeIDs.append(fields[0])
	for tripID in dest_tripIDs:
		if(tripID==fields[2]):
			dest_routeIDs.append(fields[0])

src_routeIDs.sort()
dest_routeIDs.sort()
print(len(src_routeIDs))
print(len(dest_routeIDs))
trips.close()
#----------------------------------------

zero_hop_route_IDs=[]

for x in src_routeIDs:
	for y in dest_routeIDs:
		if(x==y):
			print("0 hop route found!")
			zero_hop_route_IDs.append(x)

#-----------------------------------------
count=0
if(len(zero_hop_route_IDs)>0):
	routes=open("routes.txt","r")
	print("You can use any of the following 0-hop routes: ")
	for line in routes:
		count+=1
		if(count==1):
			continue
		fields=line.split(",")
		if(fields[3] in zero_hop_route_IDs):
			print(fields[2])

#------------------1-Hop------------------
count=0
src_reachable_stops={}			#stops reachable from source 	  <"764"=[s1,s2,s3...]>
dest_reachable_stops={}			#stops reachable from destination <"764"=[s1,s2,s3...]>
src_route_tripIDs={}			#trip ids of all routes which touch the source
dest_route_tripIDs={}			#trip ids of all routes which touch the destination
src_trip_to_route={}
dest_trip_to_route={}

trips=open("trips.txt","r")
for line in trips:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")
	if(fields[0] in src_routeIDs):
		src_route_tripIDs.setdefault(fields[0],[]).append(fields[2])	#save trip id 
		src_trip_to_route.setdefault(fields[2],[]).append(fields[0])

	if(fields[0] in dest_routeIDs):
		dest_route_tripIDs.setdefault(fields[0],[]).append(fields[2])
		dest_trip_to_route.setdefault(fields[2],[]).append(fields[0])

trips.close()
count=0

stoptimes=open("stop_times.txt","r")
for line in stoptimes:
	count+=1
	if(count==1):
		continue
	fields=line.split(",")
	if(fields[0] in src_trip_to_route.keys()):
		if(fields[3]!=src_stop_id and fields[3]!=dest_stop_id):
			src_reachable_stops.setdefault(src_trip_to_route.get(fields[0]),[]).append(fields[3])		#save stops which are reachable from source
	if(fields[0] in dest_route_tripIDs):	
		if(fields[3]!=src_stop_id and fields[3]!=dest_stop_id):
			dest_reachable_stops.setdefault(dest_trip_to_route.get(fields[0]),[]).append(fields[3])		#save stops which are reachable from destination

stoptimes.close()

one_hop_routes=set()

for bus_no in src_reachable_stops:
	for bus_no_dest in dest_reachable_stops:
		if(set(src_reachable_stops.get(bus_no)) & set(dest_reachable_stops.get(bus_no_dest))):
			one_hop_routes.add(bus_no+"->"+bus_no_dest)

print("One Hop Routes are:")
for x in one_hop_routes:
	print(x)




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

