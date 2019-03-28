from django.shortcuts import render
from .forms import *
from random import randint


def home(request):
    return render(request, 'index.html', {})

def random_csv(request):
    return render(request, 'random_csv.html', {})

def random_numbers(request):
    if request.method == 'GET':
        form = RandomNumbersForm()
        return render(request, 'random_numbers.html', {'form': form})
    elif request.method == 'POST':
        form = RandomNumbersForm(request.POST)
        if form.is_valid():
            quantity_random = int(request.POST['quantity_random'])
            first_number = int(request.POST['first_number'])
            second_number = int(request.POST['second_number'])
            numbers_of_results = []

            for i in range(quantity_random):
                numbers_of_results.append(randint(first_number, second_number))
                print(numbers_of_results)

            return render(request, 'random_numbers.html', {'form': form, 'random_done': True, 'form_result': numbers_of_results})

def about(request):
    return render(request, 'about.html', {})
