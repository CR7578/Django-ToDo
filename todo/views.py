from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def taskDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def taskNotdone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.task = request.POST['task']
    task.save()
    return redirect('home')
