from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

    # For news link


def news(request):
    return render(request, 'news.html')


def contact(request):
    return render(request, 'contact.html')
