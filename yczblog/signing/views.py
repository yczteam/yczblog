# Create your views here.
from django.shortcuts import render

def index(request):
    
    #template = loader.get_template('signing/index.html')
    context = {
        'welcome': 'Welcome to yczblog!',
        'contact': 'please contact us at yczteam@gmail.com',
    }
    return render(request, 'signing/index.html', context)

def signUp(request):
    return render(request, 'signing/index.html')

def signIn(request):
    return render(request, 'signing/index.html')


