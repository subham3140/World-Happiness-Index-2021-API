from django.shortcuts import render
from .models import HappyIndexTable
from django.http import HttpResponse
# Create your views here.

def home(request):
    countries = HappyIndexTable.objects.all()
    return render(request, "index.html", context={"countries": countries})


def searchByCountry(request):
    country = request.GET["country"]
    try:
       countryObj = HappyIndexTable.objects.get(countryName__icontains=country)
    except:
        return HttpResponse("Country Does Not Exists!")
    return render(request, 'getCountry.html', context={"country": countryObj})    

def searchByLadder(request):
    try:
      scorefrom = float(request.GET.get("from"))
    except:
        scorefrom = 0
    try:      
        scoreto = float(request.GET.get("to"))
    except:
        scoreto = 0    
    countries = HappyIndexTable.objects.filter(ladderScore__gte=scorefrom, ladderScore__lte=scoreto)
    if len(countries) == 0:
        return HttpResponse("Country Does Not Exists!")  
    return render(request, 'getdatabyladder.html', context={"countries": countries})    