from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Todo
from .models import Task
# from Templates.ToDo_app import list
# Create your views here.

from .models import *

def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
    elif request.method == 'POST':
        form = Todo(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'tasks':tasks}
    return render(request, 'ToDo_app/list.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    form = Todo(instance = task)

    if request.method == "DELETE":
        task.delete()
        return redirect('index')
    
    elif request.method == "POST":
        # form = Todo(instance = task)
        print(task)
        return redirect('index')
         
    context = {'form':form}
    return render(request, 'ToDo_app/list.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = Todo(instance = task)
    print(task)
    # if request.method == 'POST':
    #     form = Todo(request.post, instance=task)
    context = {'form':form}
    return redirect('index', context)




