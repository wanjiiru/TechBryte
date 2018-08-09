import json
import urllib.request

url = "https://api.meetup.com/2/concierge?offset=0&format=json&category_id=34&photo-host=public&page=500&sig_id=260256764&sig=7756bc69902a8df71bf518082b25d3073a17daf2"


def alldata():

    with urllib.request.urlopen(url) as dt:
        bytes = dt.read()
        entiredict = json.loads(bytes)
        mylist = entiredict['results']


    mydict = { "type": "FeatureCollection",
            "crs": {
                "type": "name",
                "properties": {
                    "name": "EPSG:4326"
                    },
                }
            }


    emptylist = []
    for x in mylist:
        if x.get("venue"):
            lat = x.get("venue").get("lat")
            lon = x.get("venue").get("lon")
            data = {
                "type": "Feature",
                "properties": {
                    "utc_offset": x.get("utc_offset"),
                    "venue" : x.get("venue"),
                    "headcount" : x.get("headcount"),
                    "id": x.get("id"),
                    "name": x.get("name"),
                    "photo_url": x.get("photo_url"),
                    "visibility": x.get("visibility"),
                    "waitlist_count": x.get("waitlist_count"),
                    "created": x.get("created"),
                    "time": x.get("time"),
                    "maybe_rsvp_count": x.get("maybe_rsvp_count"),
                    "description": x.get("description"),
                    "event_url": x.get("event_url"),
                    "status": x.get("status"),
                    "group": x.get("group"),
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon,lat],
                },
            }

            emptylist.append(data)

    mydict["features"] = emptylist
    return mydict