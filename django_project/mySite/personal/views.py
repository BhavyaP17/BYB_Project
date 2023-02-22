from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
"""
def index(request):
    return HttpResponse("<h2>Hello World</h2>")
"""


def index(request):
    return render(request, 'index.html')


def Contact(request):
    return render(request, 'Contact.html')


def CV(request):
    return render(request, 'CV.html')


def OnlineShoppingWebsite(request):
    return render(request, 'OnlineShoppingWebsite.html')
