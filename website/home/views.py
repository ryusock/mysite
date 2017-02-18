from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def landing(request):
    return render(request, 'home/landing.html')

def index(request):
    return render(request, 'home/index.html')
