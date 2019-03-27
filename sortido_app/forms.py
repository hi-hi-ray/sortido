from django import forms


class UploadFileForm(forms.Form):
    number_of_times = forms.IntegerField(label='Quantidade de Pessoas', required=True)
    csv_file = forms.FileField(label='Arquivo CSV', required=True)
