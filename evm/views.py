from django.contrib.sessions import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from evm.models import Dataset
import numpy as np
from pandas import DataFrame
def post_list(request):
    return render(request, 'evm/post_list.html',{})
from decimal import *
def update(request):
    dataset = Dataset.objects.all()
    data = []
    for each in dataset:
        data.append(each.dic())
    columns = [
            'city_id', 'time', 'temperature', 'rainfall', 'windspeed',
            'humidity', 'total_traffic'
        ]
    df = DataFrame(data=data, columns=columns)
    
    return JsonResponse(df.to_json(), safe=False)