from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUser

def index(request):

    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
    form = NewUser()
    context = {'form' : form}
    return render(request, 'index.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)
