from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.

def main_page(request):
    context = {
        
    }
    return render(request, 'complete/main.html', context)

def api_result(request):
    return HttpResponse('nothing here now')
