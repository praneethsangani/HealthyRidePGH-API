# HealthyRidePGH API
Invocation:
```
python3 mybikes.py baseURL command [parameters]  
```

### Data Feeds
Use two data feeds from the HealthyRidePGH General Bikeshare Feed Specification (GBFS) data feed, as follows:
* **Station Information**: $station_infoURL = $baseURL+'/station_information.json', which provides for each docking station: station_id, name, latitude 
 and longtitude, and the total capacity (e.g., [https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/station_information.json](https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/station_information.json)).   

* **Station Status**: $station_statusURL = $baseURL+'/station_status.json', which provides for each station_id how many bikes and how many docks are available at any given time (e.g., [https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/station_status.json](https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/station_status.json)).

You can find additional information about the GBFS specification at [https://github.com/NABSA/gbfs](https://github.com/NABSA/gbfs) and about all the available data feeds from HealthyRidePGH at [https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/gbfs.json](https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/gbfs.json).

### Command #1: Total bikes available
The command `total_bikes` will compute how many bikes are currently available over all stations in the entire HealthRidePGH network. 

Sample invocation:
```
python3 mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ total_bikes
```

Sample output of your script (meant to illustrate format only):
```
Command=total_bikes 
Parameters=
Output=123
```

### Command #2: Total docks available
The command `total_docks` will compute how many docks are currently available over all stations in the entire HealthRidePGH network. 

Sample invocation:
```
python3 mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ total_docks
```

Sample output of your script (meant to illustrate format only):
```
Command=total_docks
Parameters=
Output=168
```

### Command #3: Percentage of docks available in a specific station
The command `percent_avail` will compute how many docks are currently available for the specified station as a percentage over the total number of bikes and docks available. In this case, the station_id is given as a parameter.

Sample invocation:
```
python3 mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ percent_avail 342885
```

Sample output of your script (meant to illustrate format only):
```
Command=percent_avail
Parameters=342885
Output=76%
```
### Command #4: Names of three closest HealthyRidePGH stations.
The command `closest_stations` will return the station_ids and the names of the three closest HealthyRidePGH stations based just on latitude and longtitude (of the stations and of the specified location). The first parameter is the latitude and the second parameter is the longtitude. 

Sample invocation:
```
python3 mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ closest_stations 40.444618 -79.954707
```

Sample output of your script (meant to illustrate format only):
```
Command=closest_stations
Parameters=40.444618 -79.954707
Output=
342885, Schenley Dr at Schenley Plaza (Carnegie Library Main) 
342887, Fifth Ave & S Dithridge St
342882, Fifth Ave & S Bouquet St
```

### Command #5: Name of the closest HealthyRidePGH station with available bikes
The command `closest_bike` will return the station_id and the name of the closest HealthyRidePGH station that has available bikes, given a specific latitude and longtitude. The first parameter is the latitude and the second parameter is the longtitude. 

Sample invocation:
```
python3 mybikes.py https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en/ closest_bike 40.444618 -79.954707
```

Sample output of your script (meant to illustrate format only):
```
Command=closest_bike
Parameters=40.444618 -79.954707
Output=342887, Fifth Ave & S Dithridge St
```
This was a project for CS1656 at the University of Pittsburgh
