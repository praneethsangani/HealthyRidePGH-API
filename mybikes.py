#Praneeth Sangani
#CS1656 - Project 1

from argparse import ArgumentParser
from collections import Counter
from json import loads
from math import cos, asin, sqrt, floor

from requests import get

############################################# USAGE #############################################
# python3 mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ <COMMAND> <OTHER ARGS>
# COMMANDS: <total_bikes, total_docks, percent_avail, closest_stations, closest_bike>
# OTHER ARGS: percent_avail needs stations id, closest_stations & closest_bike need lat and long
#################################################################################################

#Compute distance between the 2 lat & lon
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

#Process the passed arguments
parser = ArgumentParser(description="Processing url and commands")
parser.add_argument("URL", help="URL for the data feed")
parser.add_argument("COMMAND", help="The command you want to run e.g. total_bikes")
parser.add_argument("LAT", help="If the command you want to run is percent_avail pass the station id, otherwise pass the latitude", nargs="?", default="") #Note that this can also be the station id for the command percent_avail
parser.add_argument("LON", help="If the command you want to run is percent_avail pass the station id, otherwise pass the latitude", nargs="?", default="")
args = parser.parse_args()

#Make sure that we are appending properly to have the proper url
if not args.URL.endswith("/"):
    url = args.URL + "/"
else:
    url = args.URL

#Command 1 - total_bikes: total bikes available
if args.COMMAND == "total_bikes":
    response = get(url + "station_status.json")
    stations = loads(response.content)

    total_bikes = 0
    for station in stations["data"]["stations"]:
        total_bikes += station.get("num_bikes_available")

    print("Command= " + args.COMMAND)
    print("Parameters= " + str(args.LAT) + " " + str(args.LON))
    print("Output= " + str(total_bikes))

#Command 2 - total_docks: total docks available
elif args.COMMAND == "total_docks":
    response = get(url + "station_status.json")
    stations = loads(response.content)

    total_docks = 0
    for station in stations["data"]["stations"]:
        total_docks += station.get("num_docks_available")

    print("Command= " + args.COMMAND)
    print("Parameters= " + str(args.LAT) + " " + str(args.LON))
    print("Output= " + str(total_docks))

#Command 3 - percent_avail: percentage of docks available in a specific station
elif args.COMMAND == "percent_avail":
    response = get(url + "station_status.json")
    stations = loads(response.content)

    for station in stations["data"]["stations"]:
        if(station.get("station_id") == args.LAT):
            percent_avail = floor(100 * (station.get("num_docks_available") / (station.get("num_bikes_available") + station.get("num_docks_available")))) #Calculate percentage of docks available in a specific station (total docks available / (total bikes available + total docks available))
            break;

    if(station.get("station_id") == args.LAT):
        print("Command= " + args.COMMAND)
        print("Parameters= " + str(args.LAT) + " " + str(args.LON))
        print("Output= " + str(percent_avail) + "%")
    else:
        print("A station with that ID was not found")

#Command 4 - closest_stations: names of three closest HealthyRidePGH stations
elif args.COMMAND == "closest_stations":
    if args.LAT == "" or args.LAT == "":
        print("Need to provide arguemnts lat and lon")
    else:
        response = get(url + "station_information.json")
        stations = loads(response.content)

        shortest_distances = {} #Maps the "station id, address" to the distance
        for station in stations["data"]["stations"]:
            shortest_distances.update({station.get("station_id") + ", " + station.get("name") : distance(float(args.LAT), float(args.LON), station.get("lat"), station.get("lon"))}) #calculate the distance and add it to the map

        shortest = Counter(shortest_distances).most_common()      #orders the values based on distance
        shortest_3 = shortest[-3:]                                #get the shortest 3 locations

        print("Command= " + args.COMMAND)
        print("Parameters= " + str(args.LAT) + " " + str(args.LON))
        print("Output=")
        print(shortest_3[2][0])
        print(shortest_3[1][0])
        print(shortest_3[0][0])

#Command 5 - closest_bike: the station_id and the name of the closest HealthyRidePGH station that has available bikes
elif args.COMMAND == "closest_bike":
    if args.LAT == "" or args.LAT == "":
        print("Need to provide arguemnts lat and lon")
    else:
        response = get(url + "station_information.json")
        stations = loads(response.content)

        shortest_distances = {} #Maps the "station id, address" to the distance
        for station in stations["data"]["stations"]:
            shortest_distances.update({station.get("station_id") + ", " + station.get("name") : distance(float(args.LAT), float(args.LON), station.get("lat"), station.get("lon"))}) #calculate the distance and add it to the map

        response = get(url + "station_status.json")
        stations = loads(response.content)

        stations_with_bikes = []
        for station in stations["data"]["stations"]:
             if station.get("num_bikes_available") > 0:
                 stations_with_bikes.append(station.get("station_id"))

        print("Command= " + args.COMMAND)
        print("Parameters= " + str(args.LAT) + " " + str(args.LON))

        shortest = Counter(shortest_distances).most_common()  # orders the values based on distance
        shortest.reverse();                                   # smallest first

        for station in shortest:
            if station[0].split(",")[0] in stations_with_bikes:
                print("Output= " + station[0])
            break;

else:
    print("That is not a valid command: valid commands are <total_bikes, total_docks, percent_avail, closest_stations, closest_bike>")




