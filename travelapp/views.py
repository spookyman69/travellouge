from django.http import HttpResponse
from django.shortcuts import render

from travelapp.models import Place


# Create your views here.
def demo(request):
    place = Place.objects.all()
    return render(request, "index.html", {"places":place})


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse("THis is contact")


def phone(request):
    return HttpResponse("Phone number")
