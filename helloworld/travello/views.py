from django.shortcuts import render
from django.http import request
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name='Dhaka'
    dest1.desc= 'Metro city'
    dest1.img = 'destination_1.jpg'
    dest1.price = 750

    dest2 = Destination()
    dest2.name='CoxBazar'
    dest2.desc= 'Sea Beach'
    dest2.img = 'destination_2.jpg'
    dest2.price = 850

    dest3 = Destination()
    dest3.name='Bogra'
    dest3.desc= 'Best city'
    dest3.img = 'destination_3.jpg'
    dest3.price = 700

    dest = [dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dest})