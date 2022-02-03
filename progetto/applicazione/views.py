from typing import Container
from django.shortcuts import render
from .models import recipe

# Create your views here.

def homepage(request):
    Container = recipe.objects.all()
    return render(request,'applicazione/homepage.html',{'Cointainer': Container})

