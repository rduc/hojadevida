from django.shortcuts import render
from .models import Certif

def certifica(request):
        certifs = Certif.objects.all()  
        return render(request, "certifica/certifica.html", 
            {'certifs':certifs}) 