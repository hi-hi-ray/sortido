from django import forms


class RandomNumbersForm(forms.Form):
    quantity_random = forms.IntegerField(label='Quantidade de vezes que será feito o sorteio', required=True)
    first_number = forms.IntegerField(label='De', required=True)
    second_number = forms.IntegerField(label='Até', required=True)
