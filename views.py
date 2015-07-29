from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers

import json

from submit.models import Game 

# Create your views here.

def main_page(request):
    context = {
        
    }
    return render(request, 'complete/main.html', context)

def api_search(request):
    search = request.GET.get('query') 
    data = serializers.serialize('json', Game.objects.filter(name__icontains = search), fields=('name'))
    #yes, I *am* decoding the freshly encoded json into another json
    #yes, I *know* that would be unncessary if I actually learned serializers
    datum = json.dumps({'suggestions':json.loads(data)})
    return HttpResponse(datum)

def api_get_id(request, game_id):
    try:
        data = get_object_or_404(Game.objects.filter(id = game_id))
    except:
        return HttpResponse('oops')
    #laaaazy
    formatted = '<b>' + data.name + '</b><br>' + data.developer.name + '<br>' + data.url + '<br>' + data.notes
    return HttpResponse(formatted)

def api_get_none(request):
    return HttpResponse('')
