from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):

    if request.method == 'POST':
        ticker = request.POST["ticker"]
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_0920b6af199d4c87acc868419bf91e38")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ..."

        return render(request,"home.html",{"api":api})
    else:
        return render(request,"home.html",{"ticker":"enter a ticker: ","api":" "})

def about(request):
    return render(request,"about.html",{})