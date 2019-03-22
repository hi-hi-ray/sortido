from django.shortcuts import render
from .forms import *


def home(request):
    return render(request, 'index.html', {})

def random_csv(request):
    return render(request, 'random_csv.html', {})

def random_numbers(request):
    return render(request, 'random_numbers.html', {})

def about(request):
    return render(request, 'about.html', {})
