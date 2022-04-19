import imp
from django.shortcuts import render
from Home.models import Teams

# Create your views here.

def home(request):
    return render(request, 'Home/index.html')


def about(request):
    teams = Teams.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'Home/about.html', context)