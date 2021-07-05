from django.shortcuts import render
from django.http import HttpResponse
import pdb


def home_page(request):
    return render(request, 'lists/home.html')

