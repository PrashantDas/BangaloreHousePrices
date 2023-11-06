from django.shortcuts import render
from .forms import MyForm
import numpy as np
import pandas as pd

# Sklearn transformers
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

import pickle
pickled_Model = pickle.load(open('Model_rfr_Bangalore2023small.pkl', 'rb'))

# Create your views here.
def face(request):
    if request.method == 'POST':
        form_instance = MyForm(request.POST)
        if form_instance.is_valid():
            place = form_instance.cleaned_data.get('location')
            bhk = form_instance.cleaned_data.get('bhk')
            sqft = form_instance.cleaned_data.get('sqft')
            data = {'place': place, 'bhk': bhk, 'sqft': sqft}
            data_list = list(data.values())
            book = {key:value for key, value in zip(['location', 'total_sqft', 'bhk'], data_list)}
            input_array = pd.DataFrame(book, index=[0])
            pred_num = pickled_Model.predict(input_array)
            response = f"A {data_list[1]}-bhk apartment of size {data_list[2]}-sqft in {data_list[0]} will cost approx. {pred_num[0]} lakhs"
            return render(request, 'frontapp/main.html', {'that_form': MyForm(), 'data': response})
        else:
            return render(request, 'frontapp/main.html', {'that_form': MyForm()})
        
    else:
        return render(request, 'frontapp/main.html', {'that_form': MyForm()})

    
def contact(request):
    return render(request, 'frontapp/contact.html', {})
