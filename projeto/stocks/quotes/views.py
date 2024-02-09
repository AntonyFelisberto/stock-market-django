from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error ..."

    return render(request,"home.html",{"api":api})

def about(request):
    return render(request,"about.html",{})