from django.shortcuts import render
from django.http import HttpResponse
# from Templates.ToDo_app import list
# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'ToDo_app/list.html')
