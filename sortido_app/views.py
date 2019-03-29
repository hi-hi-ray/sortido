from django.shortcuts import render
from .forms import MeetupForm
from django.views.generic.edit import FormView


def home(request):
    return render(request, 'index.html', {})

def random_csv(request):
    return render(request, 'random_csv.html', {})

def random_numbers(request):
    return render(request, 'random_numbers.html', {})

def about(request):
    return render(request, 'about.html', {})

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