from django import forms
import json

with open('Json_locations.json', 'r') as fread:
    contents = json.load(fread)

class MyForm(forms.Form):
    choi = [(key, value) for key, value in contents.items()]
    location = forms.ChoiceField(widget=forms.Select, choices=choi, label='Location of the property')
    bhk      = forms.IntegerField(min_value=1, max_value=10, label='BHK')
    sqft     = forms.IntegerField(min_value=300, max_value=14000, label='Square-feet', step_size=50)
