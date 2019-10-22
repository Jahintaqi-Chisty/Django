from django.shortcuts import render
from django.http import request


# Create your views here.
def index(request):
    return render(request,'index.html')

#For news link 
def news(request):
    return render(request,'news.html')
