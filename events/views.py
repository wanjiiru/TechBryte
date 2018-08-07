from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response = requests.get('https://api.meetup.com/2/concierge?offset=0&format=json&category_id=34&photo-host=public&page=500&sig_id=260256764&sig=7756bc69902a8df71bf518082b25d3073a17daf2')
    eventsdata = response.json()
    data = eventsdata['results']
    return render(request,'home.html', {
        'results':data,
    })
