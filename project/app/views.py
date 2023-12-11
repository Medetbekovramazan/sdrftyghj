from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index (request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return HttpResponse(f'Name: {name}')
        else:
            return HttpResponse('Данные не валидны')
        name = request.POST.get('name')
        return  HttpResponse(f'Name:{name}')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})



