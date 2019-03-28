from django import forms


class RandomNumbersForm(forms.Form):
    quantity_random = forms.IntegerField(label='Quantidade de vezes que será feito o sorteio', required=True)
    is_possible_same_number = forms.BooleanField(label='Quer que repetimos os números?', initial=False, required=False)
    first_number = forms.IntegerField(label='De', required=True)
    second_number = forms.IntegerField(label='Até', required=True)
