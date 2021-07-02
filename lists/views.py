from django.shortcuts import render
from django.http import HttpResponse
import pdb


def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
    # return render(request, 'lists/teste.html')

