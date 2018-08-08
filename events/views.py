from django.shortcuts import render
import requests
from . import requestdata
from django.http import HttpResponse,JsonResponse
# Create your views here.


def logdata(request):
    data = requestdata.alldata()
    return JsonResponse(data)

def home(request):
    final = requestdata.alldata()
    return render(request, 'home.html',{"data": final})