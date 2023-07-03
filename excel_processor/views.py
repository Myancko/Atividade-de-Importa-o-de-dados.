from django.shortcuts import render
import openpyxl, pandas as pd

# Create your views here.

def excel (request):
    
    if request.method == 'POST':
        
        
        teste = 'passou'
        print(request.FILES.keys())

        input('\n>>> waiting >>>')

    return render (request, 'sender.html', {})