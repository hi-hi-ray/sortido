from django.shortcuts import render
from django.views.generic.edit import FormView
from django.conf import settings
from .forms import *
from random import randint
import os
import csv


# Route Home Page
def home(request):
    return render(request, 'index.html', {})

# Route Random with CSV
def random_csv(request):
    if request.method == 'GET':
        form = UploadFileForm()
        return render(request, 'random_csv.html', {'form': form})
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            errors_message = []
            random_persons_result = []
            csv_rows = []
            qtd_lines = 0
            i = 0

            number_of_times = int(request.POST['number_of_times'])
            file_form = request.FILES['csv_file']
            has_a_header = request.POST.get('has_a_header', False)

            file_name, file_extension = os.path.splitext(file_form.name)

            # Fields Treatment
            if number_of_times <= 0:
                errors_message.append('A quantidade de sorteio não pode ser menor do que 1.')
            if file_extension != '.csv':
                errors_message.append("O seu arquivo precisa ser um CSV.")



            # Random CSV
            if len(errors_message) != 0:
                return render(request, 'random_csv.html', {'form': form, 'validation_fail': True, 'errors_message': errors_message})
            else:
                # Create File
                with open("tmp/file" + file_form.name, 'wb+') as destination:
                    for chunk in file_form.chunks():
                        destination.write(chunk)
                destination.close()
                # Pass the values to a list
                with open("tmp/file" + file_form.name, 'r') as file:
                    for row in file:
                        csv_rows.append(row.replace('\n', ''))
                file.close()

                # Remove File
                os.remove("tmp/file" + file_form.name)

                while i != number_of_times:
                    chosen_person = ''
                    if has_a_header:
                        chosen_person = csv_rows[randint(1, len(csv_rows) - 1)]
                    else:
                        chosen_person = csv_rows[randint(0, len(csv_rows) - 1)]
                    if chosen_person in random_persons_result:
                        number_of_times += 1
                    else:
                        random_persons_result.append(chosen_person)
                    i += 1
                return render(request, 'random_csv.html', {'form': form, 'random_done': True, 'form_result': random_persons_result})

# Route Random with Numbers
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
            errors_message = []
            numbers_of_results = []
            i = 0
            if quantity_random <= 0:
                errors_message.append('A quantidade de sorteio não pode ser menor do que 1.')
            if first_number >= second_number:
                errors_message.append('O segundo número (Até) não pode ser menor que o primeiro número (De).')
            if ((second_number - first_number) + 1) < quantity_random and is_possible_same_number is False:
                errors_message.append('Você não marcou que deseja repetir os números e a quantidade de números entre um e outro não é suficiente para conseguirmos fazer um sorteio de números diferentes. Por favor reveja a sua solicitação.')
            if len(errors_message) != 0:
                return render(request, 'random_numbers.html', {'form': form, 'validation_fail': True, 'errors_message': errors_message})
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

# Route About
def about(request):
    return render(request, 'about.html', {})

# Route Random with Meetup
def random_meetup(request):

    if request.method == "GET":
        form = MeetupForm()
        return render(request, 'random_meetup.html', { 'form' : form})

    elif request.method == "POST":
        form = MeetupForm(request.POST)

        errors_message = []

        url = request.POST['url']
        quantityOfPersons = request.POST['quantity_of_persons']

        urlPaths = url.split("/")

        if "https://www.meetup.com" not in url:
            errors_message.append("Sua URL precisa ser do https://www.meetup.com")
        elif len(urlPaths) < 7:
            errors_message.append("Sua URL está mal formatada")
        elif urlPaths[4] == "" or urlPaths[6] == "":
            errors_message.append("Sua URL está incompleta")

        if len(errors_message) == 0:
            result = form.random_person(urlPaths[4], urlPaths[6], quantityOfPersons)

            if result[1] != "":
                errors_message.append(result[1])

            return render(request, 'random_meetup.html', { 'form' : form, 'errors_message': errors_message, 'lucky_ones' : result[0]})
        else:
            return render(request, 'random_meetup.html', { 'form' : form, 'errors_message': errors_message, 'lucky_ones' : []})
