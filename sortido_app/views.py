from django.shortcuts import render
from .forms import *
from .functionalities import *
import os


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

def random_number(request):
    return render(request, 'random_number.html', {})
