from django.shortcuts import render
from strains.models import Strain


# Create your views here.

def do_search(request):
    strains = Strain.objects.filter(name__icontains=request.GET['q'])
    return render(request, "strains.html", {"strains":strains})
