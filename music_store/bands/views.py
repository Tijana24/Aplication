from django.shortcuts import render
from .models import Band

def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all() #SELECT * from BAND
    #first_band= Band.objects.first()
    #print(first_band)
    return render(request, 'bands/band_listing.html', {'bands': bands})

def band_detail(request, band_id):
    """A view of bands details."""
    bands = Band.objects.get(pk=band_id) 
    return render(request, 'bands/band_detail.html', {'bands': bands})

def band_search(request):
    """A view of bands details."""
    queried_band= request.GET['q']
    try:
        band = Band.objects.get(name=queried_band) 
        queried_band_exists= True
    except:
        queried_band_exists=False
        return render(request, 'bands/band_searched.html', {'band': band, 'result': queried_band_exists})

