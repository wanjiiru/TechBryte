from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response = requests.get('https://api.meetup.com/find/upcoming_events?photo-host=public&topic_category=Tech&page=20&sig_id=260256764&sig=bb02ef627855aef92d68cf80c35610403cfab2ec')
    eventsdata = response.json()
    data = eventsdata['events']
    return render(request,'home.html', {
        'events':data,
    })
