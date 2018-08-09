from django.shortcuts import render
import requests
from . import requestdata
from django.http import HttpResponse,JsonResponse
from datetime import datetime




def logdata(request):
    final = requestdata.alldata()
    for x in final["features"]:
        w_date = x.get("properties")["time"]
        f_date = datetime.utcfromtimestamp(int(w_date)/1e3)
        # print(f_date)
        x.get("properties")["time"] = f_date
    return JsonResponse(final,safe=False)

def home(request):
   final = requestdata.alldata()
   for x in final["features"]:
        w_date = x.get("properties")["time"]
        f_date = datetime.utcfromtimestamp(int(w_date)/1e3)
        print(f_date)
        x.get("properties")["time"] = f_date
   return render(request, 'home.html',{"data": final})


