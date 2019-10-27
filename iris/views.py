from django.shortcuts import render
from .forms import IrisForm

# Create your views here.


def index(request):
    parameters_form = IrisForm()
    return render(request, 'index.html', {'form': parameters_form})