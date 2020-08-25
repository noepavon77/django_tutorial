from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, este es el index de polls.")

# Create your views here.
