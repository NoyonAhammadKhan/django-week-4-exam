from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = TaskForm()
    return render(request, 'add_task.html', {'form': task_form})


def update_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    return render(request, 'add_task.html', {'form': task_form})


def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')
