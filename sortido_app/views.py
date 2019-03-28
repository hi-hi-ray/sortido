from django.shortcuts import render
from .forms import *
from random import randint


def home(request):
    return render(request, 'index.html', {})

def random_csv(request):
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request, 'random_csv.html', {'form': form})
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            number_of_times = request.POST['number_of_times']
            file_reference = RandomWithCsv.handle_uploaded_file(request.FILES['csv_file'])
            file_path = os.path.join(settings.BASE_DIR, file_reference)
            return render(request, 'random_csv.html',  {'form': form, 'random_done': True})

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
            is_possible_same_number = request.POST.get('is_possible_same_number', False)
            numbers_of_results = []
            i = 0

            if first_number <= second_number:
                pass
            elif (second_number - first_number) > quantity_random:
                pass

            if is_possible_same_number:
                for i in range(quantity_random):
                    numbers_of_results.append(randint(first_number, second_number))
                return render(request, 'random_numbers.html', {'form': form, 'random_done': True, 'form_result': numbers_of_results})
            else:
                while i != quantity_random:
                    number = randint(first_number, second_number)
                    if number in numbers_of_results:
                        quantity_random = quantity_random + 1
                    else:
                        numbers_of_results.append(number)
                    i += 1

            return render(request, 'random_numbers.html', {'form': form, 'random_done': True, 'form_result': numbers_of_results})

def about(request):
    return render(request, 'about.html', {})
