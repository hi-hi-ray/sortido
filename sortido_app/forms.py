from django import forms
from random import randint
import requests
import json

class MeetupForm(forms.Form):
    quantity_of_persons = forms.IntegerField(label='Quantidade de Pessoas')
    url = forms.CharField(label='Url do Evento')

    def random_person(self, group, id, quantity_of_persons):
        numberForSorted = int(quantity_of_persons)
        endpoint = 'https://api.meetup.com/'+group+'/events/'+id+'/attendance'
        r = requests.get(endpoint)

        names = set()
        error_msg = ""

        if r.status_code == requests.codes.ok:
            allMembers = r.json()
            checkedMembers = []
            for member in allMembers:
                if(member.get('rsvp', {}).get('response')=='yes'):
                    checkedMembers.append(member)
            
            if numberForSorted > len(checkedMembers):
                error_msg = "O evento possui "+ str(len(checkedMembers)) +" pessoas confirmadas. Você não pode sortear mais pessoas que o evento possui "
            elif  len(checkedMembers) == 0:
                error_msg = "Não há pessoas confirmadas no evento"
            else:
                while(numberForSorted != len(names)):
                    numberRandom = randint(0,len(checkedMembers)-1)
                    name = checkedMembers[numberRandom].get('member', {}).get('name')
                    names.add(name)
        else:
            error_msg = "Informe uma URL válida"
        return (names, error_msg)

class RandomNumbersForm(forms.Form):
    quantity_random = forms.IntegerField(label='Quantidade de vezes que será feito o sorteio', required=True)
    is_possible_same_number = forms.BooleanField(label='Quer que repetimos os números?', initial=False, required=False)
    first_number = forms.IntegerField(label='De', required=True)
    second_number = forms.IntegerField(label='Até', required=True)

class UploadFileForm(forms.Form):
    number_of_times = forms.IntegerField(label='Quantidade de Pessoas', required=True)
    csv_file = forms.FileField(label='Arquivo CSV', required=True)
    has_a_header = forms.BooleanField(label='Seu CSV possui um Header de uma linha?', initial=False, required=False)
