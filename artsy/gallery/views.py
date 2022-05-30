from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
     images = Image.objects.all()
     category = Category.objects.all()
     locations = Location.get_location()

     if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)