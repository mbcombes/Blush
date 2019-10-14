from django.shortcuts import render


def index(request):
    return render(request, 'blush/index.html')

def stylist(request):
    return render(request, "blush/stylist.html")
# Create your views here.
