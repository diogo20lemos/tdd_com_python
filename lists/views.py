from django.shortcuts import render
import pdb


def home_page(request):
    return render(request, 'lists/teste.html')

