from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import Person


def index(request):
    context = {}
    return render(request, 'broker/index.html', context)
