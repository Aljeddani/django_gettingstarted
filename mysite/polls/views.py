from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello this is the polls app!!</h1>')