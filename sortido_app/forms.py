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
            members = r.json()

            if numberForSorted > len(members):
                error_msg = "Você não pode sortear mais pessoas que o evento possui"
            elif  len(members) == 0:
                error_msg = "Não há pessoas confirmadas no evento"
            else:
                while(numberForSorted != len(names)):
                    numberRandom = randint(0,len(members)-1)
                    name = members[numberRandom].get('member', {}).get('name')
                    names.add(name)
        else:
            error_msg = "Informe uma URL válida"

        return (names, error_msg)