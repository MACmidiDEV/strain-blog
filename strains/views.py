from django.shortcuts import render
from .models import Strain

# Create your views here.
def all_strains(request):
    strains = Strain.objects.all()
    return render( request, "strains.html", { "strains": strains } )

