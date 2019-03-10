from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def random_csv(request):
    return render(request, 'random_csv.html', {})

def random_number(request):
    return render(request, 'random_number.html', {})
