from flask import Flask, render_template, request
app= Flask(__name__)
@app.route('/')


def index():
	return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		source = request.form['src']
		dest = request.form['dest']

		stops_dict={}
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


		# source=raw_input("Enter Source:")
		# dest=raw_input("Enter Destination:")

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
			result="Oops! Source Not Found"
			return render_template('result.html',result=result)
		if(dest_stop_id=="-1"):
			result="Oops! Destination Not Found"
			return render_template('result.html',result=result)

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
		result=""
		if(len(zero_hop_route_IDs)>0):
			# print("You can use any of the following 0-hop routes: ")
			for val in zero_hop_route_IDs:
				result+="RouteID: "
				result+=val 
				result+=" Route Name: "
				result+=routes_dict[val]
		else:
			result="No Route Found"

		return render_template('result.html',result=result)

if __name__ == "__main__":
	app.run(debug=True)